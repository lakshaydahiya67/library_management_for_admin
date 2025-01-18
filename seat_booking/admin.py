from django.contrib import admin
from .models import User, Seat, TimeSlot
# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'aadhar_number', 'address', 'phone_number']
    search_fields = ['name', 'aadhar_number', 'phone_number']
    list_filter = ['name', 'aadhar_number', 'phone_number']

@admin.register(Seat)
class SeatAdmin(admin.ModelAdmin):
    list_display = ['seat_number']
    search_fields = ['seat_number']
    list_filter = ['seat_number']

@admin.register(TimeSlot)
class TimeSlotAdmin(admin.ModelAdmin):
    list_display = ['seat', 'slot', 'is_booked', 'booked_by', 'booking_date', 'expiration_date']
    search_fields = ['seat', 'slot', 'is_booked', 'booked_by', 'booking_date', 'expiration_date']
    list_filter = ['seat', 'slot', 'is_booked', 'booked_by', 'booking_date', 'expiration_date']