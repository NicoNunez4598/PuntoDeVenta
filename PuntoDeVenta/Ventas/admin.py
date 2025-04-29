from django.contrib import admin
from Ventas.models import Cliente, Producto, Empresa

# Register your models here.

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre_completo', 'dni', 'email', 'telefono', 'direccion', 'created', 'updated', 'impositivo')
    search_fields = ('id', 'nombre_completo', 'dni', 'email', 'telefono', 'direccion', 'impositivo')
    list_filter = ('created', 'updated')

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'descripcion', 'imagen', 'precio', 'cantidad', 'iva', 'created', 'updated')
    search_fields = ('id', 'descripcion', 'imagen', 'precio', 'cantidad', 'iva')
    list_filter = ('created', 'updated')

class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'cuit', 'direccion', 'telefono', 'email', 'created', 'updated')
    search_fields = ('nombre', 'cuit', 'direccion', 'telefono', 'email')
    list_filter = ('created', 'updated')

admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Empresa, EmpresaAdmin)