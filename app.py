import os
from datetime import datetime
from functools import wraps
from pathlib import Path

from flask import Flask, abort, flash, redirect, render_template, request, session, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash


BASE_DIR = Path(__file__).resolve().parent
app = Flask(__name__, instance_relative_config=True)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "dev-key-change-before-deploy")
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
    "DATABASE_URL", f"sqlite:///{BASE_DIR / 'instance' / 'gymmanager.db'}"
).replace("mysql://", "mysql+pymysql://", 1)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
Path(app.instance_path).mkdir(parents=True, exist_ok=True)
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(160), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(20), nullable=False)
    trainer_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    students = db.relationship("User", backref=db.backref("trainer", remote_side=[id]))


class Exercise(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    trainer_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    name = db.Column(db.String(120), nullable=False)
    muscle_group = db.Column(db.String(80), nullable=False)
    description = db.Column(db.Text, default="")


class Workout(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    trainer_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    title = db.Column(db.String(120), nullable=False)
    notes = db.Column(db.Text, default="")
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    items = db.relationship("WorkoutItem", backref="workout", cascade="all, delete-orphan")
    student = db.relationship("User", foreign_keys=[student_id])


class WorkoutItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    workout_id = db.Column(db.Integer, db.ForeignKey("workout.id"), nullable=False)
    exercise_id = db.Column(db.Integer, db.ForeignKey("exercise.id"), nullable=False)
    sets = db.Column(db.Integer, nullable=False)
    reps = db.Column(db.String(40), nullable=False)
    load = db.Column(db.String(40), default="")
    rest = db.Column(db.String(40), default="")
    exercise = db.relationship("Exercise")


def signed_in_user():
    user_id = session.get("user_id")
    return db.session.get(User, user_id) if user_id else None


def login_required(view):
    @wraps(view)
    def wrapped(*args, **kwargs):
        if not signed_in_user():
            return redirect(url_for("login"))
        return view(*args, **kwargs)

    return wrapped


def trainer_required(view):
    @wraps(view)
    @login_required
    def wrapped(*args, **kwargs):
        if signed_in_user().role != "trainer":
            abort(403)
        return view(*args, **kwargs)

    return wrapped


@app.route("/login", methods=["GET", "POST"])
def login():
    if signed_in_user():
        return redirect(url_for("dashboard"))
    if request.method == "POST":
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")
        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password_hash, password):
            session.clear()
            session["user_id"] = user.id
            return redirect(url_for("dashboard"))
        flash("E-mail ou senha inválidos.", "error")
    return render_template("index.html", user=None)


@app.route("/logout", methods=["POST"])
def logout():
    session.clear()
    return redirect(url_for("login"))


@app.route("/")
@login_required
def dashboard():
    user = signed_in_user()
    if user.role == "student":
        workouts = Workout.query.filter_by(student_id=user.id).order_by(Workout.created_at.desc()).all()
        return render_template("index.html", user=user, workouts=workouts, page="student")
    return render_template("index.html", **trainer_dashboard_data(user, "overview"))


def trainer_dashboard_data(user, page):
    return {
        "user": user,
        "page": page,
        "students": User.query.filter_by(trainer_id=user.id, role="student").order_by(User.name).all(),
        "exercises": Exercise.query.filter_by(trainer_id=user.id).order_by(Exercise.name).all(),
        "workouts": Workout.query.filter_by(trainer_id=user.id).order_by(Workout.created_at.desc()).all(),
    }


@app.get("/students")
@trainer_required
def students_page():
    return render_template("index.html", **trainer_dashboard_data(signed_in_user(), "students"))


@app.get("/exercises")
@trainer_required
def exercises_page():
    return render_template("index.html", **trainer_dashboard_data(signed_in_user(), "exercises"))


@app.get("/workouts")
@trainer_required
def workouts_page():
    return render_template("index.html", **trainer_dashboard_data(signed_in_user(), "workouts"))


@app.post("/students")
@trainer_required
def add_student():
    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip().lower()
    if not name or not email or User.query.filter_by(email=email).first():
        flash("Informe nome e e-mail válidos e ainda não cadastrados.", "error")
    else:
        student = User(
            name=name,
            email=email,
            password_hash=generate_password_hash(request.form.get("password") or "treino123"),
            role="student",
            trainer_id=signed_in_user().id,
        )
        db.session.add(student)
        db.session.commit()
        flash("Aluno cadastrado. A senha inicial é treino123, caso não tenha sido definida.", "success")
    return redirect(url_for("students_page"))


@app.post("/students/<int:student_id>/delete")
@trainer_required
def delete_student(student_id):
    student = User.query.filter_by(id=student_id, trainer_id=signed_in_user().id, role="student").first_or_404()
    Workout.query.filter_by(student_id=student.id).delete()
    db.session.delete(student)
    db.session.commit()
    flash("Aluno removido.", "success")
    return redirect(url_for("students_page"))


@app.post("/exercises")
@trainer_required
def add_exercise():
    name = request.form.get("name", "").strip()
    muscle_group = request.form.get("muscle_group", "").strip()
    if not name or not muscle_group:
        flash("Preencha o nome e o grupo muscular do exercício.", "error")
    else:
        db.session.add(Exercise(
            trainer_id=signed_in_user().id,
            name=name,
            muscle_group=muscle_group,
            description=request.form.get("description", "").strip(),
        ))
        db.session.commit()
        flash("Exercício cadastrado.", "success")
    return redirect(url_for("exercises_page"))


@app.post("/exercises/<int:exercise_id>/delete")
@trainer_required
def delete_exercise(exercise_id):
    exercise = Exercise.query.filter_by(id=exercise_id, trainer_id=signed_in_user().id).first_or_404()
    if WorkoutItem.query.filter_by(exercise_id=exercise.id).first():
        flash("Este exercício está em uso em um treino e não pode ser removido.", "error")
    else:
        db.session.delete(exercise)
        db.session.commit()
        flash("Exercício removido.", "success")
    return redirect(url_for("exercises_page"))


@app.post("/workouts")
@trainer_required
def add_workout():
    return save_workout()


@app.route("/workouts/<int:workout_id>/edit", methods=["GET", "POST"])
@trainer_required
def edit_workout(workout_id):
    workout = Workout.query.filter_by(
        id=workout_id, trainer_id=signed_in_user().id
    ).first_or_404()
    if request.method == "POST":
        return save_workout(workout)
    context = trainer_dashboard_data(signed_in_user(), "workouts")
    context["editing_workout"] = workout
    return render_template("index.html", **context)


def save_workout(workout=None):
    trainer = signed_in_user()
    is_edit = workout is not None
    student = User.query.filter_by(
        id=request.form.get("student_id", type=int), trainer_id=trainer.id, role="student"
    ).first()
    title = request.form.get("title", "").strip()
    exercise_ids = request.form.getlist("exercise_id[]")
    if not student or not title or not exercise_ids:
        flash("Informe aluno, nome do treino e pelo menos um exercício.", "error")
        destination = url_for("edit_workout", workout_id=workout.id) if workout else url_for("workouts_page")
        return redirect(destination + "#treinos")

    exercises = {
        exercise.id: exercise
        for exercise in Exercise.query.filter_by(trainer_id=trainer.id).all()
    }
    selected = []
    for index, raw_id in enumerate(exercise_ids):
        exercise = exercises.get(int(raw_id)) if raw_id.isdigit() else None
        if not exercise:
            continue
        selected.append(WorkoutItem(
            exercise=exercise,
            sets=max(1, request.form.getlist("sets[]")[index] and int(request.form.getlist("sets[]")[index]) or 3),
            reps=request.form.getlist("reps[]")[index].strip() or "12",
            load=request.form.getlist("load[]")[index].strip(),
            rest=request.form.getlist("rest[]")[index].strip(),
        ))
    if not selected:
        flash("Selecione ao menos um exercício cadastrado por você.", "error")
        destination = url_for("edit_workout", workout_id=workout.id) if workout else url_for("workouts_page")
        return redirect(destination + "#treinos")

    if workout:
        workout.student = student
        workout.title = title
        workout.notes = request.form.get("notes", "").strip()
        workout.items = selected
    else:
        workout = Workout(
            trainer_id=trainer.id,
            student_id=student.id,
            title=title,
            notes=request.form.get("notes", "").strip(),
            items=selected,
        )
    db.session.add(workout)
    db.session.commit()
    flash("Treino atualizado." if is_edit else "Treino criado e disponibilizado para o aluno.", "success")
    return redirect(url_for("workouts_page"))


@app.post("/workouts/<int:workout_id>/delete")
@trainer_required
def delete_workout(workout_id):
    workout = Workout.query.filter_by(id=workout_id, trainer_id=signed_in_user().id).first_or_404()
    db.session.delete(workout)
    db.session.commit()
    flash("Treino removido.", "success")
    return redirect(url_for("workouts_page"))


with app.app_context():
    db.create_all()
    if not User.query.filter_by(email="personal@gymmanager.local").first():
        trainer = User(
            name="Marina Costa",
            email="personal@gymmanager.local",
            password_hash=generate_password_hash("treino123"),
            role="trainer",
        )
        db.session.add(trainer)
        db.session.flush()
        student = User(
            name="Ana Souza",
            email="ana@gymmanager.local",
            password_hash=generate_password_hash("treino123"),
            role="student",
            trainer_id=trainer.id,
        )
        exercise = Exercise(
            trainer_id=trainer.id,
            name="Agachamento livre",
            muscle_group="Pernas",
            description="Desça mantendo o tronco firme e os joelhos alinhados.",
        )
        db.session.add_all([student, exercise])
        db.session.flush()
        workout = Workout(
            trainer_id=trainer.id,
            student_id=student.id,
            title="Força · Treino A",
            notes="Priorize a amplitude e mantenha o controle do movimento.",
        )
        workout.items.append(WorkoutItem(exercise=exercise, sets=4, reps="10", load="40 kg", rest="90 s"))
        db.session.add(workout)
        db.session.commit()


if __name__ == "__main__":
    app.run(debug=os.environ.get("FLASK_DEBUG") == "1")