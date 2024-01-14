from django.urls import path
from . import views
from .views import IndexPage, ProductsPage
from .views import AboutPage, ContactPage

app_name='shop'

urlpatterns = [
    path('', IndexPage.as_view(), name='home'),
    path('products/',ProductsPage.as_view(), name='products'),
    path('about us/',AboutPage.as_view(), name='about'),
    path('contact/',ContactPage.as_view(), name='contact'),
    ]

