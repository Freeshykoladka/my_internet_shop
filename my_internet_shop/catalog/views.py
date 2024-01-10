from django.shortcuts import render,redirect
from .models import Product, Catalog
from django.views.generic import TemplateView
from .forms import OrderForm
from django.contrib import messages

class IndexPage(TemplateView):
    template_name = 'shop_main.html'

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
            return redirect('catalog:home')
        
        context = self.get_context_data(**kwargs)
        context['order_form'] = OrderForm()
        messages.error(request,'Errors in form Payment')
        return render(request,'shop_main.html',context=context)
    
    