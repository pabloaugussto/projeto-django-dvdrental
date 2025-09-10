from django.urls import path
from . import views


urlpatterns = [
    path('customer/', views.customer, name='mycustomer'),
    path('country/', views.country, name='country'),
    path('detalhes/<int:id>', views.detalhes, name='myDetalhes'),
    path('payment/<int:id>', views.payment, name='payment'),
    path('edit_payment/<int:payment_id>/', views.payment, name='payment_id'),
    path('category/', views.categoria, name='lista_categorias'),
    path('edit_customer/<int:customer_id>/', views.edit_customer, name='edit_customer'),
    path('categoria.html/<int:category_id>/', views.categoria, name='detalhes_categoria'),
    path('edit_categoria/<int:category_id>/', views.editcategoria, name='editar_categoria'),
    path('rental/', views.rental, name='myRental'), 
    
]

