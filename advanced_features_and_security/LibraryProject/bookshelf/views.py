from django.contrib.auth.decorators import permission_required
from django.shortcuts import render
from django.db.models import Q
from django.core.exceptions import ValidationError
from django.utils.html import escape

from .models import Book
from .forms import SearchForm   # Use forms for safe input handling


def book_list(request):
    """
    Displays a list of all books.
    Uses Django ORM (safe from SQL injection).
    """
    books = Book.objects.all()
    return render(request, "book_list.html", {"books": books})


def books(request):
    """
    Secure search functionality using Django forms and ORM filters.
    Prevents SQL injection and sanitizes user input.
    """
    form = SearchForm(request.GET or None)
    results = []

    if form.is_valid():  # validates and cleans user input
        query = form.cleaned_data.get("query")

        if query:
            # ORM filtering prevents SQL injection
            results = Book.objects.filter(
                Q(title__icontains=query) | Q(author__icontains=query)
            )

    return render(
        request,
        "books.html",
        {"form": form, "results": results}
    )


# -----------------------------
# Permission-protected views
# -----------------------------

@permission_required('accounts.can_view', raise_exception=True)
def view_post(request):
    """Protected view requiring 'can_view' permission."""
    return render(request, "view.html")


@permission_required('accounts.can_create', raise_exception=True)
def create_post(request):
    """Protected view requiring 'can_create' permission."""
    return render(request, "create.html")


@permission_required('accounts.can_edit', raise_exception=True)
def edit_post(request):
    """Protected view requiring 'can_edit' permission."""
    return render(request, "edit.html")


@permission_required('accounts.can_delete', raise_exception=True)
def delete_post(request):
    """Protected view requiring 'can_delete' permission."""
    return render(request, "delete.html")
