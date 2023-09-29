from rest_framework import serializers
from django.contrib.auth.models import User
from .models import FlightManifest, Airlines

# Serializer para Manifestos de Vuelos 

class AirlinesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airlines
        fields = '__all__'
class FlightManifestSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlightManifest
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['idAirline'] = AirlinesSerializer(instance.idAirline).data

        return response

