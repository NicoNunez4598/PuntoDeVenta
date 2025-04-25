from django.shortcuts import render, redirect
from .models import Cliente, Producto
from .forms import AddClienteForm, EditClienteForm, AddProductoForm, EditProductoForm
from django.contrib import messages

# Create your views here.

def ventas_view(request):
    return render(request, 'ventas.html')

def clientes_view(request):
    clientes = Cliente.objects.all()
    form_personal = AddClienteForm()
    form_editar = EditClienteForm()
    context = {
        'clientes': clientes,
        'form_personal': form_personal,
        'form_editar': form_editar
    }
    return render(request, 'clientes.html', context)

def add_cliente_view(request):
    if request.POST:
        form_personal = AddClienteForm(request.POST, request.FILES)
        if form_personal.is_valid():
            try:
                form_personal.save()
            except:
                messages.error(request, 'Error al agregar el cliente')
                return redirect('Clientes')
    return redirect('Clientes')

def edit_cliente_view(request):
    if request.POST:
        cliente = Cliente.objects.get(id=request.POST.get('id_personal_editar'))
        form_editar = EditClienteForm(request.POST, request.FILES, instance=cliente)
        if form_editar.is_valid():
            try:
                form_editar.save()
            except:
                messages.error(request, 'Error al editar el cliente')
                return redirect('Clientes')
    return redirect('Clientes')

def delete_cliente_view(request):
    if request.POST:
        cliente = Cliente.objects.get(id=request.POST.get('id_personal_eliminar'))
        cliente.delete()
    return redirect('Clientes')

def productos_view(request):
    productos = Producto.objects.all()
    form_add = AddProductoForm()
    context = {
        'productos': productos,
        'form_add': form_add
    }
    return render(request, 'productos.html', context)

def add_producto_view(request):
    if request.POST:
        form_personal = AddProductoForm(request.POST, request.FILES)
        if form_personal.is_valid():
            try:
                form_personal.save()
            except:
                messages.error(request, 'Error al agregar el producto')
                return redirect('Productos')
    return redirect('Productos')

def edit_producto_view(request):
    if request.POST:
        producto = Producto.objects.get(id=request.POST.get('id_producto_editar'))
        form_editar = EditProductoForm(request.POST, request.FILES, instance=producto)
        if form_editar.is_valid():
            try:
                form_editar.save()
            except:
                messages.error(request, 'Error al editar el producto')
                return redirect('Productos')
    return redirect('Productos')

def delete_producto_view(request):
    if request.POST:
        producto = Producto.objects.get(id=request.POST.get('id_producto_eliminar'))
        producto.delete()
    return redirect('Productos')