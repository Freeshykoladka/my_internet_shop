from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    name = forms.CharField(label='Your Name', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your name'}))
    email = forms.EmailField(label='Your Email', widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your email'}))
    phone = forms.CharField(label='Your Phone', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your phone'}))
    address = forms.CharField(label='Your Address', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your address'}))

    credit_card_number = forms.CharField(label='Credit Card Number', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Credit Card Number'}))
    expiration_date = forms.CharField(label='Expiration Date', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'MM/YY'}))
    cvv = forms.CharField(label='CVV', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'CVV'}))

    class Meta:
        model = Order
        fields = ('name', 'email', 'phone', 'address', 'credit_card_number', 'expiration_date', 'cvv')