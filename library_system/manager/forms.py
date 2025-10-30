from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'year', 'category', 'description', 'total_copies', 'cover']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }
