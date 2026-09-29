# GymManager

Aplicação web para personal trainers organizarem alunos, exercícios e treinos. Os alunos acessam seus próprios treinos e as orientações de cada exercício.

## Executar localmente

Requer Python 3.10 ou superior.

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Abra http://127.0.0.1:5000. O banco SQLite é criado automaticamente em `instance/gymmanager.db` com dados de demonstração.

| Perfil | E-mail | Senha |
| --- | --- | --- |
| Personal | `personal@gymmanager.local` | `treino123` |
| Aluno | `ana@gymmanager.local` | `treino123` |

## Funcionalidades

- Login e acesso separado por perfil;
- Cadastro e remoção de alunos;
- Cadastro e remoção de exercícios;
- Busca de alunos, exercícios e treinos, com filtro de exercícios por grupo muscular e de treinos por aluno;
- Criação e edição de treinos com vários exercícios, séries, repetições, carga e intervalo;
- Consulta dos treinos pelo aluno;
- Registro da conclusão do treino pelo aluno, com data visível para ele e para o personal;
- Remoção de treinos.

## Banco de dados

Por padrão, a aplicação usa SQLite para facilitar a execução local. Para usar MySQL, configure `DATABASE_URL` com uma URL SQLAlchemy, por exemplo `mysql+pymysql://usuario:senha@localhost/gymmanager`. Também defina `SECRET_KEY` com um valor aleatório antes de disponibilizar a aplicação fora do ambiente local. As credenciais demonstrativas e a chave padrão são somente para desenvolvimento.

## Estrutura

- `app.py` — aplicação Flask e modelos de dados;
- `templates/` — interface HTML;
- `static/` — estilos e interações da interface;
- `docs/` — documentação do projeto;
- `prototipos/` — protótipos das telas.

