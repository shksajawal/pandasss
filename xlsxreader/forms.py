from django import forms
from .models import ExcelFileUpload

class ExcelUpload(forms.ModelForm):
    class Meta:
        model = ExcelFileUpload
        fields = ('uploaded_file',)
