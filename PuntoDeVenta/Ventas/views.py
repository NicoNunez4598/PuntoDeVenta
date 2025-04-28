from django.shortcuts import render, redirect
from .models import Cliente, Producto, Egreso, ProductosEgreso
from .forms import AddClienteForm, EditClienteForm, AddProductoForm, EditProductoForm
from django.contrib import messages
from django.views.generic import ListView
from django.http import JsonResponse, HttpResponse
from weasyprint.text.fonts import FontConfiguration
from django.template.loader import get_template
from weasyprint import HTML, CSS
from django.conf import settings
import os


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
    form_editar = EditProductoForm()
    context = {
        'productos': productos,
        'form_add': form_add,
        'form_editar': form_editar
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

class add_ventas(ListView):
    template_name = 'add_ventas.html'
    model = Egreso

    def dispatch(self,request,*args,**kwargs):
        return super().dispatch(request, *args, **kwargs)
    """
    def get_queryset(self):
        return ProductosPreventivo.objects.filter(
            preventivo=self.kwargs['id']
        )
    """
    def post(self, request,*ars, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'autocomplete':
                data = []
                for i in Producto.objects.filter(descripcion__icontains=request.POST["term"])[0:10]:
                    item = i.toJSON()
                    item['value'] = i.descripcion
                    data.append(item)
            else:
                data['error'] = "Ha ocurrido un error"
        except Exception as e:
            data['error'] = str(e)

        return JsonResponse(data,safe=False)


def export_pdf_view(request, id, iva):
    #print(id)
    template = get_template("ticket.html")
    #print(id)
    subtotal = 0 
    iva_suma = 0 

    venta = Egreso.objects.get(pk=float(id))
    datos = ProductosEgreso.objects.filter(egreso=venta)
    for i in datos:
        subtotal = subtotal + float(i.subtotal)
        iva_suma = iva_suma + float(i.iva)

    empresa = "Mi empresa S.A. De C.V"
    context ={
        'num_ticket': id,
        'iva': iva,
        'fecha': venta.fecha_pedido,
        'cliente': venta.cliente.nombre,
        'items': datos, 
        'total': venta.total, 
        'empresa': empresa,
        'comentarios': venta.comentarios,
        'subtotal': subtotal,
        'iva_suma': iva_suma,
    }
    html_template = template.render(context)
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = "inline; ticket.pdf"
    css_url = os.path.join(settings.BASE_DIR,'index\static\index\css/bootstrap.min.css')
    #HTML(string=html_template).write_pdf(target="ticket.pdf", stylesheets=[CSS(css_url)])
   
    font_config = FontConfiguration()
    HTML(string=html_template, base_url=request.build_absolute_uri()).write_pdf(target=response, font_config=font_config,stylesheets=[CSS(css_url)])

    return response
