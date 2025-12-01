from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Book
from .serializers import BookSerializer


# List all books (Read-only, open to everyone)
class BookListView(generics.ListAPIView):
    """
    Returns a list of all books.
    Uses DRF's ListAPIView for optimized read-only access.
    Accessible to anyone (AllowAny).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


# Retrieve a single book by ID (Read-only)
class BookDetailView(generics.RetrieveAPIView):
    """
    Returns a single book based on its primary key (ID).
    Accessible to anyone.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


# Create a new book (Authenticated users only)
class BookCreateView(generics.CreateAPIView):
    """
    Creates a new Book entry.
    Only authenticated users can create books.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()


# Update a book (Authenticated users only)
class BookUpdateView(generics.UpdateAPIView):
    """
    Updates an existing Book.
    Only authenticated users can update.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        serializer.save()


# Delete a book (Authenticated users only)
class BookDeleteView(generics.DestroyAPIView):
    """
    Deletes a Book.
    Only authenticated users can delete.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
