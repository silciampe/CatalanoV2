from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework.decorators import action 
from rest_framework.response import Response
from CatalanoBackend.serializers import UserSerializer  
from .models import MotoParte 
from .models import AgroParte 
from .serializers import MotoParteSerializer
from .serializers import AgroParteSerializer
from django_filters.rest_framework import DjangoFilterBackend


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class MotoParteViewSet(viewsets.ModelViewSet):
    queryset = MotoParte.objects.all().order_by('id_catalano')
    serializer_class = MotoParteSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['grupo', 'id_catalano', 'marca', 'dientes', 'modelo', 'cadena', 'diametro_exterior', 'diametro_interior', 'diametro_rodillo', 'cantidad_agujero_x_diametro_agujero', 'cantidad_estrias_x_tipo_rosca', 'cantidad_estrias_x_espesor_estrias']
    
        # Método para obtener marcas según el grupo
    @action(detail=False, methods=['get'], url_path='marcas')
    def marcas(self, request):
        grupo = request.query_params.get('grupo', None)
        if grupo:
            marcas = MotoParte.objects.filter(grupo=grupo).values_list('marca', flat=True).distinct()
            return Response(list(marcas))
        return Response([])

    # Método para obtener modelos según el grupo y la marca
    @action(detail=False, methods=['get'], url_path='modelos')
    def modelos(self, request):
        grupo = request.query_params.get('grupo', None)
        marca = request.query_params.get('marca', None)
        if grupo and marca:
            modelos = MotoParte.objects.filter(grupo=grupo, marca=marca).values_list('modelo', flat=True).distinct()
            return Response(list(modelos))
        return Response([])
    
class AgroParteViewSet(viewsets.ModelViewSet):
    queryset = AgroParte.objects.all().order_by('id_catalano')
    serializer_class = AgroParteSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['grupo', 'id_catalano', 'medida_cub', "espesor_mm", 'dientes', 'rad_mm', 'modelo', 'marca', 'cadena', 'observacion', 'diametro_exterior', 'diametro_interior', 'diametro_rodillo', 'cantidad_agujero_x_diametro_agujero', 'cantidad_estrias_x_tipo_rosca', 'cantidad_estrias_x_espesor_estrias']
    
        # Método para obtener marcas según el grupo
    @action(detail=False, methods=['get'], url_path='marcas')
    def marcas(self, request):
        grupo = request.query_params.get('grupo', None)
        if grupo:
            marcas = AgroParte.objects.filter(grupo=grupo).values_list('marca', flat=True).distinct()
            return Response(list(marcas))
        return Response([])

    # Método para obtener modelos según el grupo y la marca
    @action(detail=False, methods=['get'], url_path='modelos')
    def modelos(self, request):
        grupo = request.query_params.get('grupo', None)
        marca = request.query_params.get('marca', None)
        if grupo and marca:
            modelos = AgroParte.objects.filter(grupo=grupo, marca=marca).values_list('modelo', flat=True).distinct()
            return Response(list(modelos))
        return Response([])