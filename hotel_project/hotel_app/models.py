from django.db import models

class Guest(models.Model):
    registration_number = models.AutoField(primary_key=True)
    last_name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)

class Room(models.Model):
    room_number = models.AutoField(primary_key=True)
    room_count = models.IntegerField()
    floor = models.IntegerField()
    has_tv = models.BooleanField()
    has_fridge = models.BooleanField()
    capacity = models.IntegerField()
    category = models.CharField(max_length=50, choices=[('standard', 'Звичайний'), ('semi_luxury', 'Полу Люкс'), ('luxury', 'Люкс')])
    cost_per_night = models.DecimalField(max_digits=8, decimal_places=2)

class Registration(models.Model):
    registration_code = models.AutoField(primary_key=True)
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE)
    arrival_date = models.DateField()
    stay_duration = models.IntegerField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
