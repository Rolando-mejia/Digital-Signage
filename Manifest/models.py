from django.db import models

# Create your models here.
class Airlines(models.Model):
    idAirline = models.BigAutoField(db_column='idAirline', 
                                    primary_key=True,
                                    )
    
    nombreAirline = models.CharField(db_column='nombreAirline', 
                                     unique=True,
                                     max_length=255,
                                     verbose_name='Nombre de la Aerolinea',
                                     )

    def __str__(self):
        fila = self.nombreAirline
        return fila
    
###################################################################################################################
                                 #Tablas de Manifestos de Vuelo#
###################################################################################################################
class FlightManifest(models.Model):
    idFlightManifest = models.BigAutoField(db_column='idFlightManifest',
                                    primary_key=True,
                                    )   
    
    idAirline = models.ForeignKey(Airlines,
                                models.DO_NOTHING,
                                db_column='nombreAirline',
                                verbose_name='Nombre de la Aerolinea',
                                )
    
    OperatorCode = models.CharField(db_column='OperatorCode',
                                  max_length=255,
                                  verbose_name='Codigo de Operador',
                                 )
    
    Date = models.DateField(null=True,
                                    blank=True,
                                    verbose_name="Fecha de guardado",
                                    )
    
    Matricula = models.CharField(db_column='Matricula',
                                  max_length=255,
                                  verbose_name='Matricula de Aeronave',
                                 )
    
    numeroVuelo = models.CharField(db_column='numeroVuelo',
                                  max_length=255,
                                  verbose_name='Numero de Vuelo',
                                 )
    
    tipoAeroNave = models.CharField(db_column='tipoAeroNave',
                                  max_length=255,
                                  verbose_name='Tipo de AeroNave',
                                 )
    
    llegadas = models.TimeField(null=True,
                                    blank=True,
                                    verbose_name="Fecha de Llegada",
                                    )
    
    salidas = models.TimeField(null=True,
                                    blank=True,
                                    verbose_name="Fecha de Salida",
                                    )
    
    destino = models.CharField(db_column='destino',
                                  max_length=255,
                                  verbose_name='Destino',
                                 )
    
    codigoATO = models.CharField(db_column='codigoATO',
                                  max_length=255,
                                  verbose_name='codigo ATO',
                                 )
    
    nombreATO = models.CharField(db_column='nombreATO',
                                  max_length=255,
                                  verbose_name='nombre ATO',
                                 )
    
    totalPax = models.IntegerField(max_length=255, 
                                   blank=True, 
                                   null=True
                                   )
    
    paxExen = models.IntegerField(max_length=255)

    inf = models.IntegerField(max_length=255)

    collect = models.IntegerField(max_length=255)

    terceraEdad = models.IntegerField(max_length=255)

    paxCargados = models.IntegerField(max_length=255)

    comentarios =  models.CharField(db_column='comentarios',
                                  max_length=255,
                                  verbose_name='comentarios',
                                 )
    def __str__(self):
        fila = self.Matricula
        return fila