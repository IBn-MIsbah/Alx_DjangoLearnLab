
#### 📝 `delete.md`

```md
# Delete Book

```python
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
Book.objects.all()
# Output: <QuerySet []>
