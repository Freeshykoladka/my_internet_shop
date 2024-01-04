from django.shortcuts import render
from .models import Product, Catalog

# Create your views here.
def main(request):
    catalog = Catalog.objects.filter(is_visible=True)
    context = {
         'catalogs': catalog,
     }
    return render(request, 'index.html', context=context)
