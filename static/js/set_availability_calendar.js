document.addEventListener("DOMContentLoaded", function () {
    const addTimeSlotButtons = document.querySelectorAll(".add-time-slot");
    const saveTimeSlotButton = document.getElementById("save-time-slot");
    const saveAvailabilityButton = document.getElementById("save-availability");
    const modalDayInput = document.getElementById("modal-day");
    const modalStartTimeInput = document.getElementById("modal-start-time");
    const modalEndTimeInput = document.getElementById("modal-end-time");
    const timeSlots = { add: {}, remove: {} }; // Initialize add and remove properties

    // Helper function to convert 24-hour time to 12-hour format
    function formatTo12Hour(time) {
        const [hour, minute] = time.split(":");
        const period = hour >= 12 ? "PM" : "AM";
        const formattedHour = hour % 12 || 12;
        return `${formattedHour}:${minute} ${period}`;
    }

    // Helper function to convert 12-hour time to 24-hour format
    function formatTo24Hour(time) {
        const [timePart, period] = time.split(" ");
        let [hour, minute] = timePart.split(":").map(Number);
        if (period === "PM" && hour !== 12) hour += 12;
        if (period === "AM" && hour === 12) hour = 0;
        return `${hour.toString().padStart(2, "0")}:${minute.toString().padStart(2, "0")}`;
    }

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
        const startTime = modalStartTimeInput.value; // Already in 24-hour format from <input type="time">
        const endTime = modalEndTimeInput.value; // Already in 24-hour format from <input type="time">

        if (!startTime || !endTime) {
            alert("Please specify both start and end times.");
            return;
        }

        if (!timeSlots.add[day]) {
            timeSlots.add[day] = [];
        }
        timeSlots.add[day].push({ start_time: startTime, end_time: endTime });

        const timeSlotsCell = document.getElementById(`time-slots-${day}`);
        const slotElement = document.createElement("div");
        slotElement.textContent = `${formatTo12Hour(startTime)} - ${formatTo12Hour(endTime)}`;
        slotElement.innerHTML += `
            <button class="btn btn-danger btn-sm remove-time-slot" 
                    data-day="${day}" 
                    data-start-time="${startTime}" 
                    data-end-time="${endTime}">
                Remove
            </button>`;
        timeSlotsCell.appendChild(slotElement);

        // Reattach event listener for dynamically added remove buttons
        slotElement.querySelector(".remove-time-slot").addEventListener("click", function () {
            const day = this.dataset.day;
            const startTime = this.dataset.startTime;
            const endTime = this.dataset.endTime;

            if (!timeSlots.remove[day]) {
                timeSlots.remove[day] = [];
            }
            timeSlots.remove[day].push({ start_time: startTime, end_time: endTime });

            // Remove the time slot from the UI
            this.parentElement.remove();
        });

        const modal = bootstrap.Modal.getInstance(document.getElementById("addTimeSlotModal"));
        modal.hide();
    });

    const removeTimeSlotButtons = document.querySelectorAll(".remove-time-slot");

    // Remove time slot from the table and prepare for server update
    removeTimeSlotButtons.forEach(button => {
        button.addEventListener("click", function () {
            const day = this.dataset.day;
            const startTime = formatTo24Hour(this.dataset.startTime);
            const endTime = formatTo24Hour(this.dataset.endTime);

            if (!timeSlots.remove[day]) {
                timeSlots.remove[day] = [];
            }
            timeSlots.remove[day].push({ start_time: startTime, end_time: endTime });

            // Remove the time slot from the UI
            this.parentElement.remove();
        });
    });

    // Save all availability to the server
    saveAvailabilityButton.addEventListener("click", function () {
        fetch("/schedule/setAvailability/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": document.querySelector("[name=csrfmiddlewaretoken]").value
            },
            body: JSON.stringify({ time_slots: timeSlots.add, remove_time_slots: timeSlots.remove })
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
