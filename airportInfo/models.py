from django.db import models

# Create your models here.

#####################################################################################################
                                        ## TABLAS GENERALES ##
#####################################################################################################

# Tabla Para Aeropuertos
class AirportSystem(models.Model):
    idAirportSystem = models.BigAutoField(db_column='idAirportSystem',
                                    primary_key=True,
                                    )
    
    nombreAirport = models.CharField(db_column='nombreAirport',
                              unique=True,
                              max_length=255,
                              verbose_name='Nombre del sistema para Aeropuerto',
                              )
    
    logoAirportSystem = models.ImageField(upload_to='airports/',blank=True,null=True)

    def __str__(self):
        fila = self.nombreAirport
        return fila
    
    # Tabla Para Aerolineas
class Airlines(models.Model):
    idAirline = models.BigAutoField(db_column='idAirline', 
                                    primary_key=True,
                                    )
    
    nombreAirline = models.CharField(db_column='nombreAirline', 
                                     unique=True,
                                     max_length=255,
                                     verbose_name='Nombre de la Aerolinea',
                                     )
    logoAirline = models.ImageField(upload_to='airlines/',blank=True,null=True)

    def __str__(self):
        fila = self.nombreAirline
        return fila
    
# Tabla para Estado de vuelos
class Status(models.Model):
    idStatus = models.BigAutoField(db_column='idStatus',
                                    primary_key=True,
                                    )
    
    nombreStatus = models.CharField(db_column='nombreStatus',
                              unique=True,
                              max_length=255,
                              verbose_name='Status del vuelo',
                              )
    def __str__(self):
        fila = self.nombreStatus
        return fila
    
class AirportFrom(models.Model):
    idAirportFrom = models.BigAutoField(db_column='idAirportFrom',
                                    primary_key=True,
                                    )
    
    nombreAirportFrom = models.CharField(db_column='nombreAirportFrom',
                              unique=True,
                              max_length=255,
                              verbose_name='nombre de la ciudad proveniente',
                              )
    def __str__(self):
        fila = self.nombreAirportFrom
        return fila
    
class FlightType(models.Model):
    idFlightType = models.BigAutoField(db_column='idFlightType',
                                    primary_key=True,
                                    )
    
    nombreFlightType = models.CharField(db_column='nombreFlightType',
                              unique=True,
                              max_length=255,
                              verbose_name='tipo de vuelo',
                              )
    def __str__(self):
        fila = self.nombreFlightType
        return fila
    
class AirCraftType(models.Model):
    idAirCraftType = models.BigAutoField(db_column='idAirCraftType',
                                    primary_key=True,
                                    )
    
    nombreAirCraftType = models.CharField(db_column='nombreAirCraftType',
                              unique=True,
                              max_length=255,
                              verbose_name='Tipo de Aeronave',
                              )
    def __str__(self):
        fila = self.nombreAirCraftType
        return fila
    
class Iata(models.Model):
    idIata = models.BigAutoField(db_column='idIata',
                                    primary_key=True,
                                    )
    
    nombreIata = models.CharField(db_column='nombreIata',
                              unique=True,
                              max_length=25,
                              verbose_name='Codigo IATA',
                              )
    def __str__(self):
        fila = self.nombreIata
        return fila

class GateNumber(models.Model):
    idGateNumber = models.BigAutoField(db_column='idIata',
                                    primary_key=True,
                                    )
    
    nombreGateNumber = models.CharField(db_column='nombreGateNumber',
                              unique=True,
                              max_length=100,
                              verbose_name='Numero de Gate',
                              )
    def __str__(self):
        fila = self.nombreGateNumber
        return fila  

# TABLA CON FORANEAS

class Arrivals(models.Model):
    
    idArrivals = models.BigAutoField(db_column='idArrivals',
                                    primary_key=True,
                                    )
    
    idAirline = models.ForeignKey(Airlines,
                                        models.DO_NOTHING,
                                        db_column='nombreAirline',
                                        verbose_name='nombre de la Aerolinea',
                                        ) 

    idAirport = models.ForeignKey(AirportSystem,
                                        models.DO_NOTHING,
                                        db_column='nombreAirport',
                                        verbose_name='nombre del sistema para aeropuerto',
                                        ) 
    
    FlightCode = models.CharField(db_column='FlightCode',
                                  max_length=255,
                                  verbose_name='codigo de vuelo',
                                 )
    
    idIata = models.ForeignKey(Iata,
                                models.DO_NOTHING,
                                db_column='nombreIata',
                                verbose_name='Codigo IATA',
                                )
     
    idAirCraftType = models.ForeignKey(AirCraftType,
                                        models.DO_NOTHING,
                                        db_column='nombreAirCraftType',
                                        verbose_name='Tipo de aeronave',
                                        ) 
    
    idAirportFrom = models.ForeignKey(AirportFrom,
                                        models.DO_NOTHING,
                                        db_column='nombreAirportFrom',
                                        verbose_name='nombre de la ciudad proveniente',
                                        ) 
    # Fecha de Llegada de vuelo
    ScheduledArrivals = models.DateField(null=True,
                                    blank=True,
                                    verbose_name="Fecha de llegada programada",)
    
    # Fecha estimada de Llegada
    EstimatedArrivals = models.DateField(null=True,
                                    blank=True,
                                    verbose_name="Fecha de llegada estimada",)
    
    # Hora de Llegada
    ScheduleTimeArrival = models.TimeField(null=True,
                                    blank=True,
                                    verbose_name="Hora programada de llegada",)

    #Hora estimada de Llegada
    EstimatedTimeArrival = models.TimeField(null=True,
                                    blank=True,
                                    verbose_name="Hora estimada de llegada",)
    
    idStatus = models.ForeignKey(Status,
                                models.DO_NOTHING,
                                db_column='idStatus',
                                verbose_name='Estado del Vuelo',
                                ) 
    def __str__(self):
        fila = "Numero de Vuelo: " + self.FlightCode + " | IATA: " + self.idIata.nombreIata 
        return fila 

    # Para ordenar los vuelos por Fecha y Hora 
    class Meta:
       db_table = 'airportinfo_arrivals'
       ordering = ['ScheduledArrivals','ScheduleTimeArrival']
 
    

