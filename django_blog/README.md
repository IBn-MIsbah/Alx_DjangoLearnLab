# Django Blog Project

A simple blog application built with **Django** and **Django REST Framework**.  
The project demonstrates how to build a blogging platform with posts, comments, and tags.

---

## Features
- User authentication (login, logout, registration)
- Create, update, delete blog posts
- Add and display comments on posts
- Tag support for posts
- REST API endpoints for posts and comments

---

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/IBn-MIsbah/Alx_DjangoLearnLab/tree/main/django_blog
   cd django-blog
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run database migrations:
   ```bash
   python manage.py migrate
   ```

5. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```bash
   python manage.py runserver
   ```

---

## Usage

- Visit `http://127.0.0.1:8000/` to view the blog posts.
- Log in to create, update, or delete your own posts.
- Add comments to blog posts if logged in.
- Use tags to categorize blog posts.

---

## API Endpoints

- List posts: `/api/posts/`
- Post detail: `/api/posts/<id>/`
- List comments: `/api/posts/<id>/comments/`
- Create comment: `/api/posts/<id>/comments/new/`

---

## Technologies Used
- Django
- Django REST Framework
- SQLite (default DB)
- HTML, CSS (Django templates)

---

## License
This project is open-source and available under the [MIT License](LICENSE).
