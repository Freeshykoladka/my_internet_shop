from typing import Any
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse
from django.views.generic import ListView, UpdateView
from catalog.models import Order
from django.urls import reverse_lazy, reverse
from .forms import PurchasesEditForm


class ManagerAccessMixin(UserPassesTestMixin):

    def test_func(self):
        return self.request.user.groups.filter(name='manager')


class ManagerIndex(LoginRequiredMixin,ManagerAccessMixin , ListView):
    template_name = 'manager_index.html'
    login_url = '/login/'
    model = Order
    context_object_name = 'orders'

    def get_queryset(self):
        return Order.objects.filter(is_precessed= False)


class EditPurchases(LoginRequiredMixin, ManagerAccessMixin, UpdateView):
    template_name = 'edit_purchases.html'
    login_url = '/login/'
    model = Order
    form_class = PurchasesEditForm
    success_url = reverse_lazy('manager:index')