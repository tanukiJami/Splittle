# forms.py
from django import forms
from bills.models import ItemUserShare

class ItemUserShareForm(forms.ModelForm):
    class Meta:
        model = ItemUserShare
        fields = ['user', 'share_percentage']