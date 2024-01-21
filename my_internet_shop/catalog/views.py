from django.shortcuts import render,redirect
from .models import Product, Catalog
from django.views.generic import TemplateView
from .forms import OrderForm
from django.contrib import messages
from django.shortcuts import render
from app_main.models import CatalogItem
from  django.http import HttpResponse


class IndexPage(TemplateView):
    template_name= 'index.html'

class ProductsPage(TemplateView):
    template_name = 'products.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['catalogs'] = Catalog.objects.all()
        context['products'] = Product.objects.exclude(catalogs__name='')
        return context

class ProductCategoryPage(TemplateView):
    template_name = 'page_content_products.html'

    def get_context_data(self, **kwargs):
        category_slug = self.kwargs['category']
        context = super().get_context_data(**kwargs)
        context['catalogs'] = Catalog.objects.all()
        context['products'] = Product.objects.filter(catalog__slug=category_slug, is_visible=True)
        return context
    
class AboutPage(TemplateView):
  template_name= 'about.html'

class ContactPage(TemplateView):
    template_name= 'contact.html'


class PurchaseView(TemplateView):
    template_name = 'purchase.html'
    
    def post(self, *args, **kwargs):
        order_form = OrderForm(self.request.POST)

        if order_form.is_valid():
            order_form.save()
            messages.success(self.request, 'Purchase done')
            return redirect('shop:home')  # Змінивши на потрібний маршрут
        else:
            # Виведення помилок форми для відлагодження
            print(order_form.errors)
            return HttpResponse("Помилка! Замовлення не було прийнято.")