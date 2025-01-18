from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.utils.timezone import now
from .models import Seat, TimeSlot, User
from .forms import BookingForm
from django.contrib import messages

class HomePageView(View):
    """Displays all seats with time slots and their statuses on the homepage."""

    def get(self, request):
        seats = Seat.objects.prefetch_related('time_slots')  # Fetch seats and their slots
        return render(request, 'home.html', {'seats': seats})


class BookSlotView(View):
    """Handles booking of a specific time slot."""

    def get(self, request, slot_id):
        slot = get_object_or_404(TimeSlot, pk=slot_id)
        if slot.is_booked:
            # Show details of the user who booked the slot
            return render(request, 'slot_details.html', {'slot': slot})
        else:
            # Show booking form for the available slot
            form = BookingForm()
            return render(request, 'book_slot.html', {'form': form, 'slot': slot})

    def post(self, request, slot_id):
        slot = get_object_or_404(TimeSlot, pk=slot_id)
        if slot.is_booked:
            messages.error(request, "Slot is already booked!")
            return redirect('home')

        form = BookingForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the user form data
            slot.book_slot(user)
            messages.success(request, f"Slot {slot.slot} booked successfully!")
            return redirect('home')
        return render(request, 'book_slot.html', {'form': form, 'slot': slot})