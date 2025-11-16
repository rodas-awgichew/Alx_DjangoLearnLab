
from django import forms
from .models import Book
from django.core.exceptions import ValidationError
import datetime

class SearchForm(forms.Form):
    q = forms.CharField(
        required=False,
        max_length=255,
        widget=forms.TextInput(attrs={'placeholder': 'Search books...'})
    )

    def clean_q(self):
        q = self.cleaned_data.get('q', '')
        # Example minimal sanitization: trim and optionally reject suspicious input
        q = q.strip()
        return q


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date']
        widgets = {
            'published_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean_title(self):
        title = self.cleaned_data.get('title', '').strip()
        if not title:
            raise ValidationError("Title required.")
        return title

    def clean_published_date(self):
        pub = self.cleaned_data.get('published_date')
        if pub and pub > datetime.date.today():
            raise ValidationError("Published date cannot be in the future.")
        return pub
