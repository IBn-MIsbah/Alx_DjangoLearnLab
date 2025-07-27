import os
import django

# Setup Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_models.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Ensure data exists
def seed_data():
    a1, _ = Author.objects.get_or_create(name="J.K. Rowling")
    b1, _ = Book.objects.get_or_create(title="Harry Potter 1", author=a1)
    b2, _ = Book.objects.get_or_create(title="Harry Potter 2", author=a1)
    
    lib, _ = Library.objects.get_or_create(name="Central Library")
    lib.books.set([b1, b2])  # ManyToMany
    
    Librarian.objects.get_or_create(name="Mr. Smith", library=lib)

# Seed the DB
seed_data()

# 1. Query all books by a specific author
author = Author.objects.get(name="J.K. Rowling")
books_by_author = Book.objects.filter(author=author)
print(f"\nBooks by {author.name}:")
for book in books_by_author:
    print(f"📚 {book.title}")

# 2. List all books in a library
library = Library.objects.get(name="Central Library")
books_in_library = library.books.all()
print(f"\nBooks in {library.name}:")
for book in books_in_library:
    print(f"📘 {book.title}")

# 3. Retrieve the librarian for a library
librarian = Librarian.objects.get(library=library)
print(f"\nLibrarian at {library.name}: 👨‍🏫 {librarian.name}")
