// 🗓️ Dynamic Year in Footer
document.getElementById('year').textContent = new Date().getFullYear();

// 🌌 Particle Background Animation
const canvas = document.getElementById('bg');
const ctx = canvas.getContext('2d');
let particles = [];

// Adjust canvas to screen size
function resize() {
  canvas.width = window.innerWidth;
  canvas.height = window.innerHeight;
}
window.addEventListener('resize', resize);
resize();

// Create particle objects (lightly reduced intensity)
for (let i = 0; i < 110; i++) {
  particles.push({
    x: Math.random() * canvas.width,
    y: Math.random() * canvas.height,
    // slightly smaller max size for a lighter feel
    size: Math.random() * 2.8 + 0.6,
    // moderate speed so motion feels lively but less intense
    speedX: (Math.random() - 0.5) * 1.6,
    speedY: (Math.random() - 0.5) * 1.6,
    // slightly lower opacity range
    opacity: Math.random() * 0.5 + 0.25
  });
}

// Animation loop
function animate() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  particles.forEach(p => {
    p.x += p.speedX;
    p.y += p.speedY;

    if (p.x < 0 || p.x > canvas.width) p.speedX *= -1;
    if (p.y < 0 || p.y > canvas.height) p.speedY *= -1;

    ctx.fillStyle = `rgba(255,255,255,${p.opacity})`;
    ctx.beginPath();
    ctx.arc(p.x, p.y, p.size, 0, Math.PI * 2);
    ctx.fill();
  });
  requestAnimationFrame(animate);
}
animate();
document.getElementById('year').textContent = new Date().getFullYear();

// 🌌 Particle Background Animation
const canvas = document.getElementById('bg');
const ctx = canvas.getContext('2d');
let particles = [];

// Adjust canvas to screen size
function resize() {
  canvas.width = window.innerWidth;
  canvas.height = window.innerHeight;
}
window.addEventListener('resize', resize);
resize();

// Create particle objects (lightly reduced intensity)
for (let i = 0; i < 110; i++) {
  particles.push({
    x: Math.random() * canvas.width,
    y: Math.random() * canvas.height,
    // slightly smaller max size for a lighter feel
    size: Math.random() * 2.8 + 0.6,
    // moderate speed so motion feels lively but less intense
    speedX: (Math.random() - 0.5) * 1.6,
    speedY: (Math.random() - 0.5) * 1.6,
    // slightly lower opacity range
    opacity: Math.random() * 0.5 + 0.25
  });
}

// Animation loop
function animate() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  particles.forEach(p => {
    p.x += p.speedX;
    p.y += p.speedY;

    if (p.x < 0 || p.x > canvas.width) p.speedX *= -1;
    if (p.y < 0 || p.y > canvas.height) p.speedY *= -1;

    ctx.fillStyle = `rgba(255,255,255,${p.opacity})`;
    ctx.beginPath();
    ctx.arc(p.x, p.y, p.size, 0, Math.PI * 2);
    ctx.fill();
  });
  requestAnimationFrame(animate);
}
animate();
