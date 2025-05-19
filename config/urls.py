from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

# Configurações do Swagger
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Informações do Swagger
schema_view = get_schema_view(
   openapi.Info(
      title="API Tribu",
      default_version='v1',
      description="Controle de cadastro de usuários",
      terms_of_service="#",
      contact=openapi.Contact(email="myamorimads2023@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

def home(request):
    return HttpResponse("Bem-vindo à página inicial!")

urlpatterns = [
    path('', home),  # Rota para a raiz /
    path('admin/', admin.site.urls),
    path('api/', include('usuarios.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
