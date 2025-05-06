document.addEventListener('DOMContentLoaded', function() {
    window.addEventListener('scroll', revealTextOnScroll);
});

function revealTextOnScroll() {
    const revealText = document.getElementById('revealText');
    const revealPosition = revealText.getBoundingClientRect().top;
    const windowHeight = window.innerHeight / 1.5; // Adjust visibility threshold

    if (revealPosition < windowHeight) {
        revealText.style.opacity = 1;
    }
}
