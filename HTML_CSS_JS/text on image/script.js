const image = document.getElementById('image');
const overlay = document.getElementById('overlay');
const overlayText = document.getElementById('overlay-text');

image.addEventListener('mouseenter', () => {
    overlay.style.opacity = '1';
    overlay.style.pointerEvents = 'auto';
    overlayText.style.display = 'block';
});

image.addEventListener('mouseleave', () => {
    overlay.style.opacity = '0';
    overlay.style.pointerEvents = 'none';
    overlayText.style.display = 'none';
});

