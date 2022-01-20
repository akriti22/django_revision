from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=20),
    price = models.DecimalField(default=99.99, max_digits=20, decimal_places=10),
    description = models.TextField(),
    created = models.DateTimeField(auto_now_add=True),
    modified = models.DateTimeField(auto_now=True),

    def __str__(self):
        return self.name

