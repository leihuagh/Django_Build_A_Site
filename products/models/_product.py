from django.db import models
from core.models import TimeStampModel


class Product(TimeStampModel):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=39.99)
    image = models.ImageField(upload_to='products/', blank=True, null=True)

    def __str__(self):
        return self.title
