from django.db import models


class User(models.Model):
    login = models.CharField(max_length=50)
    password = models.CharField(max_length=100)


class Country(models.Model):
    name = models.CharField(max_length=100)


class Town(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)


class ParkingLot(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=150)
    capacity = models.IntegerField()
    actualparkedcars = models.IntegerField(default=0)
    town = models.ForeignKey(Town, on_delete=models.CASCADE)


class Photo(models.Model):
    photo = models.CharField(max_length=100)
    parkinglot = models.ForeignKey(ParkingLot, on_delete=models.CASCADE)


class FavouriteParkingLot(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    parkinglot = models.ForeignKey(ParkingLot, on_delete=models.CASCADE)


class OldCapacityData(models.Model):
    parkedcars = models.IntegerField()
    date = models.DateTimeField(auto_now=True)
    parkinglot = models.ForeignKey(ParkingLot, on_delete=models.CASCADE)
