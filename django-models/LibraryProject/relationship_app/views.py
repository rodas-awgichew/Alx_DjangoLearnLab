from django.shortcuts import render
from .models import Book, Library
from django.views.generic.detail import DetailView

from .models import Library 

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import views as auth_views
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.contrib.auth import login


# Function-Based View
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

 



# Class-Based View
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'



# --- Registration View ---
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})


# --- Login View using Django’s built-in AuthView ---
class LoginView(auth_views.LoginView):
    template_name = 'relationship_app/login.html'


# --- Logout View using Django’s built-in AuthView ---
class LogoutView(auth_views.LogoutView):
    template_name = 'relationship_app/logout.html'

from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test, login_required
from .models import UserProfile

# --- Role Check Functions ---
def is_admin(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_librarian(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Member'


# --- Admin View ---
@login_required
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, "relationship_app/admin_view.html")


# --- Librarian View ---
@login_required
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, "relationship_app/librarian_view.html")


# --- Member View ---
@login_required
@user_passes_test(is_member)
def member_view(request):
    return render(request, "relationship_app/member_view.html")
