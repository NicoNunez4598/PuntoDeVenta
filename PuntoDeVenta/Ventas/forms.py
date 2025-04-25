from django import forms
from .models import Cliente, Producto

class AddClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('id', 'nombre_completo', 'dni', 'email', 'telefono', 'direccion', 'impositivo')
        labels = {
            'id': 'ID: ',
            'nombre_completo': 'Nombre completo: ',
            'dni': 'DNI: ',
            'email': 'Email: ',
            'telefono': 'Teléfono: ',
            'direccion': 'Dirección: ',
            'impositivo': 'Situacion Impositiva: ',
        }

class EditClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('id','nombre_completo', 'dni', 'email', 'telefono', 'direccion', 'impositivo')
        labels = {
            'nombre_completo': 'Nombre completo: ',
            'dni': 'DNI: ',
            'email': 'Email: ',
            'telefono': 'Teléfono: ',
            'direccion': 'Dirección: ',
            'impositivo': 'Situacion Impositiva: ',
        }
        widgets = {
            'nombre_completo': forms.TextInput(attrs={'type': 'text', 'id': 'nombre_completo_editar'}),
            'dni': forms.TextInput(attrs={'id': 'dni_editar'}),
            'email': forms.TextInput(attrs={'type': 'text', 'id': 'email_editar'}),
            'telefono': forms.TextInput(attrs={'id': 'telefono_editar'}),
            'direccion': forms.TextInput(attrs={'type': 'text', 'id': 'direccion_editar'}),
            'impositivo': forms.TextInput(attrs={'id': 'impositivo_editar'}),
        }

class AddProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ('id', 'descripcion', 'imagen', 'precio', 'cantidad', 'iva')
        labels = {
            'id': 'ID: ',
            'descripcion': 'Descripción: ',
            'imagen': 'Imagen: ',
            'precio': 'Precio: ',
            'cantidad': 'Cantidad: ',
            'iva': 'IVA: ',
        }

class EditProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ('id', 'descripcion', 'imagen', 'precio', 'cantidad', 'iva')
        labels = {
            'id': 'ID: ',
            'descripcion': 'Descripción: ',
            'imagen': 'Imagen: ',
            'precio': 'Precio: ',
            'cantidad': 'Cantidad: ',
            'iva': 'IVA: ',
        }
        widgets = {
            'descripcion': forms.TextInput(attrs={'type': 'text', 'id': 'descripcion'}),
            'imagen': forms.FileInput(attrs={'type': 'file', 'id': 'imagen'}),
            'precio': forms.TextInput(attrs={'type': 'text', 'id': 'precio'}),
            'cantidad': forms.TextInput(attrs={'type': 'text', 'id': 'cantidad'}),
            'iva': forms.TextInput(attrs={'type': 'text', 'id': 'iva'}),
        }