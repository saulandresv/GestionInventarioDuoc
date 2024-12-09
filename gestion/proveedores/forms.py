from django import forms
from .models import Proveedor

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['nombre_razon_social', 'tipo_proveedor', 'rut', 'direccion', 'telefono', 'email', 'notas']
        widgets = {
            'nombre_razon_social': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo_proveedor': forms.Select(attrs={'class': 'form-control'}),
            'rut': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'notas': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
