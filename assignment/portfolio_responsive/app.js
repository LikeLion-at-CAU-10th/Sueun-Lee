let darkMode = localStorage.getItem('darkMode');
const checkbox = document.querySelector('#checkbox');

const enableDarkMode = () => {
  document.body.classList.add('dark');
  localStorage.setItem('darkMode', 'enabled');
};

const disableDarkMode = () => {
  document.body.classList.remove('dark');
  localStorage.setItem('darkMode', null);
};

if (darkMode === 'enabled') enableDarkMode();

checkbox.addEventListener('click', () => {
  darkMode = localStorage.getItem('darkMode');
  if (darkMode !== 'enabled') {
    enableDarkMode();
  } else {
    disableDarkMode();
  }
});