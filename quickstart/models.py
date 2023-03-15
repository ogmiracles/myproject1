from django.db import models

# Create your models here.
class Model(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True
        
class Category(Model):
    title = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name_plural = 'Categories'

class Product(Model):
    title = models.CharField(max_length=255)
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', null=True)
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name_plural = 'Products'