from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample
from drf_spectacular.types import OpenApiTypes

from .models import Cliente
from .serializers import ClienteSerializer, ClienteIdNomeSerializer


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

    @extend_schema(
        summary="Listar ID e Nome de todos os clientes",
        responses={200: ClienteIdNomeSerializer(many=True)},
    )
    @action(detail=False, methods=["get"], url_path="id-nome")
    def listar_id_nome(self, request):
        clientes = self.get_queryset()
        serializer = ClienteIdNomeSerializer(clientes, many=True)
        return Response(serializer.data)

    @extend_schema(
        tags=["Clientes"],
        summary="Filtrar clientes (exemplo)",
        parameters=[
            OpenApiParameter(
                name="nome",
                type=str,
                location=OpenApiParameter.QUERY,
                description="Filtra clientes pelo nome",
            )
        ],
        responses={200: OpenApiTypes.OBJECT},
    )
    @action(detail=False, methods=["get"], url_path="filtrar")
    def filtrar_clientes(self, request):
        # Aqui você pode usar request.query_params.get("nome"), por exemplo
        return Response("Filtrar clientes")

    @extend_schema(
        tags=["Clientes"],
        summary="Filtrar clientes por ID e Nome",
        parameters=[
            OpenApiParameter(
                name="id",
                type=int,
                location=OpenApiParameter.QUERY,
                description="Filtrar por ID",
            ),
            OpenApiParameter(
                name="nome",
                type=str,
                location=OpenApiParameter.QUERY,
                description="Filtrar por nome",
            ),
        ],
        responses={200: OpenApiTypes.OBJECT},
    )
    @action(detail=False, methods=["get"], url_path="filtrar/id-nome")
    def filter_id_nome(self, request):
        return Response("Filtrar clientes por id e nome")
