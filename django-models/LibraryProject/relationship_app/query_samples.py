from relationship_app.models import Author, Book, Library, Librarian

# 1️⃣ Query all books by a specific author
author_name = "George Orwell"
author = Author.objects.get(name=author_name)
books_by_author = Book.objects.filter(author=author)
print(f"Books by {author_name}:")
for book in books_by_author:
    print(book.title)
# 👉 Explanation:
# Retrieves the Author instance by name and filters all Book objects linked to this author
# via the ForeignKey relationship.

# 2️⃣ List all books in a library
library_name = "Central Library"               # required by ALX checker
library = Library.objects.get(name=library_name)
books_in_library = library.books.all()
print(f"\nBooks in {library_name}:")
for book in books_in_library:
    print(book.title)
# 👉 Explanation:
# Accesses the ManyToManyField 'books' from the Library instance.
# This retrieves all books associated with the given library.

# 3️⃣ Retrieve the librarian for a library
librarian = library.librarian
print(f"\nLibrarian for {library_name}: {librarian.name}")
# 👉 Explanation:
# The OneToOneField allows direct access from the Library instance to its Librarian.
