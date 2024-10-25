# Django Bus Booking System

A Django-based bus booking system that allows users to browse and book bus tickets, view schedules, and manage bookings. The admin panel provides functionality to manage buses, routes, schedules, and users. The complete project documentation is available in the PDF file included in this repository. You can find it

## Features

- User registration and authentication
- Browse available buses and routes
- Search for buses by source, destination, and date
- Book bus tickets and view past bookings
- Manage and cancel bookings
- Admin panel for managing:
  - Buses
  - Routes
  - Schedules
  - Users

## Requirements

- Python 3.x
- Django 3.x or higher
- PostgreSQL or SQLite (for development)
- Other dependencies listed in `requirements.txt`

## Setup and Installation

Follow these steps to set up and run the project on your local machine.

### 1. Clone the repository

```bash
git clone https://github.com/AmanPoddar04/bus-booking-system
cd bus-booking-system
```

### 2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate   # On Windows use `venv\Scripts\activate`
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Create a ```.env``` file
Create a .env file in the root directory and add the following environment variables:
```bash
CLIENT_ID=your_client_id_here
CLIENT_SECRET=your_client_secret_here
```

### 5. Set up the database
By default, the project is configured to use SQLite. You can also configure PostgreSQL or another database in settings.py.
```bash
python manage.py migrate
```

### 6. Create a superuser for admin panel
```bash
python manage.py createsuperuser
```

### 7. Run the development server
```
python manage.py runserver
```

Now you can access the project at http://127.0.0.1:8000/.




## Models Involved

### 1. **Route**
Represents the route a bus will travel on.

| Field            | Type               | Description                           |
|------------------|--------------------|---------------------------------------|
| `source`         | CharField          | Starting location (max 100 characters). |
| `destination`    | CharField          | Ending location (max 100 characters). |
| `distance`       | FloatField         | Distance between source and destination (in kilometers). |
| `estimated_time` | DurationField      | Estimated time of travel (as a duration in hours). |

**Methods:**
- `__str__`: Returns a string representing the route as "source to destination".

---

### 2. **Bus**
Represents a bus that operates on a particular route.

| Field              | Type               | Description                             |
|--------------------|--------------------|-----------------------------------------|
| `name`             | CharField          | Name of the bus (max 100 characters).   |
| `total_seats`      | IntegerField       | Total number of seats available.        |
| `current_occupancy`| IntegerField       | Current number of occupied seats.       |
| `days_of_operation`| CharField          | Days of operation (e.g., 'Mon, Tue').   |
| `route`            | ForeignKey         | Foreign key to the `Route` model.       |

**Methods:**
- `available_seats`: Returns the number of available seats on the bus.
- `occupancy_percentage`: Returns the percentage of seats that are occupied.
- `__str__`: Returns the name of the bus.

---

### 3. **Seat**
Represents a seat within a bus.

| Field         | Type               | Description                          |
|---------------|--------------------|--------------------------------------|
| `bus`         | ForeignKey         | Foreign key to the `Bus` model.      |
| `seat_number` | CharField          | Seat number (max 5 characters).      |
| `is_booked`   | BooleanField       | Indicates whether the seat is booked.|

**Methods:**
- `__str__`: Returns the seat number along with the bus name (e.g., "BusName - Seat X").

---

### 4. **Booking**
Represents a booking made by a user for a particular seat.

| Field          | Type               | Description                          |
|----------------|--------------------|--------------------------------------|
| `user`         | ForeignKey         | Foreign key to the `User` model (Django's default). |
| `seat`         | OneToOneField      | One-to-one relation with the `Seat` model. |
| `booking_time` | DateTimeField      | Time when the booking was made (auto-set). |

**Methods:**
- `__str__`: Returns a string representing the booking as "Booking: username - seat_number".


