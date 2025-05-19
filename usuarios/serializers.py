from rest_framework import serializers
from .models import Cliente

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'  # Isso inclui todos os campos do modelo Cliente

class ClienteFilterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id', 'nome']  # Inclui apenas os campos id e nome para o filtro
#SERIALIZERS filter