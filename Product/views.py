from itertools import product

from django.shortcuts import render
from Product.models import Product, Category


def main_view(request):
    if request.method == 'GET':
        return render(request, 'layouts/main.html')


def products_view(request):
    if request.method == 'GET':
        products = Product.objects.all()

        context_data = {
            'products': products
        }

        return render(request, 'products/products.html', context=context_data)


def categories_view(request):
    if request.method == 'GET':
        categories = Category.objects.all()

        context_data = {
            'categories': categories
        }

        return render(request, 'categories/categories.html', context=context_data)


