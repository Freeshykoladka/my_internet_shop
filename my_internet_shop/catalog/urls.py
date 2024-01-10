from django.urls import path
from . import views
from .views import IndexPage

app_name='shop'

urlpatterns = [
    path('', IndexPage.as_view(), name='home'),   
]

