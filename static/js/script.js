console.log("TaskFlow loaded!");

document.addEventListener('DOMContentLoaded', function () {
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', function (e) {
            const requiredInputs = form.querySelectorAll('[required]');
            requiredInputs.forEach(input => {
                if (!input.value) {
                    e.preventDefault();
                    alert(`${input.name} is required!`);
                }
            });
        });
    });
});
