from pyexpat import model 
from django.db import models

# Create your models here.
class Airline(models.Model):
    idAirline = models.BigAutoField(db_column='idAirline', 
                                    primary_key=True,
                                    )
    
    nombreAirline = models.CharField(db_column='nombreAirline', 
                                     unique=True,
                                     max_length=255,
                                     verbose_name='Nombre de la Aerolinea',
                                     )
    logoAirline = models.ImageField(upload_to='airlinesChck/',blank=True,null=True)

    def __str__(self):
        fila = self.nombreAirline
        return fila
    
class StatusFlight(models.Model):
    idStatusFlight = models.BigAutoField(db_column='idStatusFlight', 
                                    primary_key=True,
                                    )
    nombreStatusFlight = models.CharField(db_column='nombreStatusFlight', 
                                     unique=True,
                                     max_length=255,
                                     verbose_name='Estado del Vuelo',
                                     )
    def __str__(self):
        fila = self.nombreStatusFlight
        return fila
    
class FlightDestination(models.Model):
    idFlightDestination = models.BigAutoField(db_column='idFlightDestination', 
                                    primary_key=True,
                                    )
    nombreFlightDestination = models.CharField(db_column='nombreFlightDestination', 
                                     unique=True,
                                     max_length=255,
                                     verbose_name='Destino del Vuelo',
                                     )
    def __str__(self):
        fila = self.nombreFlightDestination
        return fila

############################################################################################################
                                ## Tabla para CheckIn Counter ##
###########################################################################################################
class Checkin(models.Model):
    idCheckIn = models.BigAutoField(db_column='idCheckIn',
                                    primary_key=True,
                                    )
    CheckinNumber = models.CharField(max_length=50, unique=True)

    idAirline = models.ForeignKey(Airline,
                                        models.DO_NOTHING,
                                        db_column='nombreAirline',
                                        verbose_name='Aerolinea',
                                        )

    FlightNumber = models.CharField(max_length=100)

    idFlightDestination = models.ForeignKey(FlightDestination,
                                        models.DO_NOTHING,
                                        db_column='nombreFlightDestination',
                                        verbose_name='Destino del Vuelo',
                                        )
    
    idStatusFlight = models.ForeignKey(StatusFlight,
                                        models.DO_NOTHING,
                                        db_column='nombreStatusFlight',
                                        verbose_name='Estado del Vuelo',
                                        )
    
    StatusDisplay = models.BooleanField(default=False)
    
    def __str__(self):
        fila =  "Numero de Checkin: " + self.CheckinNumber + " | Numero de Vuelo: " + self.FlightNumber
        return fila
    
############################################################################################################
                                ## Tabla para Gate ##
###########################################################################################################
class Gate(models.Model):
    idGate = models.BigAutoField(db_column='idGate',
                                    primary_key=True,
                                    )
    GateNumber = models.CharField(max_length=100, unique=True)

    idAirline = models.ForeignKey(Airline,
                                        models.DO_NOTHING,
                                        db_column='nombreAirline',
                                        verbose_name='Aerolinea',
                                        )

    FlightNumber = models.CharField(max_length=100)

    idFlightDestination = models.ForeignKey(FlightDestination,
                                        models.DO_NOTHING,
                                        db_column='nombreFlightDestination',
                                        verbose_name='Destino del Vuelo',
                                        )
    
    idStatusFlight = models.ForeignKey(StatusFlight,
                                        models.DO_NOTHING,
                                        db_column='nombreStatusFlight',
                                        verbose_name='Estado del Vuelo',
                                        )
    
    StatusDisplay = models.BooleanField(default=False)
    
    def __str__(self):
        fila = "Numero de Gate: " + self.GateNumber + " | Numero de Vuelo: " + self.FlightNumber
        return fila