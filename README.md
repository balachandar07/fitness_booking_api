# fitness_booking_api
A simple booking API for a fictional fitness studio, built using **Python (Flask)** and **SQLite (in-memory)**. This API allows users to:

- View available fitness classes
- Book a class
- View bookings by email

# Features

- View upcoming fitness classes with date, time (in IST), instructor, and available slots
- Book a class if slots are available
- Retrieve all bookings made by an email address
- Timezone-aware (IST ↔ UTC)
- Input validation and error handling
- In-memory SQLite DB (no external DB setup)
- Seed data included
- Unit tests for core endpoints

---

# Getting Started

# Requirements

- Python 3.8+
- `pip` or `virtualenv`

1. **Clone the repo**
git clone  https://github.com/balachandar07/fitness_booking_api.git
git switch  booking_api