from django.forms import ModelForm
from .models import Item


class CreateNewItem(ModelForm):
    """
    Initializing a form for creating new item
    """
    class Meta:
        model = Item
        fields = '__all__'
