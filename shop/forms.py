from django import forms
# from .widgets import CustomClearableFileInput
from .models import Category, Product


from django import forms
from .models import Category, Product


class ProductForm(forms.ModelForm):
    artwork_description = forms.CharField(
        max_length=200,
        required=False,
        label='Artwork Description',
        widget=forms.Textarea(attrs={'rows': 3}),
    )

    class Meta:
        model = Product
        fields = ('sku', 'title', 'category', 'artwork_description', 'price', 'image', 'qty')
        labels = {
            'sku': 'SKU',
            'title': 'Title',
            'category': 'Category',
            'artwork_description': 'Artwork Description',
            'price': 'Price',
            'image': 'Image',
            'qty': 'Quantity'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        friendly_names = [(c.id, c.get_friendly_name()) for c in Category.objects.all()]
        self.fields['category'].choices = friendly_names