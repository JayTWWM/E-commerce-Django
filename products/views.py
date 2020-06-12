from django.shortcuts import render
from .forms import CreateProductForm
from django.shortcuts import render, get_object_or_404
from datetime import date
from .models import Product

cart = []

def registerProductPage(request):
    form = CreateProductForm(request.POST or None,initial={'seller': request.user,'date' : date.today})
    if form.is_valid():
        form.save()
        form = CreateProductForm()
    context = {'form' : form}
    return render(request,'product/registration.html',context)

def productListPage(request):
    obj = Product.objects.filter(active=True)
    context = {"obj" : obj}
    return render(request, "product/list.html", context)

def productPage(request, id):
    object = Product.objects.get(id=id)
    context = {'object' : object}
    return render(request, "product/product.html", context)

def productCartPage(request, id):
    object = Product.objects.get(id=id)
    if request.method == 'POST':
        cart.append(object)
        print(cart)
    context = {'object' : object}
    return render(request, "product/productCart.html", context)

def cartPage(request):
    context = {"obj" : cart}
    return render(request, "product/cart.html", context)