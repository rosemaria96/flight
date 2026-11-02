from django.db import models

# Create your models here.
class Flight(models.Model):
    flight_no = models.CharField(max_length=100)
    source = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return self.flight_no


class Booking(models.Model):
    flight = models.ForeignKey(Flight, on_delete = models.CASCADE)
    passenger = models.CharField(max_length= 100)

    def __str__(self):
        return self.passenger

