from django.shortcuts import render, get_object_or_404
from .models import *
# Create your views here.
def index(request):
    product_list = Producto.objects.order_by('nombre')[:6]
    categorias_list = Categoria.objects.all()
    context = {
        'productos':product_list,
        'categorias': categorias_list
    }
    return render(request,'index.html',context)

def producto(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    categorias_list = Categoria.objects.all()
    return render(request,'producto.html',{'producto':producto,'categorias': categorias_list})

def categoria(request, categoria_id):
    categoria = Categoria.objects.get(pk=categoria_id)
    lista_productos = categoria.producto_set.all()
    lista_categorias = Categoria.objects.all()

    context = {
        'productos':lista_productos,
        'categorias':lista_categorias,
        'categoria':categoria
    }
    
    return render(request,'index.html',context)