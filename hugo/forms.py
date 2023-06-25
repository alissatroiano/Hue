from django import forms
from .models import Hugo

class HugoForm(forms.ModelForm):
    class Meta:
        model = Hugo
        fields = ['artwork_description', 'name']

    def __init__(self, *args, **kwargs):
            """
            Add placeholders and classes, remove auto-generated
            labels and set autofocus on first field
            """
            super().__init__(*args, **kwargs)

            for field_name, field in self.fields.items():
                """ Set a length requirement for the artwork description """
                if field_name == 'artwork_description':
                    field.widget.attrs['maxlength'] = 500
                    field.widget.attrs['rows'] = 3
                    field.widget.attrs['placeholder'] = 'Describe your artwork'
                    field.widget.attrs['class'] = 'border-1 rounded shadow-sm'
                    field.widget.attrs['required'] = True
                if field_name == 'name':
                    field.widget.attrs['placeholder'] = 'Give your artwork a name'
                    field.widget.attrs['class'] = 'border-1 rounded shadow-sm'
                    field.widget.attrs['required'] = True
                else:
                    field.widget.attrs['class'] = 'border-1 rounded shadow-sm'
                    field.widget.attrs['required'] = True
