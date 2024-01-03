from django.db import models


class Catalog(models.Model):
    name=models.CharField(max_length=255,unique=True)
    order = models.PositiveSmallIntegerField()
    is_visible = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'catalog'
        ordering = ('order',)

    
    def __iter__(self):
        products = self.products.filter(is_visible=True)
        for product in products:
            yield product
    
    def __str__(self):
        return f' {self.name}'
    

class Product(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='url')
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    photo = models.ImageField(upload_to='dishes/', blank=True)
    is_visible = models.BooleanField(default=True)
    order = models.PositiveSmallIntegerField()
    
    catalogs = models.ForeignKey(Catalog, on_delete=models.PROTECT, related_name='dishes')

    def __str__(self):
        return f' {self.name}'
    
    
    
    
    class Meta:
        verbose_name_plural = 'product'
        ordering = ('order',)
        constraints=[
              models.UniqueConstraint(fields=['order', 'catalogs'], name='unique_order_per_each_catalogs'),
         ]
        unique_together=['id','slug']