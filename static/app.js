const button = document.querySelector('.button')
const sidebar = document.querySelector('.sidebar')

button.addEventListener('click', () => {
    sidebar.classList.toggle('-translate-x-full')
})