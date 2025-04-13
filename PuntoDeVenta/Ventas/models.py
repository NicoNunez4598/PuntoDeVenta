from django.db import models

# Create your models here.

class Cliente(models.Model):
    nro_cuenta = models.AutoField(primary_key=True)
    nombre_completo = models.CharField(max_length=200, null=False, blank=False)
    dni = models.IntegerField(null=False, blank=False)
    email = models.EmailField()
    telefono = models.CharField(max_length=200,  null=False, blank=False)
    direccion = models.CharField(max_length=200, null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
    
    def __str__(self):
        return self.nombre_completo

class Producto(models.Model):
    nro_producto = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=200, null=False, blank=False)
    imagen = models.ImageField(upload_to='productos/', null=False, blank=False)
    precio = models.DecimalField(max_digits=13, decimal_places=2, null=False, blank=False)
    cantidad = models.DecimalField(max_digits=13, decimal_places=2, null=False, blank=False)
    iva = models.DecimalField(max_digits=13, decimal_places=2, null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        order_with_respect_to = 'descripcion'
    
    def __str__(self):
        return self.descripcion