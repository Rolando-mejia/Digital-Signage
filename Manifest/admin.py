from django.contrib import admin
from .models import Airlines, FlightManifest

# Register your models here.
admin.site.register(Airlines)
admin.site.register(FlightManifest)
