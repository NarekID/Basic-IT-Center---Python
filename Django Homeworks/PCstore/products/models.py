from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=75, unique_for_date='registered_date')
    category = models.CharField(max_length=75)
    price = models.DecimalField(decimal_places=2, max_digits=8)
    details = models.TextField()
    owner = models.CharField(max_length=50)
    registered_date = models.DateTimeField(default=timezone.now)

    def get_absolute_url(self):
        return reverse('products:product_detail', args=[self.category,
                                                        self.owner,
                                                        self.slug])

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name + ' ' + str(self.price) + '$'
