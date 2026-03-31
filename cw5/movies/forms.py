from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['name', 'release_year']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter movie name', 'class': 'form-input'}),
            'release_year': forms.NumberInput(attrs={'placeholder': 'Enter release year', 'class': 'form-input'}),
        }
