from django.db import models


class Subscriptions(models.Model):

    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    price_per_box = models.DecimalField(max_digits=6, decimal_places=2)
    months = models.TextField()
    fruit = models.TextField()
    vegetables = models.TextField()
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name