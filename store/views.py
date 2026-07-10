from django.shortcuts import render
from .models import Product
from django.db.models import Q


def home(request):
    query = request.GET.get('search')

    if query:
        products = Product.objects.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query)
        )
    else:
        products = Product.objects.all()

    return render(request, 'store/home.html', {'products': products})

def product_detail(request, id):
    product = Product.objects.get(id=id)

    return render(request, 'store/product_detail.html', {
        'product': product
    })
