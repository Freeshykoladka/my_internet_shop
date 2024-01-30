from django.urls import path
from .views import ManagerIndex, EditPurchases

app_name = 'manager'


urlpatterns = [
    path('', ManagerIndex.as_view(), name='index'),
    path('purchases/<int:pk>/', EditPurchases.as_view(), name='edit_purchases'),
]