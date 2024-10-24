from django.contrib import admin
from .models import Bus, Seat, Route, Booking


class BusAdmin(admin.ModelAdmin):
    list_display = ("name", "route", "total_seats", "current_occupancy")


admin.site.register(Bus, BusAdmin)
admin.site.register(Seat)
admin.site.register(Route)
admin.site.register(Booking)
