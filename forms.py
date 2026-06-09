from django import forms
from .models import FeeRecord

class FeeRecordForm(forms.ModelForm):
    class Meta:
        model = FeeRecord
        fields = ['student_name', 'roll_no', 'semester', 'amount', 'status']
        widgets = {
            'student_name': forms.TextInput(attrs={'class': 'form-control', 'id': 'student_name'}),
            'roll_no': forms.TextInput(attrs={'class': 'form-control', 'id': 'roll_no'}),
            'semester': forms.Select(attrs={'class': 'form-select', 'id': 'semester'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control', 'id': 'amount'}),
            'status': forms.Select(attrs={'class': 'form-select', 'id': 'status'}),
        }