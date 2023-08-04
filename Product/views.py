from itertools import product

from django.shortcuts import render
from Product.models import Product, Category, Review
from products.forms import ProductCreateForm, CategoryCreateForm, ReviewCreateForm

from products.constants import PAGINATION_LIMIT


def main_view(request):
    if request.method == 'GET':
        return render(request, 'layouts/main.html')


def products_view(request):
    if request.method == 'GET':
        products = Product.objects.all()
        posts = Post.objects.all().order_by('-create_date')
        search = request.GET.get('search')
        page = int(request.GET.get('page', 1))

        if search:
            products = products.filter(title__contains=search) | products.filter(description__contains=search)

        max_page = posts.__len__() / PAGINATION_LIMIT
        if round(max_page) < max_page:
            max_page = round(max_page) + 1
        else:
            max_page = round(max_page)

        products = products [PAGINATION_LIMIT * (page-1):PAGINATION_LIMIT * page]


        context_data = {
            'products': products
            'user': request.user,
            'pages': range(1, max_page+1)
            
        }

        return render(request, 'products/products.html', context=context_data)


def categories_view(request):
    if request.method == 'GET':
        categories = Category.objects.all()

        context_data = {
            'categories': categories
        }

        return render(request, 'categories/categories.html', context=context_data)


def products_detail_view(request, id):
    if request.method == 'GET':
        product = Products.objects.get(id=id)

        context = {
            'product': product,
            'comments': product.comment_set.all(),
            'form': CommentsCreateForm
        }

        return render(request, 'products/detail.html', context=context)

    if request.method == 'POST':
        product = Products.objects.get(id=id)
        data = request.POST
        form = CommentsCreateForm(data=data)

        if form.is_valid():
            Comment.objects.create(
                text=form.cleaned_data.get('text'),
                title=form.cleaned_data.get('name'),
                product=product

            )

        context = {
            'product': product,
            'comments': product.comment_set.all(),
            'form': form
        }

        return render(request, 'products/detail.html', context=context)

def create_product_view(request):
    if request.method == 'GET':
        context_data = {'form': Products}
        return render(request, 'products/', context=context_data)

    if request.method == 'POST':
        data, files = request.POST, request.FILES
        form = Products_create(data, files)
        if form.is_valid():
            Products.objects.create(
                image=form.cleaned_data.get('image'),
                title=form.cleaned_data.get('title'),
                description=form.cleaned_data.get('description'),
                rate=form.cleaned_data.get('rate'),
                category=form.cleaned_data.get('category'),
                prize=form.cleaned_data.get('prize'),


            )
            return redirect('/products/')
        return render(request, 'products/categories.html', context={'form': form})


def create_category_view(request):
    if request.method == 'GET':
        context_data = {'form': Category_create}

        return render(request, 'products/categories.html', context=context_data)

    if request.method == 'POST':
        data, files = request.POST, request.FILES
        form = Category_create(data, files)

        if f.is_valid():
            Category.objects.create(
                title=form.cleaned_data.get('title')

            )
            return redirect('/category/')
        return render(request, 'products/categories.html', context={'form': form})
