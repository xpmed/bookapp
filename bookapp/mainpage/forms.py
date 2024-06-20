from django import forms
from .models import Review, Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'title',
            'author',
            'description',
            's_description',
            'category',
            'cover',
        ]
