# Cafe House – Django Project

## Overview

A Django-powered café website where visitors can browse categories and menu items, and users can register, log in, log out, and reset their password. The UI uses Bootstrap and Font Awesome with a modular base template (base) and shared includes (head, header, footer, scripts).

## Table of Contents

Features

Tech Stack

Installation

Project Structure

Configuration

Main URLs

Admin

Sample Data

Requirements

Contributing

License

Contact

## Features

Home Page: Featured sections (popular items, today’s specials).

Menu Page: Category-based listing (cold drinks, hot drinks, coffee-based, foods).

Contact Page: Simple contact form with validation.

Accounts:

Registration / Login / Logout

Full Password Reset (request → verify/code → set new password → complete)

Dynamic Header: Shows Logout (username) when authenticated, otherwise Login / Register.

Responsive UI: Bootstrap grid + custom CSS, preloader, smooth scrolling.

## Tech Stack

Backend: Django (Python 3.10+)

Frontend: HTML5, CSS3, Bootstrap 3, Font Awesome, jQuery

Database: SQLite (default; can switch to PostgreSQL/MySQL)

Auth: Django built-in auth with customized templates

## Installation
Prerequisites

Python 3.10+

Django 5.x (or your pinned version)

pip

SQLite (default) or another RDBMS

### Steps

1. Clone
  ```bash
  git clone https://github.com/
  ```
2. Virtualenv
  ```bash
  python -m venv venv
  # macOS/Linux
  source venv/bin/activate
  # Windows
  venv\Scripts\activate
  ```
3. Install deps
  ```bash
  pip install -r requirements.txt
  ```
4. Migrate & create superuser
  ```bash
  python manage.py migrate
  python manage.py createsuperuser
  ```
5. Run
  ```bash
  python manage.py runserver
  ```
6. Open
  ```bash
  App: http://127.0.0.1:8000
  Admin: http://127.0.0.1:8000/admin
  ```

## Project Structure
```
    yasinaliyari-cafe-house/
    ├── manage.py
    ├── account/
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── forms.py
    │   ├── models.py
    │   ├── tests.py
    │   ├── urls.py
    │   ├── views.py
    │   ├── migrations/
    │   │   └── __init__.py
    │   └── templates/
    │       └── account/
    │           ├── login.html
    │           ├── password_reset_complete.html
    │           ├── password_reset_confirm_custom.html
    │           ├── password_reset_request.html
    │           ├── password_reset_show_code.html
    │           ├── password_reset_verify.html
    │           └── register.html
    ├── cafe/
    │   ├── __init__.py
    │   ├── asgi.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    ├── contact/
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── forms.py
    │   ├── models.py
    │   ├── tests.py
    │   ├── urls.py
    │   ├── views.py
    │   ├── migrations/
    │   │   └── __init__.py
    │   └── templates/
    │       └── contact/
    │           └── contact.html
    ├── home/
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── forms.py
    │   ├── models.py
    │   ├── tests.py
    │   ├── urls.py
    │   ├── views.py
    │   ├── migrations/
    │   │   └── __init__.py
    │   └── templates/
    │       └── home/
    │           └── home.html
    ├── menu/
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── forms.py
    │   ├── models.py
    │   ├── tests.py
    │   ├── urls.py
    │   ├── views.py
    │   ├── migrations/
    │   │   └── __init__.py
    │   └── templates/
    │       └── menu/
    │           └── menu.html
    ├── static/
    │   ├── css/
    │   │   └── templatemo-style.css
    │   └── js/
    │       └── templatemo-script.js
    └── templates/
        ├── base.html
        └── includes/
            ├── footer.html
            ├── head.html
            ├── header.html
            └── script.html
```

## Configuration

Static/Media: Set STATIC_URL, STATICFILES_DIRS, MEDIA_URL, MEDIA_ROOT in settings.py.

Email (Password Reset): Configure an SMTP backend (e.g., Gmail/SendGrid) and set env vars (EMAIL_HOST, EMAIL_PORT, EMAIL_HOST_USER, EMAIL_HOST_PASSWORD, EMAIL_USE_TLS/SSL) for production.

Secret Key & Debug: Use environment variables (e.g., .env) to manage SECRET_KEY, DEBUG, DB credentials, etc.

## Main URLs

/ — Home

/menu/ — Menu

/contact/ — Contact

/accounts/register/, /accounts/login/, /accounts/logout/

/accounts/password-reset/ — Password reset flow

## Admin

Visit /admin/ with the superuser created earlier.

Manage home sections and menu items; toggle visibility using boolean flags.

## Sample Data

Add a few popular/special items for Home and several Menu items across categories.

Mark them active to render on the site.

## Contributing

Fork the repo.

Create a feature branch: git checkout -b feature/awesome

Commit with clear messages.

Open a PR with screenshots/GIFs for UI changes.

## License

Educational/demo project using public front-end assets (Bootstrap, Font Awesome, jQuery). Each asset retains its original license.

## Contact

Questions or support? Your Name — yasinaliyari30@gmail.com
