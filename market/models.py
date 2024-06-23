# market/models.py
from django.db import models

class State(models.Model):
    name = models.CharField(max_length=255)

class District(models.Model):
    name = models.CharField(max_length=255)
    state = models.ForeignKey(State, on_delete=models.CASCADE)

class Commodity(models.Model):
    name = models.CharField(max_length=255)

class Market(models.Model):
    name = models.CharField(max_length=255)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

class Price(models.Model):
    market = models.ForeignKey(Market, on_delete=models.CASCADE)
    commodity = models.ForeignKey(Commodity, on_delete=models.CASCADE)
    price = models.IntegerField()
    date = models.DateField()
