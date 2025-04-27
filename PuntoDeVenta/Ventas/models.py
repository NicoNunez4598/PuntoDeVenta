from django.db import models
from django.forms import model_to_dict

# Create your models here.

class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_completo = models.CharField(max_length=200, null=False, blank=False)
    dni = models.IntegerField(null=False, blank=False)
    email = models.EmailField()
    telefono = models.CharField(max_length=200,  null=False, blank=False)
    direccion = models.CharField(max_length=200, null=False, blank=False)
    impositivo = models.CharField(choices=(('RI', 'Responsable Inscripto'), ('E', 'Exento'), ('C', 'Consumidor Final'), ('M', 'Responsable Monotributo+')), max_length=5, null=False, blank=False, default= 'RI')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
    
    def __str__(self):
        return self.nombre_completo

class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=200, null=False, blank=False)
    imagen = models.ImageField(upload_to='productos/', null=False, blank=False)
    precio = models.DecimalField(max_digits=13, decimal_places=2, null=False, blank=False)
    cantidad = models.DecimalField(max_digits=13, decimal_places=2, null=False, blank=False)
    iva = models.DecimalField(max_digits=13, decimal_places=4, null=False, blank=False, choices=((0.21, '21%'), (0.105, '10.5%'), (0.27, '27%'), (0.025, '2.5%'), (0.0, '0%')))
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        order_with_respect_to = 'descripcion'
    
    def __str__(self):
        return self.descripcion

class Egreso(models.Model):
    fecha_pedido = models.DateField(max_length=255)
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL , null=True , related_name='clientee')
    total = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    pagado = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    comentarios = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now=True)
    ticket = models.BooleanField(default=True)
    desglosar = models.BooleanField(default=True)
    updated = models.DateTimeField(auto_now_add=True , null=True)

    class Meta:
        verbose_name='egreso'
        verbose_name_plural = 'egresos'
        order_with_respect_to = 'fecha_pedido'
    
    def __str__(self):
        return str(self.id)
   

class ProductosEgreso(models.Model):
    egreso = models.ForeignKey(Egreso, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.DecimalField(max_digits=20, decimal_places=2 , null=False)
    precio = models.DecimalField(max_digits=20, decimal_places=2 , null=False , default=0)
    subtotal = models.DecimalField(max_digits=20, decimal_places=2 , null=False , default=0)
    iva = models.DecimalField(max_digits=20, decimal_places=2 , null=False , default=0)
    total = models.DecimalField(max_digits=20, decimal_places=2 , null=False , default=0)
    created = models.DateTimeField(auto_now_add=True)
    entregado = models.BooleanField(default=True)
    devolucion = models.BooleanField(default=False)

    class Meta:
        verbose_name='producto egreso'
        verbose_name_plural = 'productos egreso'
        order_with_respect_to = 'created'
    
    def __str__(self):
        return self.producto
    
    def toJSON(self):
        item = model_to_dict(self, exclude=['created'])
        return item