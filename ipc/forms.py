# forms.py

from django import forms
from .models import UploadedFile,Patent,UploadedPdfFile

class UploadFileForm(forms.ModelForm):
    
    class Meta:
        model = UploadedFile
        fields = ['file']
        widgets = {
            'file': forms.FileInput(attrs={'class': 'form-control'}),
        }

class PdfFileUploadForm(forms.ModelForm):
    class Meta:
        model = UploadedPdfFile
        fields = ['file']


class PatentForm(forms.ModelForm):
    patent_date = forms.DateField(input_formats=['%Y-%m-%d', '%d/%m/%y'],required=False)

    class Meta:
        model = Patent
        fields = ['patent_title', 'patent_owner', 'patent_description', 'patent_date']