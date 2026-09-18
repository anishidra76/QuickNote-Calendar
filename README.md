# Quick Note


    =>  Quick Note is a lightweight and user-friendly note management web application built with Django.

    =>  It allows users to create, organize, edit, and delete personal notes while scheduling them on specific dates through an integrated calendar interface. The goal is to provide a simple way to manage notes and keep track of important tasks and information.






# Features


    =>  User Authentication:

        --> User registration
        --> Login and logout
        --> Personal notes for each user


    =>  Note Management:

        --> Create notes
        --> Edit existing notes
        --> Delete notes
        --> View note details
        --> Assign an execution date to each note


    =>  Calendar Integration:

        --> View notes according to their execution dates
        --> Quickly identify scheduled notes directly from the calendar
        --> Visual indication for notes associated with a date


    =>  Personalized Data:

        --> Each user has their own notes
        --> Users cannot access other users' private notes


    =>  Clean Interface:

        --> Simple and intuitive design
        --> Responsive layout
        --> Focused on quick access and productivity






# Technologies


    =>  Backend:

        --> Python
        --> Django
        --> Django Authentication
        --> SQLite


    =>  Frontend:

        --> HTML5
        --> CSS3
        --> JavaScript


    =>  Project Structure:

        QuickNote/
        │
        ├── manage.py
        │
        ├── project/
        │   ├── settings.py
        │   ├── urls.py
        │   ├── wsgi.py
        │   └── ...
        │
        ├── app/
        │   ├── models.py
        │   ├── views.py
        │   ├── forms.py
        │   ├── urls.py
        │   ├── templates/
        │   └── static/
        │
        ├── db.sqlite3
        └── requirements.txt






# Getting Started


    =>  Clone the repository:

        --> git clone: https://github.com/anishidra76/QuickNote-Calendar.git


    =>  Move into the project directory:

        --> cd quick-note


    =>  Create a virtual environment:

        --> python -m venv .venv


    =>  Activate it on Linux/macOS:

        --> source .venv/bin/activate


    =>  On Windows:

        --> .venv\Scripts\activate


    =>  Install dependencies:

        --> pip install -r requirements.txt


    =>  Apply migrations:

        --> python manage.py migrate


    =>  Create a superuser:

        --> python manage.py createsuperuser


    =>  Run the development server:

        --> python manage.py runserver

        note: The application will be available at: http://127.0.0.1:8000/






# Authentication


    =>  Quick Note uses Django's built-in authentication system.


    =>  Users can:

        --> Create an account.
        --> Log in securely.
        --> Manage their personal notes.
        --> Log out when finished.
        --> Notes are associated with their respective users, keeping personal information separated between accounts.






# Security


    =>  The application relies on Django's built-in security features, including:

        --> User authentication
        --> CSRF protection
        --> Password hashing
        --> Session management
        --> User-specific data access






# Development


    =>  To start the project locally:

        --> python manage.py runserver


    =>  After making changes to models:

        --> python manage.py makemigrations
        --> python manage.py migrate


    =>  To create a new administrator:

        --> python manage.py createsuperuser






# Purpose


    =>  Quick Note was created as a practical project to explore and apply concepts such as:

        --> Django application development
        --> CRUD operations
        --> User authentication
        --> Database relationships
        --> Django forms
        --> Template rendering
        --> Frontend and backend integration
        --> Calendar-based data visualization
        --> Secure web application development






# Author


    =>  Anis Hidra

    =>  Full-Stack Web Developer

    =>  Portfolio   -->   https://anishidra.com/
    =>  GitHub      -->   https://github.com/anishidra76/
    =>  LinkedIn    -->   https://www.linkedin.com/in/anishidra76/






# License


    =>  This project is available for educational and personal use.