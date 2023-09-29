from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Arrivals, Departures, AirportSystem, Airlines, Status, AirportFrom, FlightType, AirCraftType, Iata, GateNumber

# SERIALIZER PARA TABLAS 
class AirportSystemSerializer(serializers.ModelSerializer):
    class Meta:
        model = AirportSystem
        fields = '__all__'

class AirlinesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airlines
        fields = '__all__'

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'

        
class AirportFromSerializer(serializers.ModelSerializer):
    class Meta:
        model = AirportFrom
        fields = '__all__'

class FlightTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlightType
        fields = '__all__'

class AirCraftTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AirCraftType
        fields = '__all__'

class IataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Iata
        fields = '__all__'

class GateNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = GateNumber
        fields = '__all__'

# SERIALIZER PARA TABLA PRINCIPAL DE VUELOS
class ArrivalsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Arrivals
        fields = '__all__'



# FUNCION PARA ENVIAR LLAVES FORANEAS EN EL JSON 
    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['idAirline'] = AirlinesSerializer(instance.idAirline).data
        response['idAirport'] = AirportSystemSerializer(instance.idAirport).data
        response['idIata'] = IataSerializer(instance.idIata).data
        response['idAirCraftType'] = AirCraftTypeSerializer(instance.idAirCraftType).data
        response['idAirportFrom'] = AirportFromSerializer(instance.idAirportFrom).data
        response['idStatus'] = StatusSerializer(instance.idStatus).data
        
        
        return response 
    
class DeparturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departures
        fields = '__all__'

# FUNCION PARA ENVIAR LLAVES FORANEAS EN EL JSON 
    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['idStatus'] = StatusSerializer(instance.idStatus).data
        response['idAirline'] = AirlinesSerializer(instance.idAirline).data
        response['idAirport'] = AirportSystemSerializer(instance.idAirport).data
        response['idIata'] = IataSerializer(instance.idIata).data
        response['idAirCraftType'] = AirCraftTypeSerializer(instance.idAirCraftType).data
        response['idAirportFrom'] = AirportFromSerializer(instance.idAirportFrom).data
        response['idGateNumber'] = GateNumberSerializer(instance.idGateNumber).data
        response['idStatus'] = StatusSerializer(instance.idStatus).data

        return response 
    