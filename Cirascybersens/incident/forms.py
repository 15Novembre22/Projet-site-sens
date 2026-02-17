from django import forms
from .models import Incident

class IncidentForm(forms.ModelForm):
    class Meta:
        model = Incident
        fields = ['type_incident', 'description', 'email_contact', 'capture_ecran']
        widgets = {
            'type_incident': forms.Select(attrs={'class': 'form-select'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Décrivez les faits...'}),
            'email_contact': forms.EmailInput(attrs={'class': 'form-control', 'placeholder':'exemple@gmail.com'}),
            'capture_ecran': forms.FileInput(attrs={'class': 'form-control'}),
        }