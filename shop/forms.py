from django import forms
from .models import Product, Category

class ArtworkDescriptionForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['artwork_description']
        labels = {
            'artwork_description': 'Artwork Description'
        }
        widgets = {
            'artwork_description': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': 'Describe your artwork',
                'class': 'border-1 rounded shadow-sm'
            })
        }

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = 'sku', 'title', 'category', 'image', 'medium', 'price', 'user'

        # image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-1 rounded shadow-sm'
            if field_name == 'image_url':
                field.widget.attrs['required'] = False
            elif field_name == 'image':
                field.widget.attrs['required'] = False
            else:
                field.widget.attrs['required'] = True

class ArtworkForm(forms.Form):
    description = forms.CharField(label='Describe your artwork', widget=forms.Textarea)
    