from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'student_class', 'age']
        labels = {
            'name': 'Student Name',
            'student_class': 'Class',
            'age': 'Age',
        }
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Enter student name',
            }),
            'student_class': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Enter class (e.g., 10th Grade)',
            }),
            'age': forms.NumberInput(attrs={
                'class': 'form-input',
                'placeholder': 'Enter age',
                'min': 3,
                'max': 25,
            }),
        }
