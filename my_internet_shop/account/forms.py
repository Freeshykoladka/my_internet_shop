from django import forms
from django.contrib.auth.forms import UserCreationForm, UserCreationForm
from django.contrib.auth.models import User



class UserRegistrationForm(UserCreationForm):
    """
    User Registration Form.
    """
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'placeholder': 'Your Username',
                                                                              'class': 'form-control',
                                                                              'id': 'username',
                                                                              'data-rule': 'minlen:4',
                                                                              'data-msg': 'Please enter at least 4 chars'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'placeholder': 'Your Email',
                                                                            'class': 'form-control',
                                                                            'id': 'email',
                                                                            'data-rule': 'email',
                                                                            'data-msg': 'Please enter a valid email'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'placeholder': 'Your Password',
                                                                                   'class': 'form-control',
                                                                                   'id': 'password',
                                                                                   'data-rule': 'minlen:4',
                                                                                   'data-msg': 'Please enter at least 4 chars'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Your Password',
                                                                                                   'class': 'form-control',
                                                                                                   'id': 'confirm_password',
                                                                                                   'data-rule': 'minlen:4',
                                                                                                   'data-msg': 'Please enter at least 4 chars'}))
    
    card_number = forms.CharField(label='Card Number', widget=forms.TextInput(attrs={'placeholder': 'Your Card Number',
                                                                                     'class': 'form-control',
                                                                                     'id': 'card_number',
                                                                                     'data-rule': 'creditcard',
                                                                                     'data-msg': 'Please enter a valid credit card number'}))

    expiration_date = forms.DateField(label='Expiration Date', widget=forms.DateInput(attrs={'placeholder': 'MM/YYYY',
                                                                                            'class': 'form-control',
                                                                                            'id': 'expiration_date',
                                                                                            'data-rule': 'creditcard',
                                                                                            'data-msg': 'Please enter a valid expiration date (MM/YYYY)'}))

    cvv = forms.CharField(label='CVV', widget=forms.TextInput(attrs={'placeholder': 'CVV',
                                                                     'class': 'form-control',
                                                                     'id': 'cvv',
                                                                     'data-rule': 'minlen:3',
                                                                     'data-msg': 'Please enter at least 3 chars'}))
    
class Meta:
    model = User
    fields = ('user','username','email','password1','password2','card_number','expiration_date','cvv')