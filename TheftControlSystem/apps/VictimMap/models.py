from django.db import models


class Place(models.Model):
    latitude = models.DecimalField(max_digits=12, decimal_places=9, blank=True, null=True)
    longitude = models.DecimalField(max_digits=12, decimal_places=9, blank=True, null=True)


class Victim(models.Model):
    name = models.TextField(blank=True, null=True)
    phone = models.TextField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    place = models.ForeignKey(Place, blank=True, null=True)
    # intermediate_places = models.ManyToManyField(Place, blank=True, null=True)
