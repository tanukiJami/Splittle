# forms.py
from django import forms
from .models import Bill, BillItem

class BillForm(forms.ModelForm):
    class Meta:
        model = Bill
        fields = ['name', 'bill_type', 'due_date']

class BillItemForm(forms.ModelForm):
    class Meta:
        model = BillItem
        fields = ['name', 'price']