from .models import CatalogItem

def catalog_item(request):
    items = CatalogItem.objects.filter()
    return {'catalog_item': items}