from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib import messages
# Create your views here.
from .models import Product
# Create your tests here.
# Create your views here.
def index(request):
    productos = Product.objects.all().values()
    template = loader.get_template('index.html')
    context = {
    'productos': productos,
    }
    return HttpResponse(template.render(context, request))

def add(request):
    return render(request,'productForm.html',{})

def addproducto(request):
    name = request.POST['name']
    price = request.POST['price']
    description = request.POST['description']
    expiration_date = request.POST['d_expiration']
    product = Product(name=name, price=price, description=description, d_expiration = expiration_date)
    product.save()
    messages.success(request,'guardado correctamente')
    return redirect('/productos/lista')