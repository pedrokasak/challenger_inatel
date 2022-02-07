from django import forms
from .models import ImportsFile


class ImportsFileForms(forms.ModelForm):
    class Meta:

        model = ImportsFile

        fields = ('archive',)

        widgets = {
            'archive': forms.FileInput(attrs={'class': 'form-control', 'placeholder': '.xls ou .csv'}),
        }
