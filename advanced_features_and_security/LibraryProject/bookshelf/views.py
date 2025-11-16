from django.contrib.auth.decorators import permission_required
from django.shortcuts import render
from .models import Book



def book_list(request):
    books = Book.objects.all()      
    return render(request, "book_list.html", {"books": books})

def books(request):
    all_books = Book.objects.all()
    return render(request, "books.html", {"books": all_books})


@permission_required('accounts.can_view', raise_exception=True)
def view_post(request):
    return render(request, 'view.html')

@permission_required('accounts.can_create', raise_exception=True)
def create_post(request):
    return render(request, 'create.html')

@permission_required('accounts.can_edit', raise_exception=True)
def edit_post(request):
    return render(request, 'edit.html')

@permission_required('accounts.can_delete', raise_exception=True)
def delete_post(request):
    return render(request, 'delete.html')
