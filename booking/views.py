from django.shortcuts import render, get_object_or_404, redirect
from .models import Bus, Seat, Route, Booking
from django.contrib.auth.decorators import login_required
from .forms import BookingForm
from django.contrib import messages
from django.shortcuts import render
from .models import Booking
from django.contrib.auth import logout


@login_required(login_url="/accounts/google/login/")
def dashboard(request):
    user_bookings = (
        Booking.objects.filter(user=request.user)
        if request.user.is_authenticated
        else []
    )
    return render(request, "index.html", {"user_bookings": user_bookings})


@login_required
def browse_buses(request):
    source = request.GET.get("source")
    destination = request.GET.get("destination")
    sources = Route.objects.values_list("source", flat=True).distinct()
    destinations = Route.objects.values_list("destination", flat=True).distinct()
    buses = Bus.objects.filter(route__source=source, route__destination=destination)
    return render(
        request,
        "booking/browse_buses.html",
        {"buses": buses, "sources": sources, "destinations": destinations},
    )


@login_required
def check_seat_availability(request, bus_id):
    bus = get_object_or_404(Bus, id=bus_id)
    seats = Seat.objects.filter(bus=bus)
    return render(
        request, "booking/check_seat_availability.html", {"bus": bus, "seats": seats}
    )


@login_required
def book_seat(request, seat_id):
    seat = get_object_or_404(Seat, id=seat_id, is_booked=False)
    bus = seat.bus  # Get the bus associated with the seat
    user = request.user

    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.seat = seat
            seat.is_booked = True
            bus.current_occupancy += 1
            bus.save()

            seat.save()
            booking.save()

            return redirect("check_seat_availability", bus_id=bus.id)
    else:
        form = BookingForm(initial={"seat": seat.id})

    return render(request, "booking/book_seat.html", {"form": form, "seat": seat})


@login_required
def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    seat = booking.seat
    bus = seat.bus
    bus.current_occupancy -= 1
    bus.save()
    seat.is_booked = False
    seat.save()
    booking.delete()
    messages.success(request, "Your booking has been successfully canceled.")
    return redirect("dashboard")


@login_required
def custom_logout(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect("login")
