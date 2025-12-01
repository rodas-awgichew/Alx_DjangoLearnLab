from rest_framework import generics, permissions, filters
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from django_filters import rest_framework as django_filters

from .models import Book
from .serializers import BookSerializer

# ----------------------------------------
# List all books + filtering + search + ordering
# ----------------------------------------

class BookListView(generics.ListAPIView):
    """
    Returns a list of all books.
    Now supports:
    - Filtering by: title, author, publication_year
    - Searching by: title, author
    - Ordering by: title, publication_year, id
    Accessible to everyone.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

    # Enable filtering, searching, ordering
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    ]

    # Filtering fields
    filterset_fields = ['title', 'author', 'publication_year']

    # Search fields
    search_fields = ['title', 'author']

    # Ordering fields
    ordering_fields = ['title', 'publication_year', 'id']
    ordering = ['id']  # default ordering


# ----------------------------------------
# Retrieve single book
# ----------------------------------------

class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


# ----------------------------------------
# Create new book
# ----------------------------------------

class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


# ----------------------------------------
# Update book
# ----------------------------------------

class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


# ----------------------------------------
# Delete book
# ----------------------------------------

class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
