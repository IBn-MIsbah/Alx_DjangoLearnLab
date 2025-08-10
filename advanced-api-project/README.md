# Advanced API Project

This project is a Django REST Framework (DRF) based API for managing authors and books.  
It demonstrates the use of **generic views**, **permissions**, and **custom serializers** for handling nested relationships and data validation.

## Features

- Manage Authors and Books with a one-to-many relationship.
- CRUD API endpoints for Books using DRF's generic views.
- Nested serialization to include books inside author details.
- Custom validation for `publication_year` to prevent future dates.
- Permission handling:
  - Public read-only access.
  - Authenticated users can create, update, and delete.

## Project Structure

advanced-api-project/
│
├── advanced_api_project/ # Django project configuration
├── api/ # Application containing models, views, serializers, urls
└── manage.py


## Requirements

- Python 3.10+
- Django 5+
- Django REST Framework
- SQLite (default) or other database backend

Install dependencies:
```bash
pip install django djangorestframework

git clone https://github.com/yourusername/Alx_DjangoLearnLab.git
cd advanced-api-project

python manage.py migrate

python manage.py createsuperuser

python manage.py runserver

API Endpoints
Book Endpoints

| Method | Endpoint       | Description           | Permissions   |
| ------ | -------------- | --------------------- | ------------- |
| GET    | `/books/`      | List all books        | Public        |
| POST   | `/books/`      | Create new book       | Authenticated |
| GET    | `/books/<id>/` | Retrieve book details | Public        |
| PUT    | `/books/<id>/` | Update existing book  | Authenticated |
| DELETE | `/books/<id>/` | Delete book           | Authenticated |

Author Endpoints (if implemented)

| Method | Endpoint         | Description                        |
| ------ | ---------------- | ---------------------------------- |
| GET    | `/authors/`      | List all authors                   |
| GET    | `/authors/<id>/` | Retrieve author details with books |

Testing

curl -X GET http://127.0.0.1:8000/books/

With authentication token:
curl -H "Authorization: Token <your_token>" -X POST http://127.0.0.1:8000/books/ -d "title=Sample Book&publication_year=2023&author=1"

License
This project is part of the ALX Django Learn Lab and is intended for learning purposes.

---

If you save this as `README.md` in the **root of your project**, GitHub will automatically display it on your repository’s main page.  

Do you want me to also **add an API example output** so that anyone reading the README sees exactly what the JSON looks like? That would make it even clearer.