class Departures(models.Model):
    
    idDepartures = models.BigAutoField(db_column='idDepartures',
                                    primary_key=True,
                                    )
    
    idAirline = models.ForeignKey(Airlines,
                                        models.DO_NOTHING,
                                        db_column='nombreAirline',
                                        verbose_name='nombre de la Aerolinea',
                                        ) 

    idAirport = models.ForeignKey(AirportSystem,
                                        models.DO_NOTHING,
                                        db_column='nombreAirport',
                                        verbose_name='nombre del sistema para aeropuerto',
                                        ) 
    
    FlightCode = models.CharField(db_column='FlightCode',
                                  max_length=255,
                                  verbose_name='codigo de vuelo',
                                 )
    
    idIata = models.ForeignKey(Iata,
                                models.DO_NOTHING,
                                db_column='nombreIata',
                                verbose_name='Codigo IATA',
                                )
     
    idAirCraftType = models.ForeignKey(AirCraftType,
                                        models.DO_NOTHING,
                                        db_column='nombreAirCraftType',
                                        verbose_name='Tipo de aeronave',
                                        ) 
    
    idAirportFrom = models.ForeignKey(AirportFrom,
                                        models.DO_NOTHING,
                                        db_column='nombreAirportFrom',
                                        verbose_name='nombre de la ciudad proveniente',
                                        ) 
    # Fecha de Salida del vuelo
    ScheduledDepartures = models.DateField(null=True,
                                    blank=True,
                                    verbose_name="Fecha de salida programada",)
    
    #Fecha estimada de Salida
    EstimatedDepartures = models.DateField(null=True,
                                    blank=True,
                                    verbose_name="Fecha de salida estimada",)
    
    #Hora de Salida
    ScheduleTimeDepartures = models.TimeField(null=True,
                                    blank=True,
                                    verbose_name="Hora programada de salida",)
    
    # Hora estimada de Salida
    EstimatedTimeDepartures = models.TimeField(null=True,
                                    blank=True,
                                    verbose_name="Hora estimada de salida",)
    
    idGateNumber = models.ForeignKey(GateNumber,
                                models.DO_NOTHING,
                                db_column='nombreGateNumber',
                                verbose_name='Numero de Gate',
                                ) 
    
    idStatus = models.ForeignKey(Status,
                                models.DO_NOTHING,
                                db_column='idStatus',
                                verbose_name='Estado del Vuelo',
                                ) 
    
    def __str__(self):
        fila = "Numero de Vuelo: " + self.FlightCode + " | IATA: " + self.idIata.nombreIata 
        return fila 
    
    class Meta:
       db_table = 'airportinfo_departures'
       ordering = ['ScheduledDepartures','ScheduleTimeDepartures']
    

###################################################################################################################
                                 #Tablas de Gestion de Pantallas#
###################################################################################################################
# Tabla que almacena el Tipo de Posiciones
class TypePositions(models.Model):
    idTypePositions = models.BigAutoField(db_column='idTypePositions',
                                    primary_key=True,
                                    )
    
    nombreTypePositions = models.CharField(db_column='nombreTypePositions',
                              unique=True,
                              max_length=25,
                              verbose_name='Type Positions',
                              )
    def __str__(self):
        fila = self.nombreTypePositions
        return fila

class Position(models.Model):
    idPosition = models.BigAutoField(db_column='idPositions',
                                    primary_key=True,
                                    )
    
    nombrePosition = models.CharField(db_column='nombrePosition',
                              unique=True,
                              max_length=25,
                              verbose_name='Positions',
                              )
    
    tipo = models.ForeignKey(TypePositions,
                                models.DO_NOTHING,
                                db_column='nombreTypePositions',
                                verbose_name='Posiciones Asignadas',
                                )
    
    estatus = models.BooleanField(null=True, blank=True)


    def __str__(self):
        fila = self.nombrePosition
        return fila
