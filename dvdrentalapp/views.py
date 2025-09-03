
from django.http import HttpResponse
from django.template import loader
from .models import Customer, Rental, Country, Payment
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


def payment (request, id):
    myPayment = Payment.objects.filter(customer_id=id)
    customer = get_object_or_404(Customer, pk=id)
    template = loader.get_template('all_payments.html')
    context = {
        'myPayment' : myPayment,
        'customer_name' : f"{customer.first_name} {customer.last_name}",
    }
    return HttpResponse(template.render(context, request))

def country(request):
    country = Country.objects.all().values()
    template = loader.get_template('all_countries.html')
    context = {
    'country': country,
}
    return HttpResponse(template.render(context, request))


