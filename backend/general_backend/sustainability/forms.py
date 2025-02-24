from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import User

#sustainability/forms.py

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    account_type = forms.ChoiceField(choices=User.ACCOUNT_TYPES, required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'account_type']


class LoginForm(AuthenticationForm):
    email = forms.EmailField(max_length=254, required=True, help_text='Required. Enter a valid email address.')
    account_type = forms.ChoiceField(choices=User.ACCOUNT_TYPES, required=True, help_text='Required. Select your account type.')

    class Meta:
        model = User
        fields = ['email', 'password']
