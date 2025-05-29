from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.http import HttpResponse
from rest_framework import routers
from usuarios import views

# Importações do drf-spectacular
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView,
)


# Define a view para a página inicial
def home(request):
    return HttpResponse("Bem-vindo à página inicial!")


# Configuração do router do DRF
router = routers.DefaultRouter()
router.register("clientes", views.ClienteViewSet, basename="cliente")

# Configuração das URLs do projeto Django
urlpatterns = [
    path("", home, name="home"),  # Melhor mapear a view home na raiz
    path("Cadastro/", include(router.urls)),  # Inclui as URLs do DRF
    path("api-auth/", include("rest_framework.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("admin/", admin.site.urls),
    # Schema da API em JSON
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    # Documentação Swagger UI
    path(
        "swagger/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"
    ),
    # Documentação Redoc (opcional)
    path("redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
]
