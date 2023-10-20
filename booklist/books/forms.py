from django import forms
from .models import *

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'slug', 'author', 'year_published', 'genres', 'rating', 'view_count']


