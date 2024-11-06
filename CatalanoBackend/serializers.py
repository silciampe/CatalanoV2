from rest_framework import serializers
from django.contrib.auth.models import User
from .models import MotoParte 

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']
        
class MotoParteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MotoParte
        fields = ['id_catalano', 'articulo', 'grupo', 'modelo_marca', 'paso_de_la_cadena', 'dientes', 'compatible', 'modelo', 'marca', 'cadena', 'codigo_original', 'diametro_exterior', 'diametro_interior', 'diametro_rodillo', 'cantidad_agujero_x_diametro_agujero', 'cantidad_estrias_x_tipo_rosca', 'cantidad_estrias_x_espesor_estrias', 'imagen']