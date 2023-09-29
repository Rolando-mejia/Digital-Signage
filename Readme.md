# BACKEND Digital Signage
 Backend para sistema de información de vuelos en Django con MySQL
 El sistema Corre en:
 Python 3.11.3
 Django 4.2.2 

# INCIAR PROYECTO
 En entorno local
 Crear entorno virtual a. Instalar entorno virtual $ pip install virtualenv
 b. Crear entorno virtual $ virtualenv venv o $ python -m venv venv

 c. Inicializar el entorno virtual (Windows) $ cd venv $ cd Scripts $ activate

  (Linux y Mac OS X)
  $ source bin/activate 

      Luego retornar a la carpeta raiz del proyecto
# Instalaciónes necesarias
 Instalar paquetes necesarios del proyecto con el comando $ pip install -r "requirements.txt"

 Nota: En caso que el comando no funcione abrir el archivo Requirements.txt del proyecto e instalar cada paquete

# Iniciar Proyecto
En el archivo settings.py colocar la dirección del servidor donde se creara la Base de Datos y las creedenciales

Crear Base de Datos mediante el comando $ python manage.py migrate

Instalar Pillow para generar las migraciones 
           $ pip install Pillow

Nota: En servidor o SO Ubuntu colocar la versión de python3

Crear un Super Usuario para acceder al panel admin del Backend $ python manage.py createsuperuser

# Autentificacion por TOKEN

1. pip install djangorestframework jwt.

2. metodo de autentificacion en settings.py.

3. agregar url y endpoint.

4. agregar permissions classes en las views.

# RUTAS DE API 

 ## Rutas para información de Vuelos de Llegadas en Pantallas FIDS

1. PARA VER INFORMACION "GET" 
      http://127.0.0.1:8000/api/arrivalsInfo/  
    
2. PARA EDITAR INFORMACION "PUT"   
      http://127.0.0.1:8000/api/arrivalsInfo/id/
      
3. PARA ELIMINAR INFORMACION "DELETE"   
      http://127.0.0.1:8000/api/arrivalsInfo/id/


 ## Rutas para información de Vuelos de Salidas en Pantallas FIDS

1. PARA VER INFORMACION "GET" 
      http://127.0.0.1:8000/api/departuresInfo/  
    
2. PARA EDITAR INFORMACION "PUT"   
      http://127.0.0.1:8000/api/departuresInfo/id/
      
3. PARA ELIMINAR INFORMACION "DELETE"   
      http://127.0.0.1:8000/api/departuresInfo/id/

 ## Rutas para Manifestos de Vuelo Manifest

1. PARA VER INFORMACION "GET" 
     http://127.0.0.1:8000/api/flightManifest/

2. PARA EDITAR INFORMACION "PUT"  
     http://127.0.0.1:8000/api/flightManifest/id/

3. PARA ELIMINAR INFORMACION "DELETE" 
     http://127.0.0.1:8000/api/flightManifest/id/

 ## Rutas para Counters

 ## CheckIn Counter

1. PARA VER INFORMACION "GET" 
     http://127.0.0.1:8000/api/Checkin/

2. PARA EDITAR INFORMACION "PUT"  
     http://127.0.0.1:8000/api/Checkin/id/

3. PARA ELIMINAR INFORMACION "DELETE" 
     http://127.0.0.1:8000/api/Checkin/id/

 ## Gates

1. PARA VER INFORMACION "GET" 
     http://127.0.0.1:8000/api/Gate/

2. PARA EDITAR INFORMACION "PUT"  
     http://127.0.0.1:8000/api/Gate/id/

3. PARA ELIMINAR INFORMACION "DELETE" 
     http://127.0.0.1:8000/api/Gate/id/


     
