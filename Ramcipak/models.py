from django.db import models


# Create your models here.
class Categories(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(max_length=100, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=200, blank=True)
    category_id = models.ForeignKey(Categories, on_delete=models.SET_NULL, null=True)
    price = models.FloatField(max_length=50)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

