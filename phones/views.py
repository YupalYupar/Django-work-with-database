from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get('sort', '')
    pok = Phone.objects

    if sort == 'name':
        phones = pok.order_by("name")
    elif sort == 'max_price':
        phones = pok.order_by("-price")
    elif sort == 'min_price':
        phones = pok.order_by("price")
    else:
        phones = pok.all()

    context = {'phones': phones}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    context = {'phone': phone}
    return render(request, template, context)