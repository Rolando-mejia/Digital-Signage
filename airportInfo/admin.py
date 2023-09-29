from django.contrib import admin
from .models import AirportSystem
from .models import Airlines
from .models import Status
from .models import AirportFrom, Arrivals, Departures, AirCraftType
from .models import FlightType, Iata, GateNumber

# Register your models here.

admin.site.register(AirportSystem)
admin.site.register(Airlines)
admin.site.register(Status)
admin.site.register(AirportFrom)
admin.site.register(FlightType)
admin.site.register(Arrivals)
admin.site.register(Departures)
admin.site.register(AirCraftType)
admin.site.register(Iata)
admin.site.register(GateNumber)

#admin.site.register(TypePositions)
#admin.site.register(Position)

admin.site.site_header = "Digital Signage"
admin.site.site_title = "Admin Digital Signage"
admin.site.index_title = "Admin Digital Signage"