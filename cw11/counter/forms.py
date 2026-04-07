from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        'placeholder': 'Email address',
        'class': 'form-input',
    }))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'placeholder': 'Username',
            'class': 'form-input',
        })
        self.fields['password1'].widget.attrs.update({
            'placeholder': 'Password',
            'class': 'form-input',
        })
        self.fields['password2'].widget.attrs.update({
            'placeholder': 'Confirm password',
            'class': 'form-input',
        })
