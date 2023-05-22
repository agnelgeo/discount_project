from django.db import models
from django.utils.html import format_html

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='product_images')

    def display_image(self):
        return format_html('<img src="{}" width="50" height="50" />', self.image.url)

    def __str__(self):
        return self.name

