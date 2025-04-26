document.addEventListener("DOMContentLoaded", function () {
    const addTimeSlotButtons = document.querySelectorAll(".add-time-slot");
    const saveTimeSlotButton = document.getElementById("save-time-slot");
    const saveAvailabilityButton = document.getElementById("save-availability");
    const modalDayInput = document.getElementById("modal-day");
    const modalStartTimeInput = document.getElementById("modal-start-time");
    const modalEndTimeInput = document.getElementById("modal-end-time");
    const timeSlots = {};

    // Open modal to add a time slot
    addTimeSlotButtons.forEach(button => {
        button.addEventListener("click", function () {
            const day = this.dataset.day;
            modalDayInput.value = day;
            modalStartTimeInput.value = "";
            modalEndTimeInput.value = "";
            const modal = new bootstrap.Modal(document.getElementById("addTimeSlotModal"));
            modal.show();
        });
    });

    // Save time slot to the table
    saveTimeSlotButton.addEventListener("click", function () {
        const day = modalDayInput.value;
        const startTime = modalStartTimeInput.value;
        const endTime = modalEndTimeInput.value;

        if (!startTime || !endTime) {
            alert("Please specify both start and end times.");
            return;
        }

        if (!timeSlots[day]) {
            timeSlots[day] = [];
        }
        timeSlots[day].push({ start_time: startTime, end_time: endTime });

        const timeSlotsCell = document.getElementById(`time-slots-${day}`);
        const slotElement = document.createElement("div");
        slotElement.textContent = `${startTime} - ${endTime}`;
        timeSlotsCell.appendChild(slotElement);

        const modal = bootstrap.Modal.getInstance(document.getElementById("addTimeSlotModal"));
        modal.hide();
    });

    // Save all availability to the server
    saveAvailabilityButton.addEventListener("click", function () {
        fetch("/schedule/setAvailability/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": document.querySelector("[name=csrfmiddlewaretoken]").value
            },
            body: JSON.stringify({ time_slots: timeSlots })
        })
            .then(response => {
                if (response.ok) {
                    return response.json();
                } else {
                    return response.json().then(data => {
                        alert(data.error_message || "An error occurred while saving availability.");
                        throw new Error("Failed to save availability.");
                    });
                }
            })
            .then(data => {
                if (data.redirect_url) {
                    window.location.href = data.redirect_url; // Redirect to the URL provided by the backend
                }
            })
            .catch(error => {
                console.error("Error:", error);
                alert("An error occurred while saving availability.");
            });
    });
});
