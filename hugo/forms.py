from django import forms
from .models import Hugo

class HugoForm(forms.ModelForm):
    class Meta:
        model = Hugo
        fields = ['user'
        ]

