from django import forms
from .models import *

class Faculty(forms.ModelForm):
    class Meta:
        model = Faculty
        fields = ('facName', 'facDesc')
        widgets = {
            'facName': forms.TextInput(attrs={'class': 'from-control', 'size': 50, 'maxlenght':50}),
            'facDesc': forms.TextInput(attrs={'class': 'from-control', 'row':3}),
        }
        labels = {
            'facName' : 'ชื่อคณะ',
            'facDesc' : 'รายละเอียดคณะ'
        }
