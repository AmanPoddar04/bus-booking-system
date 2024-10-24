from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("buses/", views.browse_buses, name="browse_buses"),
    path(
        "bus/<int:bus_id>/seats/",
        views.check_seat_availability,
        name="check_seat_availability",
    ),
    path("book/<int:seat_id>/", views.book_seat, name="book_seat"),
    path("cancel/<int:booking_id>/", views.cancel_booking, name="cancel_booking"),
]
