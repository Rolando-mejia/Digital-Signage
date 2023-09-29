import datetime as dt
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render
from django.http import JsonResponse
from django.utils import timezone

from rest_framework.decorators import api_view
from rest_framework.response import Response 

from rest_framework import viewsets
from .serializer import ArrivalsSerializer, DeparturesSerializer, AirportSystemSerializer, AirlinesSerializer, StatusSerializer, AirportFromSerializer, FlightTypeSerializer, AirCraftTypeSerializer, IataSerializer, GateNumberSerializer

from datetime import datetime, timedelta, date, time


from rest_framework.generics import ListAPIView

from .models import Arrivals, Departures, AirportSystem, Airlines, Status, AirportFrom, FlightType, AirCraftType, Iata, GateNumber


# Create your views here.
class AirportSystemView(viewsets.ModelViewSet):
    serializer_class = AirportSystemSerializer
    permission_classes = [IsAuthenticated]
    queryset = AirportSystem.objects.all()

class AirlinesView(viewsets.ModelViewSet):
    serializer_class = AirlinesSerializer
    permission_classes = [IsAuthenticated]
    queryset = Airlines.objects.all()

class StatusView(viewsets.ModelViewSet):
    serializer_class = StatusSerializer
    permission_classes = [IsAuthenticated]
    queryset = Status.objects.all()

class AirportFromView(viewsets.ModelViewSet):
    serializer_class = AirportFromSerializer
    permission_classes = [IsAuthenticated]
    queryset = AirportFrom.objects.all()

class FlightTypeView(viewsets.ModelViewSet):
    serializer_class = FlightTypeSerializer
    permission_classes = [IsAuthenticated]
    queryset = FlightType.objects.all()
 
class AirCraftTypeView(viewsets.ModelViewSet):
    serializer_class = AirCraftTypeSerializer
    permission_classes = [IsAuthenticated]
    queryset = AirCraftType.objects.all()

class IataView(viewsets.ModelViewSet):
    serializer_class = IataSerializer
    permission_classes = [IsAuthenticated]
    queryset = Iata.objects.all()

class GateNumberView(viewsets.ModelViewSet):
    serializer_class = GateNumberSerializer
    permission_classes = [IsAuthenticated]
    queryset = GateNumber.objects.all()


# View Principal de Informacion de Vuelos 
class ArrivalsView(viewsets.ModelViewSet):
    serializer_class = ArrivalsSerializer
    
    def get_queryset(self):
        # Obtener el valor del parámetro 'hora' desde la URL
        horas = self.request.query_params.get('hora')

        if horas is not None:
            try:
                horas_a_restar = int(horas)  # Convertir la cadena a un número entero
            except ValueError:
                # Si no se puede convertir a un número entero, devolver una lista vacía
                return Arrivals.objects.none()

            fecha_hoy = date.today()

            hora_fin = datetime.now() + timedelta(hours=horas_a_restar)
          
            hora_inicio =  datetime.now() - timedelta(hours=horas_a_restar)

            # Filtrar los registros según el rango de tiempo
            return Arrivals.objects.filter(ScheduledArrivals=fecha_hoy).filter(ScheduleTimeArrival__range=(hora_inicio, hora_fin))
     
        else:
            # Si no se proporciona el parámetro 'hora', devolver todos los registros
            return Arrivals.objects.all()
      
class DeparturesView(viewsets.ModelViewSet):
    serializer_class = DeparturesSerializer
    def get_queryset(self):
        # Obtener el valor del parámetro 'hora' desde la URL
        horas = self.request.query_params.get('hora')

        if horas is not None:
            try:
                horas_a_restar = int(horas)  # Convertir la cadena a un número entero
            except ValueError:
                # Si no se puede convertir a un número entero, devolver una lista vacía
                return Departures.objects.none()

            fecha_hoy = date.today()

            hora_fin = datetime.now() + timedelta(hours=horas_a_restar)
          
            hora_inicio =  datetime.now() - timedelta(hours=horas_a_restar)

            # Filtrar los registros según el rango de tiempo
            return Departures.objects.filter(ScheduledDepartures=fecha_hoy).filter(ScheduleTimeDepartures__range=(hora_inicio, hora_fin))
     
        else:
            # Si no se proporciona el parámetro 'hora', devolver todos los registros
            return Departures.objects.all()
