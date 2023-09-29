from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework import routers
from counter import views

# api versioning
router = routers.DefaultRouter()
router.register(r'Checkin', views.CheckinView, 'Checkin')
router.register(r'Gate', views.GateView, 'Gate')
router.register(r'Airline', views.AirlineView, 'Airline')
router.register(r'FlightDestination', views.FlightDestinationView, 'FlightDestination')
router.register(r'StatusFlight', views.StatusFlightView, 'StatusFlight')



urlpatterns = [
    path("", include(router.urls)),
    path('docs/', include_docs_urls(title="counter API"))
]