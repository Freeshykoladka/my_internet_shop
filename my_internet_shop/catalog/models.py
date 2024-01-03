from django.db import models

class Catalog(models.Model):
    name=models.CharField(max_length=255,unique=True)
    order = models.PositiveSmallIntegerField()
    is_visible = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'catalog'
        ordering = ('order',)

    
    
    def __str__(self):
        return f' {self.name}'
    