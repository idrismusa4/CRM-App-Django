from django.shortcuts import render
from .models import *

# Create your views here.
# def index(request): 
#     return HttpResponse("My First Django Project!")

# dict = {'books': 'Harry Potter, Peter pan, Live in the west, High school Chronicles, Bridge of Mayhem'}

def index(request):
    return render(request, 'crm/index.html')

def dashboard(request):
    # customers = Customer.object.all()
    # revenue = Revenue.object.all()
    return render(request, 'crm/dashboard.html')


def customers(request):
    # customers = Customer.object.all()
    return render(request, 'crm/customers.html')