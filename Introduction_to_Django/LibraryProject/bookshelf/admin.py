from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Columns to show in the list view
    list_display = ('title', 'author', 'publication_year')
    
    # Add filters for quick narrowing
    list_filter = ('publication_year', 'author')
    
    # Enable search functionality
    search_fields = ('title', 'author')
