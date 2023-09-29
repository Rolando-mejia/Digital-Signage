from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response 

from rest_framework import viewsets
from .serializer import CheckinSerializer, GateSerializer, AirlineSerializer, FlightDestinationSerializer, StatusFlightSerializer
from .models import Checkin, Gate, Airline, FlightDestination, StatusFlight

## Vistas de Manifesto de Vuelo 
class CheckinView(viewsets.ModelViewSet):
    serializer_class = CheckinSerializer
    queryset = Checkin.objects.all()

class GateView(viewsets.ModelViewSet):
    serializer_class = GateSerializer
    queryset = Gate.objects.all()

class AirlineView(viewsets.ModelViewSet):
    serializer_class = AirlineSerializer
    permission_classes = [IsAuthenticated]
    queryset = Airline.objects.all()

class FlightDestinationView(viewsets.ModelViewSet):
    serializer_class = FlightDestinationSerializer
    permission_classes = [IsAuthenticated]
    queryset = FlightDestination.objects.all()

class StatusFlightView(viewsets.ModelViewSet):
    serializer_class = StatusFlightSerializer
    permission_classes = [IsAuthenticated]
    queryset = StatusFlight.objects.all()