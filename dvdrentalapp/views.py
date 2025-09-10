
from django.http import HttpResponse
from django.template import loader
from .models import Customer, Rental, Country, Payment, Category
from django.shortcuts import render, get_object_or_404, redirect

def customer(request):
    customer = Customer.objects.all().values()
    template = loader.get_template('all_customers.html')
    context = {
    'mycustomer': customer,
}
    return HttpResponse(template.render(context, request))

def edit_customer(request,customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    if request.method == "POST":
        customer.first_name = request.POST.get('first_name')
        customer.last_name = request.POST.get('last_name')
        customer.email = request.POST.get('email')
        
        customer.save()
        return redirect('/customer')
    return render(request, 'edit_customer.html', {'customer': customer})

def detalhes(request, id):
    myDetalhes = Rental.objects.filter(customer_id=id)
    customer = get_object_or_404(Customer, pk=id)
    template = loader.get_template('detalhes.html')
    context = {
        'myDetalhe' : myDetalhes,
        'customer_name' : f"{customer.first_name} {customer.last_name}",
    }
    return HttpResponse(template.render(context, request))

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
        return redirect('/category/')

    return render(request, 'categoria.html', {'categoria': categoria_obj})

def rental (request, id):
    myRental = Rental.objects.filter(rental_id=id)
    Rental = get_object_or_404(Rental, pk=id)
    template = loader.get_template('rental.html')
    context = {
        'myRental' : myRental,
        'customer_name' : f"{customer.first_name} {customer.last_name}",
    }
    return HttpResponse(template.render(context, request))

def payment (request, id):
    myPayment = Payment.objects.filter(customer_id=id)
    customer = get_object_or_404(Customer, pk=id)
    template = loader.get_template('all_payments.html')
    context = {
        'myPayment' : myPayment,
        'customer_name' : f"{customer.first_name} {customer.last_name}",
    }
    return HttpResponse(template.render(context, request))

def edit_payment(request, payment_id):
    payment_obj = get_object_or_404(Payment, pk=payment_id)

    if request.method == "POST":
        payment_obj.name = request.POST.get('name')
        payment_obj.save()
        return redirect('/payment/')

    return render(request, 'edit_payment.html', {'payment': payment_obj})

def country(request):
    country = Country.objects.all().values()
    template = loader.get_template('all_countries.html')
    context = {
    'country': country,
}
    return HttpResponse(template.render(context, request))





