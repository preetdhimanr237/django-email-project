# Email Project

A simple Django web application where users can register an account and automatically receive a welcome email after successful registration.

## Features

- User Registration
- Custom Registration Page
- Username, Email, First Name and Last Name
- Password and Confirm Password
- Django Built-in User Model
- SQLite Database
- Automatic Welcome Email
- Gmail SMTP Integration
- Django Admin Panel
- Simple HTML and CSS UI

## Technologies Used

- Python
- Django
- HTML
- CSS
- SQLite
- Gmail SMTP

## How It Works

User opens the Registration Page
        ↓
User fills the Registration Form
        ↓
Django validates the form
        ↓
User account is created
        ↓
Welcome Email is sent
        ↓
User is redirected to Home Page

## Installation

### 1. Create Virtual Environment

python -m venv venv

### 2. Activate Virtual Environment

For Windows:

venv\Scripts\activate

### 3. Install Django

pip install django

### 4. Run Migrations

python manage.py migrate

### 5. Create Superuser

python manage.py createsuperuser

### 6. Start Server

python manage.py runserver

Open the project in browser:

http://127.0.0.1:8000/register/

## Email Configuration

The project uses Gmail SMTP to send welcome emails.

Django 6.1 uses the MAILERS configuration.

Example:

MAILERS = {
    'default': {
        'BACKEND': 'django.core.mail.backends.smtp.EmailBackend',
        'OPTIONS': {
            'host': 'smtp.gmail.com',
            'port': 587,
            'username': 'your-email@gmail.com',
            'password': 'your-app-password',
            'use_tls': True,
        },
    },
}

EMAIL_SENDER = 'your-email@gmail.com'

For Gmail, use a Google App Password instead of your normal Gmail password.

Never upload your real email password or App Password to GitHub.

## Django Admin

The Django Admin Panel can be opened at:

http://127.0.0.1:8000/admin/

Registered users can be viewed from:

Authentication and Authorization → Users

## Main Django Concepts Used

### UserCreationForm

Django's built-in UserCreationForm is used for user registration and password validation.

### User Model

The project uses Django's built-in User model instead of creating a custom user model.

### Django Forms

Django Forms are used to receive and validate user registration data.

### send_mail()

Django's send_mail() function is used to send the welcome email after successful registration.

## Future Improvements

- Custom Login Page
- Logout Functionality
- User Dashboard
- Email Verification
- Password Reset
- Better Responsive UI
- Environment Variables for Email Credentials
- PostgreSQL Database
- Deploy the Project Online

## Author

Preet Dhiman

BCA Student | Backend Web Development

Skills:
Python | Django | SQL | HTML | CSS