from django import forms
from .models import Detail

class PostForm(forms.ModelForm):
    class Meta:
        model=Detail
        fields=[
            'name',
            'email',
            'mobile'
        ]