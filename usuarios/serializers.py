from rest_framework import serializers
from .models import Cliente

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'  # Isso inclui todos os campos do modelo Cliente

class ClienteIdNomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id', 'nome']  # Inclui apenas os campos id e nome

class ClienteFilterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id', 'nome']  # Inclui apenas os campos id e nome para o filtro

#class ClienteCreateSerializer(serializers.ModelSerializer):
#       model = Publicacao
#        fields = ['cliente', 'data_publicacao', 'conteudo']
#        extra_kwargs = {
#            'cliente': {'required': True},
#            'data_publicacao': {'required': True},
#            'conteudo': {'required': True}
#        }
#        read_only_fields = ['id']