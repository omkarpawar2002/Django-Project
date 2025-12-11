# Student Management System (Django)

A simple Student Management System built using Django, SQLite, and Django’s built-in authentication.  
It allows users to add, update, delete, and view student records.

---

## Features
- User authentication (login/logout)
- Add new students
- Update student details
- Delete students
- View all students
- Uses SQLite (default Django DB)

---

## Tech Stack
- Python
- Django
- SQLite
- HTML / Bootstrap

---

## How to Run

```bash
# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Create admin user
python manage.py createsuperuser

# Run the server
python manage.py runserver
```