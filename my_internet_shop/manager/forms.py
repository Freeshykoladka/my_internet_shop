from django import forms
from catalog.models import Order


class PurchasesEditForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('name', 'email', 'address', 'is_precessed')
