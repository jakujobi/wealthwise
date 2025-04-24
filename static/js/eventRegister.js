document.addEventListener('DOMContentLoaded', function () {
    const buttons = document.querySelectorAll('.register-btn');
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    buttons.forEach(button => {
        button.addEventListener('click', function () {
            const eventId = this.getAttribute('data-event-id');

            // Add a timestamp to the URL to prevent caching
            const url = `/schedule/registerEvent/${eventId}/?t=${new Date().getTime()}`;

            fetch(url, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrfToken
                },
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    alert(data.message);
                    // Reload the page to ensure data is up to date
                    window.location.reload(true);
                } else {
                    alert(`Failed: ${data.message}`);
                }
            })
            .catch(error => {
                console.error('Error:', error);
                alert('An error occurred. Please try again.');
            });
        });
    });
});
