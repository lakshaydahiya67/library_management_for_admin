document.addEventListener('DOMContentLoaded', () => {
    const slots = document.querySelectorAll('.slot div');

    // Add hover effect for slots
    slots.forEach(slot => {
        slot.addEventListener('mouseenter', () => {
            slot.style.filter = 'brightness(1.1)';
        });

        slot.addEventListener('mouseleave', () => {
            slot.style.filter = '';
        });
    });

    // Loading state (for demonstration purposes)
    const skeletons = document.querySelectorAll('.skeleton');
    setTimeout(() => {
        skeletons.forEach(skeleton => {
            skeleton.classList.remove('skeleton');
        });
    }, 1500);
});