const studentDialog = document.querySelector('#student-form');
document.querySelectorAll('[data-open="student-form"]').forEach((button) => {
  button.addEventListener('click', () => studentDialog.showModal());
});
document.querySelectorAll('[data-close]').forEach((button) => {
  button.addEventListener('click', () => studentDialog.close());
});
studentDialog?.addEventListener('click', (event) => {
  if (event.target === studentDialog) studentDialog.close();
});

const exerciseBuilder = document.querySelector('[data-exercise-builder]');
document.querySelector('[data-add-exercise]')?.addEventListener('click', () => {
  const entry = exerciseBuilder.querySelector('.exercise-entry');
  const clone = entry.cloneNode(true);
  clone.querySelector('select').value = '';
  clone.querySelectorAll('input').forEach((input) => {
    input.value = input.name === 'sets[]' ? '3' : input.name === 'reps[]' ? '12' : '';
  });
  exerciseBuilder.append(clone);
});