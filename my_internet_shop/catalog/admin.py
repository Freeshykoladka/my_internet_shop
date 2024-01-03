from django.contrib import admin
from .models import Catalog
from .models import  Product


admin.site.register(Catalog)

admin.site.register(Product)

