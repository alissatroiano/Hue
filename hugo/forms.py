from django import forms
from .models import Artwork

class ArtworkForm(forms.ModelForm):
    class Meta:
        model = Artwork
        fields = ['title', 'style', 'artwork_description', 'is_downloadable', 'is_public']

    def __init__(self, *args, **kwargs):
            """
            Add placeholders and classes, remove auto-generated
            labels and set autofocus on first field
            """
            super().__init__(*args, **kwargs)

            for field_name, field in self.fields.items():
                """ Set a length requirement for the artwork description """
                if field_name == 'artwork_description':
                    field.widget.attrs['maxlength'] = 400
                    field.widget.attrs['rows'] = 3
                    field.widget.attrs['placeholder'] = 'Describe your artwork'
                    field.widget.attrs['class'] = 'border-1 rounded shadow-sm'
                    field.widget.attrs['required'] = True
                if field_name == 'title':
                    field.widget.attrs['placeholder'] = 'Give your artwork a title'
                    field.widget.attrs['class'] = 'border-1 rounded shadow-sm'
                    field.widget.attrs['required'] = True
                if field_name == 'style':
                    field.widget.attrs['required'] = True
                else:
                    field.widget.attrs['class'] = 'border-1 rounded shadow-sm'
                    field.widget.attrs['required'] = False


class EditArtworkForm(forms.ModelForm):
    class Meta:
        model = Artwork
        fields = ['title', 'is_downloadable', 'is_public']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-1 rounded shadow-sm'
            field.widget.attrs['required'] = False


class AddToStoreForm(forms.ModelForm):
  class Meta:
        model = Artwork
        fields = ['price']
        
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

            for field_name, field in self.fields.items():
                field.widget.attrs['class'] = 'border-1 rounded shadow-sm'
                field.widget.attrs['required'] = False
