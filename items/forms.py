from django import forms
from django.forms import ModelForm
from .models import Item


class CreateNewItem(ModelForm):
    """
    Initializing a form for creating new item
    """
    class Meta:
        model = Item
        fields = '__all__'

        # Giving styles to form(assigning Bootstrap class "form-control" to each of the fields)
        labels = {
            'title': '',
            'brand': '',
            'giver': '',
            'description': '',
            'category': 'Category *',
            'condition': 'Condition *',
            'image': 'Image *',
            'delivery': 'Delivery *',
            'city': '',
            'phone': '',
            'email': ''
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title *'}, required=True),
            'brand': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Item brand (if applicable)'}),
            'giver': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your name *'},  required=True ),
            'description': forms.TextInput(attrs={'class': 'form-control', 'rows': '5', 'placeholder': 'Describe your item in a few sentence'}),
            'category': forms.Select(attrs={'class': 'form-select'}, required=True),
            'condition': forms.Select(attrs={'class': 'form-select'}, required=True),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}, required=True),
            'delivery': forms.Select(attrs={'class': 'form-select'}, required=True),
            'city': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Your city *'}, required=True),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your phone number'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your email *'}, required=True),
        }



