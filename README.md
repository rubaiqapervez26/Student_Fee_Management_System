# Smart Fee Management System

A responsive university student fee tracking web application engineered using the Django MVC/MVT framework. This system provides institutional administrators with a centralized dashboard to track and manage student financial records seamlessly.

This application was developed as an Open-Ended Lab (OEL) for the Web Engineering Course (CYS-463) at the University of Wah, Department of Computer Science.

---

## Key Features

* **Complete CRUD Operations:** Secure system architecture allowing administrators to Create, Read, Update, and Delete individual student fee logs.
* **Instant Status Updates:** A dynamic action mechanism enabling administrators to toggle a student's status between Paid and Unpaid instantly from the dashboard.
* **Live Search Index:** An optimized look-up filter on the main interface to query records by student name or roll number.
* **Front-End Validation:** Integrated client-side JavaScript guardrails to prevent empty submissions or erroneous negative fee values.
* **Responsive Layout:** Designed with a fluid grid system using Bootstrap to ensure full cross-device compatibility (mobile, tablet, and desktop).

---

## Tech Stack

* **Backend Engine:** Python & Django Web Framework
* **Frontend Design:** HTML5, CSS3, and Bootstrap 5
* **Client Scripts:** Vanilla JavaScript (ES6+)
* **Database Wrapper:** SQLite 3

---

## Project Structure & Architecture

The application follows Django's modular development architecture, segmented into distinct technical layers:

1. **Data Layer (`models.py`):** Defines the database structure for record properties, automated timestamps, field constraint rules, and semester categorizations.
2. **Validation Layer (`forms.py`):** Automatically maps backend structural models to front-end forms while injecting Bootstrap styling natively.
3. **Logic Controller (`views.py`):** Manages backend operations, processing request methods, parsing query lookups, and updating the database state.
4. **Routing Grid (`urls.py`):** Configures application navigation, binding web endpoints directly to corresponding view functions.

---

## Installation & Environment Setup

Follow these terminal steps to configure and run a local instance of the application:

1. **Clone the Repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/smart-fee-management.git](https://github.com/YOUR_USERNAME/smart-fee-management.git)
   cd smart-fee-management
