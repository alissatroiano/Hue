from django import forms
# from .widgets import CustomClearableFileInput
from .models import Category, Product


class ProductForm(forms.ModelForm):
    
    class Meta:
        model = Product
        fields = '__all__'
        
        # image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]
        self.fields['price'].required = True
        placeholders = {
            'sku': 'sk00000000801',
            'title': 'Artwork Title',
            '': 'Phone Number',
            'postcode': 'Postal Code',
            'town_or_city': 'Town or City',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'county': 'County, State or Locality',
            'country': 'Country',
        }

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-1 rounded shadow-sm'
            field.widget.attrs['placeholder'] = field.label
            field.widget.attrs['autofocus'] = True
            field.widget.attrs['required'] = True