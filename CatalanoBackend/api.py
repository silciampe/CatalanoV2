from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework.decorators import action 
from rest_framework.response import Response
from CatalanoBackend.serializers import UserSerializer  
from .models import MotoParte, AgroParte, Premio 
from .serializers import MotoParteSerializer, AgroParteSerializer, PremioSerializer
from django_filters.rest_framework import DjangoFilterBackend


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets
from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from .models import MotoParte
from .serializers import MotoParteSerializer
from rest_framework.permissions import IsAuthenticated

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
    
    # Método para búsqueda avanzada con filtros dinámicos
    @action(detail=False, methods=['get'], url_path='avanzada')
    def filtros(self, request):
        grupo = request.query_params.get('grupo')
        marca = request.query_params.get('marca')
        modelo = request.query_params.get('modelo')
        dientes = request.query_params.get('dientes')
        cadena = request.query_params.get('cadena')
        diametro_interior = request.query_params.get('diametro_interior')
        diametro_exterior = request.query_params.get('diametro_exterior')
        cantidad_rosca = request.query_params.get('cantidad_rosca')
        espesor_estrias = request.query_params.get('espesor_estrias')
        cantidad_diam_ag = request.query_params.get('cantidad_diam_ag')

        # Construir filtros dinámicos
        filters = Q()
        if grupo:
            filters &= Q(grupo=grupo)
        if marca:
            filters &= Q(marca__icontains=marca)
        if modelo:
            filters &= Q(modelo__icontains=modelo)
        if dientes:
            filters &= Q(dientes=dientes)
        if cadena:
            filters &= Q(cadena__icontains=cadena)
        if diametro_interior:
            filters &= Q(diametro_interior__icontains=diametro_interior)
        if diametro_exterior:
            filters &= Q(diametro_exterior__icontains=diametro_exterior)
        if cantidad_rosca:
            filters &= Q(cantidad_estrias_x_tipo_rosca__icontains=cantidad_rosca)
        if espesor_estrias:
            filters &= Q(cantidad_estrias_x_espesor_estrias__icontains=espesor_estrias)
        if cantidad_diam_ag:
            filters &= Q(cantidad_agujero_x_diametro_agujero__icontains=cantidad_diam_ag)

        # Aplicar los filtros a la consulta
        resultados = MotoParte.objects.filter(filters).order_by('id_catalano')
        serializer = self.get_serializer(resultados, many=True)
        return Response(serializer.data)

        return Response(serializer.data)
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
    
     # Acción personalizada para la búsqueda avanzada
    @action(detail=False, methods=['get'], url_path='avanzada')
    def busqueda_avanzada(self, request):
        grupo = request.query_params.get('grupo', None)
        marca = request.query_params.get('marca', None)
        modelo = request.query_params.get('modelo', None)
        dientes = request.query_params.get('dientes', None)
        cadena = request.query_params.get('cadena', None)
        diametro_interior = request.query_params.get('diametro_interior', None)
        diametro_exterior = request.query_params.get('diametro_exterior', None)
        diametro_centro = request.query_params.get('diametro_centro', None)
        cantidad_rosca = request.query_params.get('cantidad_estrias_x_tipo_rosca', None)
        espesor_estrias = request.query_params.get('cantidad_estrias_x_espesor_estrias', None)
        cantidad_diam_ag = request.query_params.get('cantidad_agujero_x_diametro_agujero', None)

        filters = Q()
        if grupo:
            filters &= Q(grupo=grupo)
        if marca:
            filters &= Q(marca__icontains=marca)  # Búsqueda parcial e insensible a mayúsculas/minúsculas
        if modelo:
            filters &= Q(modelo__icontains=modelo)  # Búsqueda parcial e insensible a mayúsculas/minúsculas
        if dientes:
            filters &= Q(dientes=dientes)
        if cadena:
            filters &= Q(cadena__icontains=cadena)
        if diametro_interior:
            filters &= Q(diametro_interior__icontains=diametro_interior)
        if diametro_exterior:
            filters &= Q(diametro_exterior__icontains=diametro_exterior)
        if diametro_centro:
            filters &= Q(diametro_centro__icontains=diametro_centro)
        if cantidad_rosca:
            filters &= Q(cantidad_estrias_x_tipo_rosca__icontains=cantidad_rosca)
        if espesor_estrias:
            filters &= Q(cantidad_estrias_x_espesor_estrias__icontains=espesor_estrias)
        if cantidad_diam_ag:
            filters &= Q(cantidad_agujero_x_diametro_agujero__icontains=cantidad_diam_ag)

        resultados = AgroParte.objects.filter(filters).order_by('id_catalano')
        serializer = self.get_serializer(resultados, many=True)
        return Response(serializer.data)
    
    # Acción personalizada para subir archivos con motopartes
    @action(detail=False, methods=['post'], url_path='importar')
    def importar(self, request):
        file = request.FILES['file']
        for line in file:
            print(line)

        return Response('exito')
    
class PremioViewSet(viewsets.ModelViewSet):
    queryset = Premio.objects.all().order_by('orden')
    serializer_class = PremioSerializer
    filter_backends = [DjangoFilterBackend]
    #permission_classes = [IsAuthenticated]
    
