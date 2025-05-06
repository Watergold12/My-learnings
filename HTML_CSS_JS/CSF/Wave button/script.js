document.getElementById('waveBtn').addEventListener('click', function(e) {
  const wave = document.createElement('span');
  wave.className = 'button-wave';
  const rect = this.getBoundingClientRect();
  const x = e.clientX - rect.left;
  const y = e.clientY - rect.top;
  wave.style.left = `${x}px`;
  wave.style.top = `${y}px`;
  this.appendChild(wave);
  setTimeout(() => {
    wave.remove();
  }, 400);
});
