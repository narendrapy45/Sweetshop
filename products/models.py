from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.name

class ProductModel(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    image = models.FileField(upload_to="images/products_img",null=True)
    digital = models.BooleanField(default=False,null=True, blank=True)
    name = models.CharField(max_length=30, null=True)
    price = models.IntegerField(null=True)
    desc = models.TextField(null=True)

    def __str__(self):
        return self.category.name+"--"+self.name
