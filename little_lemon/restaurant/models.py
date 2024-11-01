from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name


class Booking(models.Model):
    customer_name = models.CharField(max_length=100)
    table_number = models.IntegerField()
    booking_time = models.DateTimeField()

    def __str__(self):
        return f"Booking for {self.customer_name} at table {self.table_number}"
