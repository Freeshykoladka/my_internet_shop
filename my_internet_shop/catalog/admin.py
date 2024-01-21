from django.contrib import admin
from .models import Catalog, Product,Order
from django.utils.safestring import mark_safe



admin.site.register(Order)

admin.site.register(Catalog)





@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('id', 'catalogs', 'name', 'price', 'is_visible', 'photo_src_tag')
    list_editable = ('catalogs', 'name', 'price', 'is_visible')
    search_fields = ('name',)
    list_filter = ('catalogs', 'price', 'is_visible')
    actions = ['delete_selected']

    def photo_src_tag(self, obj):
        if obj.photo:
            return mark_safe(f"<img src='{obj.photo.url}' width=50>")

    photo_src_tag.short_description = 'Product photo'