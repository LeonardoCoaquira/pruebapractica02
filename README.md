# Prueba Practica 02

*Proyecto de Prueba*

#### Table of Contents
- [Development Setup](#development-setup)
    - [Local setup](#local-setup)
        - [Venv](#venv)
        - [Install Framewoks](#install-frameworks)
        - [Django Project](#django-project)
            - [Apps](#apps)
    - [Models](#models)
    - [Admin (Optional)](#admin)
        - [SuperUser](#superuser)
    - [Frontend](#frontend)
        - [Routing](#routing)
            - [Views](#views)
            - [Routes](#routes)
        - [Templates](#templates)
            - [Index](#index)
            - [Layout](#layout)
            - [Producto](#producto)
            - [Categoria](#categoria)
    - [API](#api)
        - [Setup](#setup-api)

## Development Setup

Steps to create a setup to run Django and DjangoRestFramework:
```bash
git clone "link of your repository for practice"
cd "created folder"
```

### Local setup
Steps to have an optimal environment for the project

#### Venv
Create and activate venv:
```bash
python -m venv venv
```
Activate venv:
```bash
venv\Scripts\activate
```

#### Install Frameworks
We are going to install two frameworks (you can select your favorite version):
Django 3.2:
```bash
pip install Django==3.2
```
DjangoRESTFramework 3.2:
```bash
pip install djangorestframework
```

#### Django Project
Creation of the project and apps:
Project:
```bash
django-admin startproject "project-name"
```

#### Apps
Before adding applications, it must be in the project folder::
```bash
cd "project-name"
```

App to display products:
```bash
python manage.py startapp "tienda"
```

App to receive product data :
```bash
python manage.py startapp "api"
```

After you create apps, you must be to integrate to project in settings.py file
```python
    'rest_framework',
    'tienda',
    'api',
```
It should look like this:
```python
    INSTALLED_APPS = (
        ...
        'rest_framework',
        'tienda',
        'api',
    )
```

## Models

Examples of Models (Models can be created in one app and imported into others):
```python
class Categoria(models.Model):
    nombre = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    categoria = models.ForeignKey(Categoria,on_delete=models.RESTRICT)
    nombre = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=6,decimal_places=2)
    stock = models.IntegerField(default=0)
    
    def __str__(self):
        return self.nombre
```
Using `on_delete=models.RESTRICT` on the `Product` model prevents a category from being deleted if there are products associated with it.

#### Migrations
To migrate the models execute the following:

```bash
python manage.py makemigrations
```
Then run:
```bash
python manage.py migrate
```

### Admin
This section of code allows you to add data to the Django admin panel, and you can also use SQLite Browser to edit the SQLite database directly.

#### Superuser
To create a super users we must be in the project folder
```bash
cd ..
ls
```
We repeat this process until we can see the apps and project folder together

After this run this code to create a superuser:
```bash
python manage.py createsuperuser
```
Select your preferred name and password

You must also add to the panel the power to register information
```python
from .models import Categoria,Producto

admin.site.register(Categoria)
admin.site.register(Producto)
```

Run the server to check the admin panel
```bash
python manage.py runserver
```
Enter this direction to add information in Categorias and Productos
```bash
http://127.0.0.1:8000/admin
```
## Frontend
We create the templates folder inside the app to display products:
Go to the app folder:
```bash
cd "tienda"
```
Create and go the templates folder:
```bash
mkdir templates
cd templates
```
Load the static folder in "tienda" (given by teacher)
### Routing
We create the routes for the frontend application
Create a file index.html and product.html:
index.html:
```html
<h1>Inicio</h1>
```
producto.html:
```html
<h1>Producto</h1>
```

#### Views
Create the next functions in views.py
```python
def index(request):
    return render(request,'index.html')

def producto(request):
    return render(request,'producto.html')
```

#### Routes
Create the urls.py file in "tienda" folder
Inside the file we put:
```python
from django.urls import path
from . import views

app_name = 'tienda'

urlpatterns = [
    path('',views.index, name="index"),
    path('producto', views.producto, name="producto")
]
```
Add (or modify) in the project's urls.py file:
```python
from django.urls import path,include

urlpatterns = [
    path('',include('tienda.urls')),
    path('admin/', admin.site.urls),
]
```
### Templates
We create the routes for the frontend application
Create a file index.html and product.html:
index.html:
```html
<h1>Inicio</h1>
```
producto.html:
```html
<h1>Producto</h1>
```

#### Index
Modify index.html:
```html
{% extends 'layout.html' %}
{% block content %}
<div class="container px-4 px-lg-5 mt-5">
    <div class="row gx-4 gx-lg-5 row-cols-2 row-cols-md-3 row-cols-xl-4 justify-content-center">
        {% for prod in productos %}
        <div class="col mb-5">
            <div class="card h-100">
                <!-- Product image-->
                <img class="card-img-top" src="https://dummyimage.com/450x300/dee2e6/6c757d.jpg" alt="..." />
                <!-- Product details-->
                <div class="card-body p-4">
                    <div class="text-center">
                        <!-- Product name-->
                        <h5 class="fw-bolder"><a href="{% url 'tienda:producto' prod.id %}">{{prod.nombre}}</a></h5>
                        <!-- Product price-->
                        ${{prod.precio}}
                    </div>
                </div>
                <!-- Product actions-->
                <div class="card-footer p-4 pt-0 border-top-0 bg-transparent">
                    <div class="text-center"><a class="btn btn-outline-dark mt-auto" href="{% url 'tienda:categoria' prod.categoria.id %}">{{prod.categoria.nombre}}</a></div>
                </div>
            </div>
        </div>
        {% endfor %}
    </div>
</div>
{% endblock %}
```

#### Layout
Create the layout.html file in templates folder
```html
{% load static %}
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <title>Shop Homepage</title>
        <link href="{% static 'vendor/bootstrap/css/bootstrap.min.css' %} " rel="stylesheet">
        <link href="{% static 'css/shop.css' %}" rel="stylesheet">
      </head>
    
  <body>

    <!-- Navigation -->
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark fixed-top">
      <div class="container">
        <a class="navbar-brand" href="{% url 'tienda:index' %}">Start Bootstrap</a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarResponsive">
          <ul class="navbar-nav ml-auto">
            <li class="nav-item active">
              <a class="nav-link" href="#">Home
                <span class="sr-only">(current)</span>
              </a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#">About</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#">Services</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#">Contact</a>
            </li>
          </ul>
        </div>
      </div>
    </nav>

    <!-- Page Content -->
    <div class="container">

      <div class="row">

        <div class="col-lg-3">
          <h1 class="my-4">Shop Name</h1>          
            <div class="list-group">
                <ul class="navbar-nav me-auto mb-2 mb-lg-0 ms-lg-4">
                    <li class="nav-item"><a class="nav-link active" aria-current="page" href="{% url 'tienda:index' %}">Home</a></li>
                    {% for cat in categorias %}
                    <li class="nav-item"><a class="nav-link" href="{% url 'tienda:categoria' cat.id %}">{{cat.nombre}}</a></li>
                    {% endfor %}
                </ul>
              </div>
        </div>
        <!-- /.col-lg-3 -->

        <div class="col-lg-9">
          {% block content  %} {% endblock %}
        </div>
        <!-- /.col-lg-9 -->

      </div>
      <!-- /.row -->

    </div>
    <!-- /.container -->

    <!-- Footer -->
    <footer class="py-5 bg-dark">
      <div class="container">
        <p class="m-0 text-center text-white">Copyright &copy; Your Website 2019</p>
      </div>
      <!-- /.container -->
    </footer>

    <!-- Bootstrap core JavaScript -->
    <script src="{% static 'vendor/jquery/jquery.min.js' %}"></script>
    <script src="{% static 'vendor/bootstrap/js/bootstrap.bundle.min.js' %}"></script>

  </body>

</html>
```

### Producto
Modify to:
```html
{% extends 'layout.html' %}{% block content %}
<div class="container px-4 px-lg-5 mt-5">
    <div class="row gx-4 gx-lg-5 row-cols-2 row-cols-md-3 row-cols-xl-4 justify-content-center">
        <div class="card" style="width: 18rem;">
            <div class="card-body">
              <h5 class="card-title">{{producto.nombre}}</h5>
              <a href="{% url 'tienda:index' %}" class="btn btn-primary">Go Home</a>
            </div>
          </div>
    </div>
</div>
{% endblock %}
```

To show products in index.html need to change views.py:
```python
def index(request):
    product_list = Producto.objects.order_by('nombre')[:6]
    categorias_list = Categoria.objects.all()
    context = {
        'productos':product_list,
        'categorias': categorias_list
    }
    return render(request,'index.html',context)
```
Also we need to import models:
```python
from .models import *
```

Now we can select each Producto to get information about it:
Change views.py in "tienda":
```python
from django.shortcuts import get_object_or_404

def producto(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    categorias_list = Categoria.objects.all()
    return render(request,'producto.html',{'producto':producto,'categorias': categorias_list})
```
Modify urls.py in "tienda":
```python
from django.urls import path
from . import views

app_name = 'tienda'

urlpatterns = [
    path('',views.index, name="index"),
    path('producto/<int:producto_id>/', views.producto, name="producto"),
]
```

### Categoria
Modify urls.py:
```python
from django.urls import path
from . import views

app_name = 'tienda'

urlpatterns = [
    path('',views.index, name="index"),
    path('producto/<int:producto_id>/', views.producto, name="producto"),
    path('categoria/<int:categoria_id>/', views.categoria, name='categoria')
]
```

Add function to views.py in "tienda":
```python
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
```

## API
In this section we are going to use djangoRESTframework to provide an api for querying products and categories.

### Setup API
Go to the api folder and create the serializers.py file:
```python
from rest_framework import serializers

from tienda.models import Categoria,Producto

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'
        
class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'
```

### Views
Modify in views.py in API folder:
```python
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import viewsets

from tienda.models import Categoria,Producto
from .serializers import (
    CategoriaSerializer,
    ProductoSerializer
)

class IndexView(APIView):
    
    def get(self,request):
        lista_categorias = Categoria.objects.all()
        serializer_categoria = CategoriaSerializer(lista_categorias,many=True)
        return Response(serializer_categoria.data)
    
class CategoriaView(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    
class CategoriaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categoria.objects.all()
    lookup_url_kwarg  = 'categoria_id'
    serializer_class = CategoriaSerializer
    
class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
```

### Urls
Add or modify in urls.py in API folder:
```python
from django.urls import path,include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()

router.register(r'producto',views.ProductoViewSet,basename='producto')

urlpatterns = [
    path('',views.IndexView.as_view()),
    path('categoria',views.CategoriaView.as_view()),
    path('categoria/<int:categoria_id>',views.CategoriaDetailView.as_view()),
    path('admin/',include(router.urls))
]
```

Also add or modify in urls.py in project folder:
```python
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('',include('tienda.urls')),
    path('api/',include('api.urls')),
    path('admin/', admin.site.urls),
]
```
