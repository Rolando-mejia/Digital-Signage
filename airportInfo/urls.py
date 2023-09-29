from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework import routers
from airportInfo import views

# api versioning
router = routers.DefaultRouter()
router.register(r'arrivalsInfo', views.ArrivalsView, 'Arrivals')
router.register(r'departuresInfo', views.DeparturesView, 'Departures')
router.register(r'airportSystem', views.AirportSystemView, 'AirportSystem')
router.register(r'status', views.StatusView, 'Status')
router.register(r'airportFrom', views.AirportFromView, 'AirportFrom')
router.register(r'flightType', views.FlightTypeView, 'FlightType')
router.register(r'aircraftType', views.AirCraftTypeView, 'AircraftType')
router.register(r'iata', views.IataView, 'iata')
router.register(r'gateNumber', views.GateNumberView, 'GateNumber')
router.register(r'airlines', views.AirlinesView, 'Airlines')




urlpatterns = [
    path("", include(router.urls)),
    path('docs/', include_docs_urls(title="airportInfo API"))
]