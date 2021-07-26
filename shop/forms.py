from django import forms
# from .widgets import CustomClearableFileInput
from .models import Category, Product


class ProductForm(forms.ModelForm):
    
    class Meta:
        model = Product
        # Add list_selected_related so django will perform less queries on the database
        list_select_related = [
            'category', 'medium'
                               ]
        # Add search_fields so autocomplete will work in product admin 
        search_fields = [
            'title',
            'category',
            ]
        fields = [
            'sku',
            'title',
            'active', 
            'medium',
            'image', 
            'category', 
            'parent',
            'price', 
            'orientation', 
            'has_dimensions',
            'label',
        ]
        # image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]
        self.fields['price'].required = True

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-1 rounded shadow-sm'
            field.widget.attrs['autofocus'] = True
            field.widget.attrs['required'] = True