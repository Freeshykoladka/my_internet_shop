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
    photo = models.ImageField(upload_to='pohots/', blank=True)
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


class Gallery(models.Model):
    photo = models.ImageField(upload_to='gallery/')
    is_visible = models.BooleanField(default=True)
    title = models.CharField(max_length=255, blank=True)


class Order(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    credit_card_number = models.CharField(max_length=16)  
    expiration_date = models.CharField(max_length=5)  
    cvv = models.CharField(max_length=4)
    is_precessed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"Order #{self.pk} - {self.name}"
    
    class Meta:
        ordering = ('-created_at', )