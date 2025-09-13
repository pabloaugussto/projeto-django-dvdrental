
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
     path('films/', views.list_films, name='list_films_url'),
    path('add_film/', views.add_film, name='add_film_url'),
    path('add_category/', views.add_category, name='add_category'), 
    path('categories/', views.list_categories, name='list_categories'),
    path('listacustomer1/', views.listacustomer1, name='listacustomer1'),
    path('listacustomer/', views.listacustomer, name='listacustomer'),
    path('search_film_actors/', views.search_film_actors, name='search_film_actors_url'),
    path('film_details/<int:film_id>/', views.film_details, name='film_details_url'),
    path('edit_film/<int:film_id>/', views.edit_film, name='edit_film_url'),
]

