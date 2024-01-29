from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    name = forms.CharField(label='Your Name', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your name'}))
    email = forms.EmailField(label='Your Email', widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your email'}))
    address = forms.CharField(label='Your Address', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your address'}))
    
    class Meta:
        model = Order
        fields = ('name', 'email', 'address')