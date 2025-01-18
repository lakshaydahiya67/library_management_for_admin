from django.contrib import admin
from .models import User, Seat, TimeSlot

# Register your models here.

# Admin configuration for User model
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    # Fields to display in the admin list view
    list_display = ['name', 'aadhar_number', 'address', 'phone_number']
    # Fields to search in the admin search bar
    search_fields = ['name', 'aadhar_number', 'phone_number']
    # Fields to filter in the admin filter sidebar
    list_filter = ['name', 'aadhar_number', 'phone_number']

# Admin configuration for Seat model
@admin.register(Seat)
class SeatAdmin(admin.ModelAdmin):
    # Fields to display in the admin list view
    list_display = ['seat_number']
    # Fields to search in the admin search bar
    search_fields = ['seat_number']
    # Fields to filter in the admin filter sidebar
    list_filter = ['seat_number']

# Admin configuration for TimeSlot model
@admin.register(TimeSlot)
class TimeSlotAdmin(admin.ModelAdmin):
    # Fields to display in the admin list view
    list_display = ['seat', 'slot', 'is_booked', 'booked_by', 'booking_date', 'expiration_date']
    # Fields to search in the admin search bar
    search_fields = ['seat', 'slot', 'is_booked', 'booked_by', 'booking_date', 'expiration_date']
    # Fields to filter in the admin filter sidebar
    list_filter = ['seat', 'slot', 'is_booked', 'booked_by', 'booking_date', 'expiration_date']