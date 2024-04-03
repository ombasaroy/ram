from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

# Create your views here.


# SHOP VIEWS STARTS HERE
def index(request):
    return render(request, 'shop/index.html')


def store(request):
    return render(request, 'shop/store.html')


def checkout(request):
    return render(request, 'shop/checkout.html')


def product(request):
    return render(request, 'shop/product.html')

# SHOP VIEWS ENDS HERE


# ADMIN VIEWS STARTS HERE
def ramadmin(request):
    return render(request, 'ramadmin/index.html')


def ramadmin_login(request):
    return render(request, 'ramadmin/login.html')


def ramadmin_register(request):
    return render(request, 'ramadmin/register.html')


def ramadmin_add_product(request):
    categories = Categories.objects.all()
    context = {'categories': categories}

    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        category_id = request.POST.get('category_id')
        price = request.POST.get('price')
        image = request.FILES.get('image')

        query = Product(name=name, description=description, category_id=category_id, price=price, image=image)
        query.save()
        messages.success(request, 'SUCCESS!! Product added.')
        redirect('ramadmin_add_product')

    return render(request, 'ramadmin/addproduct.html', context)


def ramadmin_add_category(request):
    if request.method == 'POST':
        name = request.POST.get('category_name')
        description = request.POST.get('description')

        query = Categories(name=name, description=description)
        query.save()
        messages.success(request, 'Category added successfuly')
        return redirect('ramadmin_add_category')

    return render(request, 'ramadmin/addcategory.html')


def ramadmin_categories(request):
    categories = Categories.objects.all()
    context = {'categories': categories}

    return render(request, 'ramadmin/categories.html', context)


# ADMIN VIEWS ENDS HERE

















