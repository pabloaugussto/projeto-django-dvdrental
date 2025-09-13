
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Customer, Rental, Country, Payment, Category, Film, Language, FilmActor

def customer(request):
    all_customers = Customer.objects.all().values()
    context = {
        'mycustomer': all_customers,
    }
    return render(request, 'all_customers.html', context)

def edit_customer(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    if request.method == "POST":
        customer.first_name = request.POST.get('first_name')
        customer.last_name = request.POST.get('last_name')
        customer.email = request.POST.get('email')
        customer.save()
        return redirect('mycustomer') 
    return render(request, 'edit_customer.html', {'customer': customer})

def detalhes(request, id):
    myDetalhes = Rental.objects.filter(customer_id=id)
    customer = get_object_or_404(Customer, pk=id)
    context = {
        'myDetalhe' : myDetalhes,
        'customer_name' : f"{customer.first_name} {customer.last_name}",
    }
    return render(request, 'detalhes.html', context)

def categoria(request, category_id=None):
    if category_id is not None:
        categoria_obj = get_object_or_404(Category, pk=category_id)
        return render(request, 'categoria.html', {'categoria': categoria_obj})
    else:
        todas_as_categorias = Category.objects.all()
        return render(request, 'all_categoria.html', {'mycategoria': todas_as_categorias})

def editcategoria(request, category_id):
    categoria_obj = get_object_or_404(Category, pk=category_id)
    if request.method == "POST":
        categoria_obj.name = request.POST.get('name')
        categoria_obj.save()
        return redirect('lista_categorias') # Melhorado: Usando nome da URL
    return render(request, 'categoria.html', {'categoria': categoria_obj})

def rental(request, id):
    
    rental_obj = get_object_or_404(Rental, pk=id)
    context = {
        'myRental' : rental_obj,
        'customer_name' : f"{rental_obj.customer.first_name} {rental_obj.customer.last_name}",
    }
    return render(request, 'rental.html', context)

def payment(request, id):
    myPayment = Payment.objects.filter(customer_id=id)
    customer = get_object_or_404(Customer, pk=id)
    context = {
        'myPayment' : myPayment,
        'customer_name' : f"{customer.first_name} {customer.last_name}",
    }
    return render(request, 'all_payments.html', context)

def edit_payment(request, payment_id):
    payment_obj = get_object_or_404(Payment, pk=payment_id)
    if request.method == "POST":
        payment_obj.name = request.POST.get('name')
        payment_obj.save()
        
        return redirect('mycustomer') 
    return render(request, 'edit_payment.html', {'payment': payment_obj})

def country(request):
    countries = Country.objects.all().values()
    context = {
        'country': countries,
    }
    return render(request, 'all_countries.html', context)

def list_categories(request):
    categories = Category.objects.all().order_by('name')
    return render(request, 'list_categories.html', {'categories': categories})

def add_category(request):
    if request.method == "POST":
        name = request.POST.get('name')
        if name:
            category = Category(name=name, last_update=timezone.now())
            category.save()
        return redirect('list_categories')
    return render(request, 'add_category.html')

def list_films(request):
    films = Film.objects.all().order_by('title')
    context = {
        'films': films
    }
    return render(request, 'list_films.html', context)

def add_film(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        default_language = Language.objects.first()
        Film.objects.create(
            title=title,
            language=default_language,
            rental_duration=3,
            rental_rate=4.99,
            replacement_cost=19.99,
            last_update=timezone.now()
        )
        return redirect('list_films_url')
    return render(request, 'add_film.html')

def listacustomer1(request):
    search_name = request.GET.get('search_name', '')
    if search_name:
        mycustomers = Customer.objects.filter(first_name__icontains=search_name).values()
    else:
        mycustomers = Customer.objects.all().values()
    
    context = {
        'listcustomer1': mycustomers,
    }
    return render(request, 'list_customers1.html', context)

def search_film_actors(request):
    search_title = request.GET.get('search_title', '')
    if search_title:
        film_actors = FilmActor.objects.filter(film__title__icontains=search_title)
    else:
        film_actors = FilmActor.objects.all()[:50]

    context = {
        'film_actors': film_actors,
        'search_title': search_title
    }
    return render(request, 'search_film_actors.html', context)

def listacustomer(request):
    mycustomers = Customer.objects.all() 
    context = {
        'listcustomer': mycustomers,
    }
    return render(request, 'list_customers.html', context)






