from relationship_app.models import Author, Book, Library, Librarian

# 1️⃣ Query all books by a specific author
author = Author.objects.get(name="George Orwell")
books_by_author = Book.objects.filter(author=author)
print("Books by George Orwell:")
for book in books_by_author:
    print(book.title)
# 👉 Explanation:
# We retrieve the Author instance and filter all Book objects related to that author
# using the ForeignKey relationship.


# 2️⃣ List all books in a specific library
library = Library.objects.get(name="Central Library")
books_in_library = library.books.all()
print("\nBooks in Central Library:")
for book in books_in_library:
    print(book.title)
# 👉 Explanation:
# The Library model has a ManyToManyField to Book.
# Accessing library.books.all() returns all books associated with that library.


# 3️⃣ Retrieve the librarian for a library
library = Library.objects.get(name="Central Library")
librarian = library.librarian  # uses the related_name='librarian'
print(f"\nLibrarian for {library.name}: {librarian.name}")
# 👉 Explanation:
# A OneToOne relationship allows direct access from the Library instance
# to its associated Librarian using the related_name defined in the model.
