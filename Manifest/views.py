from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response 

from rest_framework import viewsets
from .serializer import FlightManifestSerializer, AirlinesSerializer
from .models import FlightManifest, Airlines

## Vistas de Manifesto de Vuelo 
class FlightManifestView(viewsets.ModelViewSet):
    serializer_class = FlightManifestSerializer
    permission_classes = [IsAuthenticated]
    queryset = FlightManifest.objects.all()

class AirlinesView(viewsets.ModelViewSet):
    serializer_class = AirlinesSerializer
    permission_classes = [IsAuthenticated]
    queryset = Airlines.objects.all()