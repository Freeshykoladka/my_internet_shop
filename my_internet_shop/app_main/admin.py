from django.contrib import admin
from .models import CatalogItem

@admin.register(CatalogItem)
class MainMenuItemAdmin(admin.ModelAdmin):
    prepopulated_fields={"slug":("title",)}
    list_display=('title','slug','is_anchor','is_visible','order')
    list_editable=('is_anchor','is_visible','order')
    

