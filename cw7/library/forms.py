from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author_name']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter book title'}),
            'author_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter author name'}),
        }
