# gestion/productos/forms.py
from django import forms
from .models import Producto
from proveedores.models import Proveedor

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre_producto', 'categoria', 'precio', 'proveedor', 'descripcion']
        widgets = {
            'nombre_producto': forms.TextInput(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-control', 'id': 'id_categoria'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
            'proveedor': forms.Select(attrs={'class': 'form-control', 'id': 'id_proveedor'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'categoria' in self.data:
            categoria = self.data.get('categoria')
            self.fields['proveedor'].queryset = Proveedor.objects.filter(tipo_proveedor=categoria)
        else:
            self.fields['proveedor'].queryset = Proveedor.objects.none()
