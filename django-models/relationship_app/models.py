from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# --- Core Models ---

class Author(models.Model):
    """Represents the author of a book."""
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Library(models.Model):
    """Represents a physical library location."""
    name = models.CharField(max_length=150)
    # NOTE: The ManyToManyField to Book was removed because the Book model
    # already uses a ForeignKey to Library, defining the relationship.
    
    def __str__(self):
        return self.name

class Book(models.Model):
    """Represents a single book instance."""
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(
        Author, 
        on_delete=models.CASCADE, 
        related_name='books' # Added related_name for clarity
    )
    # FIX: Using a string literal 'Library' resolves the NameError 
    # because the Library class is defined later in the file.
    # This defines a One-To-Many relationship: many books belong to one library.
    library = models.ForeignKey(
        'Library', 
        related_name='books', 
        on_delete=models.CASCADE
    )

    class Meta:
        permissions = [
            ("can_add_book", "Can add a book"),
            ("can_change_book", "Can change a book"),
            ("can_delete_book", "Can delete a book"),
        ]

    def __str__(self):
        return self.title

class Librarian(models.Model):
    """Represents a librarian tied to a specific library."""
    name = models.CharField(max_length=100)
    # Correct usage of OneToOneField with the Library model
    library = models.OneToOneField(
        Library, 
        on_delete=models.CASCADE, 
        related_name='librarian'
    )

    def __str__(self):
        return f"{self.name} - {self.library.name}"


# --- User Profile Model (Role System) ---

class UserProfile(models.Model):
    """Extends the built-in User model with a role system."""
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='userprofile')
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='Member')

    def __str__(self):
        return f"{self.user.username} - {self.role}"

# --- Signals ---

@receiver(post_save, sender=User)
def create_or_save_user_profile(sender, instance, created, **kwargs):
    """
    Creates a UserProfile when a new User is created.
    Saves the profile on subsequent User saves.
    """
    if created:
        UserProfile.objects.create(user=instance)
    else:
        # Check if userprofile exists before trying to save
        if hasattr(instance, 'userprofile'):
            instance.userprofile.save()