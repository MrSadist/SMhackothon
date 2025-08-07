from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    

class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    total = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    
    def __str__(self):
        return self.title
    

class Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    
    def __str__(self):
        return self.product.title
    
    
class Video(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    video = models.FileField(upload_to='videos/')
    
    def __str__(self):
        return self.product.title