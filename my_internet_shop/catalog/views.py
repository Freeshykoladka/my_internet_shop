from django.shortcuts import render,redirect
from .models import Product, Catalog
from django.views.generic import TemplateView
from .forms import OrderForm
from django.contrib import messages
from django.shortcuts import render
from app_main.models import CatalogItem

class IndexPage(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')

class ProductsPage(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, 'products.html')

class AboutPage(TemplateView):
  def get(self, request, *args, **kwargs):
        return render(request, 'about.html')

class ContactPage(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, 'contact.html')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        catalogs= Catalog.objects.filter(is_visible=True)
        context['catalogs'] = catalogs
        context['order_form'] = OrderForm()
        return context

    def post(self, request,*args, **kwargs):
        order_form = OrderForm(self.request.POST)

        if order_form.is_valid():
            order_form(request,'Reservation done')
            return redirect('shop:home')
        
        context = self.get_context_data(**kwargs)
        context['order_form'] = OrderForm()
        messages.error(request,'Errors in form Payment')
        return render(request,'index.html',context=context)
    

def index(request):
    catalog_items = CatalogItem.objects.all()  
    return render(request, 'index.html', {'catalog_items': catalog_items})

