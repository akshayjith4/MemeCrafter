document.addEventListener('DOMContentLoaded', () => {
    const form = document.querySelector('form');
    const topicInput = document.querySelector('input[name="topic"]');
    const image = document.querySelector('img');

    // Fade-in effect for the meme image
    if (image) {
        image.style.opacity = 0;
        image.onload = () => {
            image.style.transition = 'opacity 0.6s ease-in-out';
            image.style.opacity = 1;
        };
    }

    // Button hover animation: edgy glow
    document.querySelectorAll('button').forEach(button => {
        button.addEventListener('mouseenter', () => {
            button.style.transform = 'scale(1.05)';
            button.style.boxShadow = '0 0 12px #00b7ff';
        });
        button.addEventListener('mouseleave', () => {
            button.style.transform = 'scale(1)';
            button.style.boxShadow = 'none';
        });
    });

    // Submit on Enter from topic input
    if (topicInput) {
        topicInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') {
                e.preventDefault();
                form.submit();
            }
        });
    }

    // Highlight selected caption radio label
    document.querySelectorAll('input[type="radio"]').forEach(radio => {
        radio.addEventListener('change', () => {
            document.querySelectorAll('label').forEach(label => {
                label.classList.remove('selected-caption');
            });
            if (radio.closest('label')) {
                radio.closest('label').classList.add('selected-caption');
            }
        });
    });
});
