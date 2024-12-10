from django import forms
from .models import Inventario, HistorialInventario

class InventarioForm(forms.ModelForm):
    class Meta:
        model = Inventario
        fields = ['cantidad_disponible']
        widgets = {
            'cantidad_disponible': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class HistorialInventarioForm(forms.ModelForm):
    class Meta:
        model = HistorialInventario
        fields = ['descripcion']
        widgets = {
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
