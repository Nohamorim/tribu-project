from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Cliente
from .serializers import ClienteSerializer, ClienteIdNomeSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

    @action(detail=False, methods=['get'], url_path='id.nome')
    def listar_id_nome(self, request):
        clientes = self.get_queryset()
        serializer = ClienteIdNomeSerializer(clientes, many=True)
        return Response(serializer.data)


    def list(self, request, *args, **kwargs):
        return Response("Listar todos os clientes")