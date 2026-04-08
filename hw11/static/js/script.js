// Book Club Website JavaScript

document.addEventListener('DOMContentLoaded', function() {
    // Fade in the container
    const container = document.querySelector('.container');
    if (container) {
        container.style.opacity = '0';
        container.style.transform = 'translateY(20px)';
        container.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
        setTimeout(() => {
            container.style.opacity = '1';
            container.style.transform = 'translateY(0)';
        }, 100);
    }

    // Animate visit count
    const visitCountElement = document.querySelector('.visit-count');
    if (visitCountElement) {
        const count = parseInt(visitCountElement.textContent.match(/\d+/)[0]);
        animateCount(visitCountElement, count);
    }
});

function animateCount(element, target) {
    let current = 0;
    const increment = target / 50; // Adjust speed
    const timer = setInterval(() => {
        current += increment;
        if (current >= target) {
            current = target;
            clearInterval(timer);
        }
        element.innerHTML = element.innerHTML.replace(/\d+/, Math.floor(current));
    }, 30);
}