from .models import Directory
from django import forms

class DirectoryForm(forms.ModelForm):
    class Meta:
        model = Directory
        fields = ['name','number','email','address','profilepic','comment']
        labels = {
            'profilepic': 'Image',
            'name':'Full Name',
            'number':'Contact No.',
            'email':'Email ID'
        }
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'number':forms.NumberInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'address':forms.TextInput(attrs={'class':'form-control'}),
            'comment':forms.Textarea(attrs={'class':'form-control','rows':2,'cols':2}),
        }