# HRMS Flask App

This project simulates a Basic HRMS (Human Resource Management System) with functionalities such as employee management, attendance tracking, and basic reporting.

## Project Overview

### Tasks

1. **Set up the Flask App:**
    - Initialize a Flask application.
    - Create necessary directories and files (templates, static, app.py, etc.).
    - Implement a basic route for the home page ("/") with a welcome message.

2. **Employee Management:**
    - Create a database model for employees with attributes like name, designation, department, date of joining, etc.
    - Create an API endpoint to add a new employee with basic information (name, address, email, etc.).
    - Create an API endpoint to retrieve the list of all employees.
    - Implement a route to display the list of employees on the home page.

3. **Attendance Tracking:**
    - Add fields for attendance in the employee model.
    - Create an API endpoint to mark attendance for a specific employee on a given date (In time/Out Time).
    - Create an API endpoint to retrieve attendance details for a specific employee.
    - Display attendance details on the employee details page.

4. **Basic Reporting:**
    - Implement a route to show a simple report that displays the count of employees in each department.
    - Use charts or tables to present the report.

5. **Documentation:**
    - Include docstrings for all functions and classes.
    - Write a brief README.md file explaining the project structure, how to run the app locally, and any additional information.

## Project Structure


## How to Run Locally

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/udayakumar21/HRMS.git
   cd code

2. python app.py

3. Access the App:
Open your web browser and go to http://127.0.0.1:5000/
