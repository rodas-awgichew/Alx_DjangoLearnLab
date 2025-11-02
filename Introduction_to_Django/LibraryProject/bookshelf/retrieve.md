# Retrieve Operation

from bookshelf.models import Book

# Retrieve the book
book = Book.objects.get(title="1984")

# Display all attributes
book.title, book.author, book.publication_year
# Expected Output: ('1984', 'George Orwell', 1949)
