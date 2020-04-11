const toggleButton = document.getElementsByClassName('toggle-button')[0]
const navbarLinks = document.getElementsByClassName('navbar-links')[0]

toggleButton.addEventListener('click', () => {
    navbarLinks.classList.toggle('active');
});

document.querySelector('.tour-button').onclick = function() {
    document.querySelector('.tour-title').innerHTML = "Big Tournament<br>Coming Soon";
};