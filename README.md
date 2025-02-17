# Academy Backend

## Overview

The **Academy Backend** project provides a robust backend system for managing students, classes, and progression in a martial arts academy. This system includes features for managing students' personal information, tracking their progress, and handling completed lessons. The backend is designed to be integrated with a frontend system in the next phase of the project.

## First look:

<p align="center">
<img src="https://github.com/user-attachments/assets/7283d9b0-7f21-446a-b4ab-de5a2beb5154" alt="" width="700">
</p>


## Features

- **Student Management**: Allows for creating and updating student profiles.
- **Progress Tracking**: Enables tracking students' progress in their martial arts journey.
- **Lesson Completion**: Manages completed lessons, ensuring students' records are updated.
- **Graduation System**: Calculates the number of lessons required to promote students to the next belt level.

## Technologies Used

- **Django**: A high-level Python web framework used for creating and managing the backend system.
- **Ninja**: A fast web framework for building APIs with Pydantic and async support.
- **SQLite**: A lightweight, serverless database used for storing students' data and completed lessons.

## Installation

To run this project locally, follow the steps below:

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/academy-backend.git
   cd academy-backend
   ```

2. Create a virtual environment and activate it:

   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. Install the required dependencies:

   ```bash
   pip install django
   pip install pillow
   pip install django-ninja
   ```

4. Run the development server:

   ```bash
   python manage.py runserver
   ```

5. The API will be available at `http://127.0.0.1:8000`.

## API Endpoints

The backend exposes several endpoints for managing students and tracking progress.

### Student Endpoints

#### Create a Student

`POST /api/`

Create a new student profile by providing their name, email, belt, and birth date.

**Request Body Example:**

```json
{
    "name": "John Doe",
    "email": "john.doe@example.com",
    "belt": "Blue",
    "birth_date": "2000-01-01"
}
```

#### List All Students

`GET /api/students/`

Retrieve a list of all students.

#### Update a Student

`PUT /api/students/{student_id}`

Update an existing student's profile by ID.

**Request Body Example:**

```json
{
    "name": "John Doe Updated",
    "belt": "Purple",
    "birth_date": "2000-01-01"
}
```

#### Get Student Progress

`GET /api/student_progress/`

Get a student's progress by providing their email.

**Request Parameters:**

- `student_email`: The email address of the student.

#### Mark Completed Lesson

`POST /api/completed_lesson/`

Mark a lesson as completed for a student.

**Request Body Example:**

```json
{
    "qtd": 3,
    "email_student": "john.doe@example.com"
}
```

### Progress Calculation

The backend calculates the number of lessons required to promote a student to the next belt based on the student's current belt and the number of lessons they have completed.

- **Current Belts**: White (0), Blue (1), Purple (2), Brown (3), Black (4)
- **Lesson Calculation**: Each belt level has a corresponding lesson requirement, and the system tracks how many lessons remain to achieve the next belt.

## Future Integration

In the next phase of the project, this backend will be integrated with a frontend system, which will allow users to interact with the API via a user-friendly interface. The frontend will allow for managing students, tracking progress, and completing lessons more efficiently.

