# forms.py
from django import forms
from .models import Product, Category
from hugo.models import Style

class ProductForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label='Select Category')
    style = forms.ModelChoiceField(queryset=Style.objects.all(), empty_label='Select Style')

    class Meta:
        model = Product
        fields = ['title', 'orientation', 'label', 'has_dimensions', 'medium', 'category', 'style', 'price', 'image_url', 'image', 'qty']
