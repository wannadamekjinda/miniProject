from django import forms
from .models import *

class FacultyForm(forms.ModelForm):
    class Meta:
        model = Faculty
        fields = ('facName', 'facDesc')
        widgets = {
            'facName': forms.TextInput(attrs={'class': 'from-control', 'size': 50, 'maxlenght':50}),
            'facDesc': forms.TextInput(attrs={'class': 'from-control', 'row':3}),
        }
        labels = {
            'facName' : 'ชื่อคณะ',
            'facDesc' : 'รายละเอียดคณะ',
        }

class MajorProgramForm(forms.ModelForm):
    class Meta:
        model = MajorProgram
        fields = ('majorProName', 'majorProDesc')
        widgets = {
            'majorProName': forms.TextInput(attrs={'class': 'from-control', 'size': 50, 'maxlenght':50}),
            'majorProDesc': forms.TextInput(attrs={'class': 'from-control', 'row':3}),
        }
        labels = {
            'majorProName' : 'ชื่อโปรแกรมวิชา',
            'majorProDesc' : 'รายละเอียดโปรแกรมวิชา',
        }
class SubjectListForm(forms.ModelForm):
    class Meta:
        model = SubjectList
        fields = ('idSubject','nameSubject','credit','aj')
        widgets = {
            'idSubject' : forms.TextInput(attrs={'class': 'form-control', 'size':55, 'maxlength':50}),
            'nameSubject': forms.TextInput(attrs={'class': 'form-control', 'size': 55, 'maxlength': 50}),
            'credit': forms.TextInput(attrs={'class': 'form-control', 'size': 55, 'maxlength': 50}),
            'aj': forms.TextInput(attrs={'class': 'form-control', 'size': 55, 'maxlength': 50}),
        }
        labels = {
            'idSubject': 'รหัสวิชา',
            'nameSubject': 'ชื่อวิชา',
            'credit': 'หย่วยกิต',
            'aj': 'อาจารย์ผู้สอน',
        }


