from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(request):
    return HttpResponse("Bem-vindo à página inicial!")

urlpatterns = [
    path('', home),  # Rota para a raiz /
    path('admin/', admin.site.urls),
    path('api/', include('usuarios.urls')),
]
