from django.db import models

# Create your models here.


class Produk(models.Model):
    title = models.CharField(max_length=100)


class Supplier(models.Model):
    title = models.CharField(max_length=100)


class Stok(models.Model):
    gudangId = models.ForeignKey
