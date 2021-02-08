from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.CharField(max_length=255, null=False, blank=False)

class Sport(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.CharField(max_length=255, null=False, blank=False)

class Customer(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    num_doc = models.CharField(max_length=50, null=False, blank=False)
    phone = models.CharField(max_length=20, null=True, blank=False)

class Product(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.CharField(max_length=255, null=False, blank=False)
    price = models.FloatField(null=False, blank=False)
