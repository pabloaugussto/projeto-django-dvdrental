
from django.http import HttpResponse
from django.template import loader
from .models import Country
def country(request):
    country = Country.objects.all().values()
    template = loader.get_template('all_countries.html')
    context = {
    'country': country,
}
    return HttpResponse(template.render(context, request))

from django.http import HttpResponse
from django.template import loader
from .models import Customer
def customer(request):
    customer = Customer.objects.all().values()
    template = loader.get_template('all_customers.html')
    context = {
    'customer': customer,
}
    return HttpResponse(template.render(context, request))

