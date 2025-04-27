document.querySelectorAll('.cancel-consultation-btn').forEach(button => {
    button.addEventListener('click', function () {
        const consultationId = this.dataset.consultationId;
        const sessionNotes = prompt("Please provide a reason or notes for cancelling this consultation (optional):");

        if (confirm("Are you sure you want to cancel this consultation?")) {
            fetch(`/schedule/cancelConsultation/${consultationId}/`, {
                method: 'POST',
                headers: {
                    'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value,
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ consultation_id: consultationId, session_notes: sessionNotes }),
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    location.reload();
                }
            })
            .catch(error => {
                console.error('Error:', error);
            });
        }
    });
});
