from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Account
from django.contrib.auth.forms import AuthenticationForm

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = Account
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
            'profile_image',
        )

        widgets = {
            'first_name': forms.TextInput(attrs={
                'placeholder': 'First name',
                # No 'input-group' class here because that's for the wrapper div
            }),
            'last_name': forms.TextInput(attrs={
                'placeholder': 'Last name',
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Email',
            }),
            'username': forms.EmailInput(attrs={
                'placeholder': 'Email',
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({
            'placeholder': 'Password',
        })
        self.fields['password2'].widget.attrs.update({
            'placeholder': 'Confirm Password',
        })
        self.fields['profile_image'].widget.attrs.update({
            # Add attrs if you want to style file input
        })

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Email',
        'class': 'input-field',  # optional class for styling
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Password',
        'class': 'input-field',
    }))