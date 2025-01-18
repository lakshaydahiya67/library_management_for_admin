from django.db import models
from datetime import timedelta
from django.utils.timezone import now

class User(models.Model):
    name = models.CharField(max_length=255)
    aadhar_number = models.CharField(max_length=12, unique=True)
    address = models.TextField()
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class Seat(models.Model):
    seat_number = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return f"Seat {self.seat_number}"


class TimeSlot(models.Model):
    SLOT_CHOICES = [
        ('8AM-4PM', '8AM-4PM'),
        ('4PM-12AM', '4PM-12AM'),
        ('12AM-8AM', '12AM-8AM'),
    ]

    seat = models.ForeignKey(Seat, on_delete=models.CASCADE, related_name="time_slots")
    slot = models.CharField(max_length=20, choices=SLOT_CHOICES)
    is_booked = models.BooleanField(default=False)
    booked_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    booking_date = models.DateTimeField(null=True, blank=True)  # When the slot was booked
    expiration_date = models.DateTimeField(null=True, blank=True)  # When the booking expires

    def __str__(self):
        return f"{self.slot} - {self.seat.seat_number}"

    def book_slot(self, user):
        """Book the slot for 30 days and set the expiration date."""
        self.is_booked = True
        self.booked_by = user
        self.booking_date = now()
        self.expiration_date = now() + timedelta(days=30)
        self.save()

    def check_expiration(self):
        """Reset the slot if it is expired."""
        if self.expiration_date and now() > self.expiration_date:
            self.is_booked = False
            self.booked_by = None
            self.booking_date = None
            self.expiration_date = None
            self.save()