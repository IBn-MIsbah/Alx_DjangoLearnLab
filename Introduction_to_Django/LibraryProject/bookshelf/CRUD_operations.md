---

### 📝 Combine All in `CRUD_operations.md`

````md
# Django ORM - CRUD Operations for Book Model

## CREATE

```python
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
print(book)
# Output: <Book: 1984>
```
````
