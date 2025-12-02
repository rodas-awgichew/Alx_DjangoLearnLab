from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User

from .models import Author, Book


class BookAPITests(APITestCase):

    def setUp(self):
        """
        Create reusable test data and a test user.
        """
        self.user = User.objects.create_user(username="testuser", password="password123")

        self.author = Author.objects.create(name="Author One")

        self.book1 = Book.objects.create(
            title="Book One",
            publication_year=2000,
            author=self.author
        )

        self.book2 = Book.objects.create(
            title="Another Book",
            publication_year=1995,
            author=self.author
        )

        self.list_url = reverse("book-list")          # /api/books/
        self.detail_url = reverse("book-detail", args=[self.book1.id])  # /api/books/<id>/
        self.create_url = reverse("book-create")
        self.update_url = reverse("book-update", args=[self.book1.id])
        self.delete_url = reverse("book-delete", args=[self.book1.id])

    # ------------------------------------------------------------
    # LIST VIEW TEST
    # ------------------------------------------------------------
    def test_list_books(self):
        """
        Ensure the list endpoint returns all books.
        """
        response = self.client.get(self.list_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    # ------------------------------------------------------------
    # DETAIL VIEW TEST
    # ------------------------------------------------------------
    def test_get_single_book(self):
        """
        Ensure retrieving a single book works.
        """
        response = self.client.get(self.detail_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], self.book1.title)

    # ------------------------------------------------------------
    # CREATE VIEW TEST
    # ------------------------------------------------------------
    def test_create_book_requires_authentication(self):
        """
        Creating a book should require authentication.
        """
        data = {
            "title": "New Test Book",
            "publication_year": 2024,
            "author": self.author.id
        }

        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_authenticated_user_can_create_book(self):
        """
        A logged-in user should be able to create a book.
        """
        self.client.login(username="testuser", password="password123")

        data = {
            "title": "Created by Test User",
            "publication_year": 2024,
            "author": self.author.id
        }

        response = self.client.post(self.create_url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    # ------------------------------------------------------------
    # UPDATE VIEW TEST
    # ------------------------------------------------------------
    def test_update_book_requires_authentication(self):
        data = {"title": "Updated Title"}

        response = self.client.patch(self.update_url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_authenticated_user_can_update_book(self):
        self.client.login(username="testuser", password="password123")
        data = {"title": "Updated Title"}

        response = self.client.patch(self.update_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Title")

    # ------------------------------------------------------------
    # DELETE VIEW TEST
    # ------------------------------------------------------------
    def test_delete_book_requires_authentication(self):
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_authenticated_user_can_delete_book(self):
        self.client.login(username="testuser", password="password123")

        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    # ------------------------------------------------------------
    # FILTERING, SEARCH, ORDERING
    # ------------------------------------------------------------
    def test_filter_by_publication_year(self):
        """
        Ensure filtering works.
        Example: /api/books/?publication_year=2000
        """
        response = self.client.get(self.list_url, {"publication_year": 2000})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "Book One")

    def test_search_books(self):
        """
        Ensure search feature works.
        Example: /api/books/?search=Another
        """
        response = self.client.get(self.list_url, {"search": "Another"})

        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "Another Book")

    def test_ordering_books(self):
        """
        Ensure ordering works.
        Example: /api/books/?ordering=publication_year
        """
        response = self.client.get(self.list_url, {"ordering": "publication_year"})

        self.assertEqual(response.data[0]["publication_year"], 1995)   # oldest first
