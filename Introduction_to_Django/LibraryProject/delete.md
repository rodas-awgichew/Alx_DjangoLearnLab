# Delete Operation

```python
from bookshelf.models import Book

book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
# Output: (1, {'bookshelf.Book': 1})

Book.objects.all()
# Output: <QuerySet []>