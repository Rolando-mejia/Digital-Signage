from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Airline, StatusFlight, FlightDestination
from .models import Checkin, Gate, Airline, FlightDestination, StatusFlight

# Serializer para Counters
class AirlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airline
        fields = '__all__'

class StatusFlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusFlight
        fields = '__all__'

class FlightDestinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlightDestination
        fields = '__all__'

## Serializer para Checkin 
class CheckinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Checkin
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['idAirline'] = AirlineSerializer(instance.idAirline).data
        response['idFlightDestination'] = FlightDestinationSerializer(instance.idFlightDestination).data
        response['idStatusFlight'] = StatusFlightSerializer(instance.idStatusFlight).data

        return response

## Serializer para Gate
class GateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gate
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['idAirline'] = AirlineSerializer(instance.idAirline).data
        response['idFlightDestination'] = FlightDestinationSerializer(instance.idFlightDestination).data
        response['idStatusFlight'] = StatusFlightSerializer(instance.idStatusFlight).data
        
        return response