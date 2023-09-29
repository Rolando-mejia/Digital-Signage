from django.contrib import admin
from .models import Airline, StatusFlight, FlightDestination
from .models import Checkin, Gate

# Register your models here.
admin.site.register(Airline)
admin.site.register(StatusFlight)
admin.site.register(FlightDestination)

admin.site.register(Checkin)
admin.site.register(Gate)