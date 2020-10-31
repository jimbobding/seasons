from django.db import models

# Create your models here.
class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)


class Season(models.Model):
    name = models.CharField(max_length=254)
    description = models.TextField(null=True, blank=True)
    fruit = models.TextField(null=True, blank=True)
    veg = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    month_1 = models.CharField(max_length=254,null=True, blank=True)
    month_2 = models.CharField(max_length=254,null=True, blank=True)
    month_3 = models.CharField(max_length=254,null=True, blank=True)

    def __str__(self):
        return self.name


class Boxes(models.Model):
    category = models.ForeignKey('Season', null=True, blank=True, on_delete=models.SET_NULL)
    box_name = models.CharField(max_length=254)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField(null=True, blank=True)
    size = models.CharField(max_length=254)
    fruit = models.TextField(null=True, blank=True)
    veg = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)

    def __str__(self):
        return self.box_name

