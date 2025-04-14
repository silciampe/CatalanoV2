from rest_framework import serializers
from django.contrib.auth.models import User
from .models import MotoParte, AgroParte, Cliente, Premio, Catalogo 

class UserSerializer(serializers.HyperlinkedModelSerializer):
    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret["tipo"] = instance.cliente.tipo_cliente
        ret["puntos"] = instance.cliente.puntos
        ret["razon_social"] = instance.cliente.razon_social
        ret["actualizacion"] = instance.cliente.fecha_actualizacion

        return ret
    class Meta:
        model = User
        fields = ['username', 'email', 'is_superuser']
        
class MotoParteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MotoParte
        fields = ['id_catalano', 'articulo', 'grupo', 'modelo_marca', 'paso_de_la_cadena', 'dientes', 'compatible', 'modelo', 'marca', 'cadena', 'codigo_original', 'diametro_exterior', 'diametro_interior', 'diametro_rodillo', 'cantidad_agujero_x_diametro_agujero', 'cantidad_estrias_x_tipo_rosca', 'cantidad_estrias_x_espesor_estrias', 'imagen']
        
class AgroParteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AgroParte
        fields = ['grupo', 'id_catalano', 'medida_cub', "espesor_mm", 'dientes', 'rad_mm', 'modelo', 'marca', 'cadena', 'observacion', 'diametro_exterior', 'diametro_interior', 'diametro_rodillo', 'cantidad_agujero_x_diametro_agujero', 'cantidad_estrias_x_tipo_rosca', 'cantidad_estrias_x_espesor_estrias', 'imagen']

class ClienteSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret["es_admin"] = instance.user.is_superuser

        return ret
    class Meta:
        model = Cliente
        fields = ['razon_social', 'puntos', 'tipo_cliente']


class PremioSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        cliente = self.context['request'].user.cliente
        ret["puntos"] = instance.puntos_agroparte if cliente.tipo_cliente == 'Agro' else instance.puntos_motoparte 
        
        return ret

    class Meta:
        model = Premio
        fields = ['nombre', 'descripcion', 'imagen']


class CatalogoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Catalogo
        fields = '__all__'
