from django.urls import path
from . import views
from .views import IndexPage, ProductsPage, PurchaseView, AboutPage, ContactPage, ProductCategoryPage

app_name = 'shop'

urlpatterns = [
    path('', IndexPage.as_view(), name='home'),
    path('products/', ProductsPage.as_view(), name='products'),
    path('about_us/', AboutPage.as_view(), name='about'),
    path('contact/', ContactPage.as_view(), name='contact'),
    path('products/<str:category>/', ProductCategoryPage.as_view(), name='products_category'),
    path('purchase/<int:product_id>/', PurchaseView.as_view(), name='purchase'),
]

    
