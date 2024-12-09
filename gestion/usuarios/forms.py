# usuarios/forms.py
from django import forms
from .models import Usuario

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['username', 'first_name', 'last_name', 'email', 'fecha_nacimiento', 'rut', 'rol']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-group-input'}),
            'first_name': forms.TextInput(attrs={'class': 'form-group-input'}),
            'last_name': forms.TextInput(attrs={'class': 'form-group-input'}),
            'email': forms.EmailInput(attrs={'class': 'form-group-input'}),
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date', 'class': 'form-group-input'}),
            'rut': forms.TextInput(attrs={'class': 'form-group-input'}),
            'rol': forms.Select(attrs={'class': 'form-group-input'}),
        }
