from .models import Directory
from django import forms

class DirectoryForm(forms.ModelForm):
    class Meta:
        model = Directory
        fields = '__all__'