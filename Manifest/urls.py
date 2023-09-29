from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework import routers
from Manifest import views

# api versioning
router = routers.DefaultRouter()
router.register(r'flightManifest', views.FlightManifestView, 'FlightManifest')
router.register(r'airlinesFM', views.AirlinesView, 'Airlines')


urlpatterns = [
    path("", include(router.urls)),
    path('docs/', include_docs_urls(title="Manifest API"))
]