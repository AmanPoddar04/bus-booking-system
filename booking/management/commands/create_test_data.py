from django.core.management.base import BaseCommand
from booking.models import Bus, Seat, Route
from datetime import timedelta


class Command(BaseCommand):
    help = "Creates test buses, routes, and seats"

    def handle(self, *args, **kwargs):
        # Create Route instances
        route1 = Route.objects.create(
            source="City A",
            destination="City B",
            distance=120.5,  # Distance in km (float field)
            estimated_time=timedelta(
                hours=2, minutes=30
            ),  # Duration field using timedelta
        )

        route2 = Route.objects.create(
            source="City C",
            destination="City D",
            distance=220.0,  # Distance in km (float field)
            estimated_time=timedelta(
                hours=4, minutes=45
            ),  # Duration field using timedelta
        )

        # Create Bus instances for route1
        bus1 = Bus.objects.create(
            name="Express Bus A1",
            total_seats=50,
            current_occupancy=0,  # Starts empty
            days_of_operation="Mon, Wed, Fri",  # Days of operation
            route=route1,
        )

        bus2 = Bus.objects.create(
            name="Express Bus A2",
            total_seats=40,
            current_occupancy=0,
            days_of_operation="Tue, Thu, Sat",
            route=route1,
        )

        # Create Bus instances for route2
        bus3 = Bus.objects.create(
            name="Express Bus C1",
            total_seats=60,
            current_occupancy=0,
            days_of_operation="Mon, Tue, Wed, Thu, Fri",
            route=route2,
        )

        # Create Seat instances for each bus
        for bus in [bus1, bus2, bus3]:
            for i in range(1, bus.total_seats + 1):
                seat_number = f"{i}"
                Seat.objects.create(bus=bus, seat_number=seat_number, is_booked=False)

        self.stdout.write(
            self.style.SUCCESS(
                "Test buses, routes, and seats have been created successfully!"
            )
        )
