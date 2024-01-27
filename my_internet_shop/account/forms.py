from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Username')
    email = forms.EmailField(label='Email')
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
    card_number = forms.CharField(label='Card Number', max_length=16)
    expiration_date = forms.DateField(label='Expiration Date')
    cvv = forms.CharField(label='CVV', max_length=3)