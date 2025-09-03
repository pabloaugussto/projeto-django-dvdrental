from django.urls import path
from . import views


urlpatterns = [
    path('customer/', views.customer, name='mycustomer'),
    path('country/', views.country, name='country'),
    path('detalhes/<int:id>', views.detalhes, name='myDetalhes'),                                          
    path('payment/<int:id>', views.payment, name='payment'),  
    path('edit_customer/<int:customer_id>/', views.edit_customer, name='edit_customer'),                                       
]

