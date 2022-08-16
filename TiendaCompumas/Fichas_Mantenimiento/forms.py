from django import forms
from .models import FichaMantenimiento

class FichaFormulario(forms.ModelForm):
    class Meta:
        model = FichaMantenimiento
        fields = ["numero_ficha", "dispositivo", "problema", "fecha"]
        widgets = {
            'numero_ficha': forms.TextInput(attrs={'placeholder':'Numero', 'class': 'form-control'}),
            'dispositivo': forms.TextInput(attrs={'placeholder':'Ingrese Dispositivo', 'class': 'form-control'}),
            'problema': forms.TextInput(attrs={'placeholder':'Ingrese problema del dispositivo', 'class': 'form-control'}),
            'fecha': forms.TextInput(attrs={'placeholder':'Ingrese fecha', 'class': 'form-control'}),
        }