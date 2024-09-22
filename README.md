project added
Project Overview
Name: Hospital Management System
Technology Stack: Java, MySQL, JDBC, Scanner (for user input)
Purpose: To manage patients, doctors, appointments, and provide a user-friendly interface for hospital staff to streamline operations.

Key Features.....................
User Roles:

Doctors: Can view their details, check appointment history, and manage their schedules.
Patients: Can be added, viewed, and deleted, with appointments booked against them.
Database Management:

MySQL is used to manage the database with tables for patients, doctors, and appointments.
Foreign key constraints ensure data integrity (e.g., appointments reference existing patients and doctors).
CRUD Operations:

Create: Adding new patients and doctors through the system.
Read: Viewing lists of patients and doctors, along with their details.
Update: Updating patient and doctor information as needed (not directly shown but can be implemented).
Delete: Removing patients from the system, ensuring constraints are respected.
Appointment Management:

Users can book appointments by checking the availability of doctors on specific dates.
Appointment history can be viewed for each doctor, showing past patients and times.
Technical Implementation
Database Schema:

Patients Table: Contains fields like patient_id, first_name, last_name, etc.
Doctors Table: Similar structure with additional fields for specialty and experience.
Appointments Table: Links patients to doctors and includes date and time of the appointment.
JDBC Connection:

A connection to the MySQL database is established using JDBC.
Prepared statements are used for executing SQL queries safely, preventing SQL injection.
Menu-Driven Interface:

