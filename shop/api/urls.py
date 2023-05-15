from django.urls import path,include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()

router.register(r'producto',views.ProductoViewSet,basename='producto')

urlpatterns = [
    path('',views.IndexView.as_view()),
    path('categoria',views.CategoriaView.as_view()),
    path('categoria/<int:categoria_id>',views.CategoriaDetailView.as_view()),
    path('admin/',include(router.urls)),
    path('productos/', views.ProductoListView.as_view(), name='producto-list'),
    path('productos/<int:producto_id>/', views.ProductoDetailView.as_view(), name='producto-detail'),

]