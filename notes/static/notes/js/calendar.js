const calendar = document.getElementById("calendar");
const monthYear = document.getElementById("monthYear");
const previousMonth = document.getElementById("previousMonth");
const nextMonth = document.getElementById("nextMonth");
let currentDate = new Date();
const notes = document.querySelectorAll(".note-card");



function renderCalendar() {
    calendar.innerHTML = "";
    const year = currentDate.getFullYear();
    const month = currentDate.getMonth();
    const firstDay = new Date(
        year,
        month,
        1
    );
    const lastDay = new Date(
        year,
        month + 1,
        0
    );
    const monthName = currentDate.toLocaleString(
        "default",
        {
            month: "long"
        }
    );
    monthYear.textContent =
        `${monthName} ${year}`;
    let startDay = firstDay.getDay();

    // JavaScript: Sunday = 0
    // We want Monday = 0

    startDay = startDay === 0 ? 6 : startDay - 1;

    for (let i = 0; i < startDay; i++) {
        const emptyDay = document.createElement("div");
        emptyDay.classList.add("calendar-day", "empty");
        calendar.appendChild(emptyDay);
    }

    for (let day = 1; day <= lastDay.getDate(); day++
    ) {
        const dayElement = document.createElement("div");
        dayElement.classList.add("calendar-day");
        const dateString = `${year}-${String(month + 1).padStart(2, "0")}-${String(day).padStart(2, "0")}`;
        dayElement.dataset.date = dateString;
        const dayNumber = document.createElement("span");
        dayNumber.classList.add("day-number");
        dayNumber.textContent = day; dayElement.appendChild(dayNumber);
        const dayNotes =
            Array.from(notes).filter(note => note.dataset.date === dateString);
        dayNotes.forEach(note => {
            const noteIndicator = document.createElement("span");
            noteIndicator.classList.add("note-indicator");
            noteIndicator.textContent = note.dataset.title;
            dayElement.appendChild(noteIndicator);
        })

        // Today

        const today = new Date();

        if (day === today.getDate() && month === today.getMonth() && year === today.getFullYear()) {
            dayElement.classList.add(
                "today"
            );
        }

        calendar.appendChild(dayElement);
    }
}

previousMonth.addEventListener(
    "click",
    () => {
        currentDate.setMonth(
            currentDate.getMonth() - 1
        );
        renderCalendar();
    }
);

nextMonth.addEventListener(
    "click",
    () => {

        currentDate.setMonth(
            currentDate.getMonth() + 1
        );

        renderCalendar();
    }
);


renderCalendar();
