from django.contrib import admin
from Ventas.models import Cliente, Producto

# Register your models here.

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nro_cuenta', 'nombre_completo', 'dni', 'email', 'telefono', 'direccion', 'created', 'updated')
    search_fields = ('nro_cuenta', 'nombre_completo', 'dni', 'email', 'telefono', 'direccion')
    list_filter = ('created', 'updated')

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nro_producto', 'descripcion', 'imagen', 'precio', 'cantidad', 'iva', 'created', 'updated')
    search_fields = ('nro_producto', 'descripcion', 'imagen', 'precio', 'cantidad', 'iva')
    list_filter = ('created', 'updated')

admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Producto, ProductoAdmin)