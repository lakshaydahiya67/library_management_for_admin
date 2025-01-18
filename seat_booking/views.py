from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.utils.timezone import now
from .models import Seat, TimeSlot, User
from .forms import BookingForm
from django.contrib import messages

class HomePageView(View):
    """Displays all seats with time slots and their statuses on the homepage."""

    def get(self, request):
        # Fetch all seats along with their associated time slots
        seats = Seat.objects.prefetch_related('time_slots')
        # Render the homepage with the seats data
        return render(request, 'home.html', {'seats': seats})


class BookSlotView(View):
    """Handles booking of a specific time slot."""

    def get(self, request, slot_id):
        # Fetch the time slot by its ID or return a 404 error if not found
        slot = get_object_or_404(TimeSlot, pk=slot_id)
        if slot.is_booked:
            # If the slot is already booked, show the details of the user who booked it
            return render(request, 'slot_details.html', {'slot': slot})
        else:
            # If the slot is available, show the booking form
            form = BookingForm()
            return render(request, 'book_slot.html', {'form': form, 'slot': slot})

    def post(self, request, slot_id):
        # Fetch the time slot by its ID or return a 404 error if not found
        slot = get_object_or_404(TimeSlot, pk=slot_id)
        if slot.is_booked:
            # If the slot is already booked, show an error message and redirect to the homepage
            messages.error(request, "Slot is already booked!")
            return redirect('home')

        # Process the booking form data
        form = BookingForm(request.POST)
        if form.is_valid():
            # Save the user form data
            user = form.save()
            # Book the slot for the user
            slot.book_slot(user)
            # Show a success message and redirect to the homepage
            messages.success(request, f"Slot {slot.slot} booked successfully!")
            return redirect('home')
        # If the form is not valid, re-render the booking form with errors
        return render(request, 'book_slot.html', {'form': form, 'slot': slot})