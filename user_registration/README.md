# Django Project

Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design.This project focuses on registering user's using django-registration.

## Installation
1 Create a Python 3.6 virtualenv

2 Install dependencies:

```bash
pip install -r requirements.txt 
```

## Project structure

```
.
├── manage.py
├── payment
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations
│   │   ├── __init__.py
│   │   └── __pycache__
│   │       └── __init__.cpython-36.pyc
│   ├── models.py
│   ├── __pycache__
│   │   ├── admin.cpython-36.pyc
│   │   ├── __init__.cpython-36.pyc
│   │   └── models.cpython-36.pyc
│   ├── tests.py
│   └── views.py
├── README.md
├── registration
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations
│   │   ├── __init__.py
│   │   └── __pycache__
│   │       └── __init__.cpython-36.pyc
│   ├── models.py
│   ├── __pycache__
│   │   ├── admin.cpython-36.pyc
│   │   ├── forms.cpython-36.pyc
│   │   ├── __init__.cpython-36.pyc
│   │   ├── models.cpython-36.pyc
│   │   ├── urls.cpython-36.pyc
│   │   └── views.cpython-36.pyc
│   ├── templates
│   │   ├── django_registration
│   │   │   ├── registration_complete.html
│   │   │   └── registration_form.html
│   │   ├── login
│   │   │   ├── homepage.html
│   │   │   └── login_page.html
│   │   ├── logout
│   │   │   └── logout_page.html
│   │   └── registration
│   │       └── login.html
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── requirements.txt
├── templates
│   └── user_registration
│       └── base.html
└── user_registration
    ├── __init__.py
    ├── __pycache__
    │   ├── __init__.cpython-36.pyc
    │   ├── settings.cpython-36.pyc
    │   ├── urls.cpython-36.pyc
    │   └── wsgi.cpython-36.pyc
    ├── settings.py
    ├── urls.py
    └── wsgi.py


```
## Files  
 1. manage.py: Used to run Command line commands.  
2. settings.py: Here we set our configurations  
3. urls.py: It contains url dispatchers.  
4. views.py: This file contains the business logic required.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
