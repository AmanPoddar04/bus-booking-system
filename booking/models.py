from django.db import models
from django.contrib.auth.models import User


class Route(models.Model):
    source = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    distance = models.FloatField()  # in km
    estimated_time = models.DurationField()  # ETA in hours

    def __str__(self):
        return f"{self.source} to {self.destination}"


class Bus(models.Model):
    name = models.CharField(max_length=100)
    total_seats = models.IntegerField()
    current_occupancy = models.IntegerField(default=0)
    days_of_operation = models.CharField(max_length=100)  # e.g., 'Mon, Tue, Wed'
    route = models.ForeignKey(Route, on_delete=models.CASCADE)

    def available_seats(self):
        return self.total_seats - self.current_occupancy

    def occupancy_percentage(self):
        return (self.current_occupancy / self.total_seats) * 100

    def __str__(self):
        return self.name


class Seat(models.Model):
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    seat_number = models.CharField(max_length=5)
    is_booked = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.bus.name} - Seat {self.seat_number}"


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    seat = models.OneToOneField(Seat, on_delete=models.CASCADE)
    booking_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking: {self.user.username} - {self.seat.seat_number}"
