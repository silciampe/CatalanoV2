from django.db import models
from django.contrib.auth.models import User

class MotoParte(models.Model):
    id_catalano = models.CharField(max_length=250, null=False, blank=False)
    articulo = models.CharField(max_length=250, null=True, blank=True)
    grupo = models.CharField(max_length=250, null=True, blank=True)
    modelo_marca = models.CharField(max_length=250, null=True, blank=True)
    paso_de_la_cadena = models.CharField(max_length=250, null=True, blank=True)
    dientes = models.IntegerField(null=True, blank=True)
    compatible = models.CharField(max_length=250, null=True, blank=True)
    modelo = models.CharField(max_length=250, null=True, blank=True)
    marca = models.CharField(max_length=250, null=True, blank=True)
    cadena = models.CharField(max_length=250, null=True, blank=True)
    codigo_original = models.CharField(max_length=250, null=True, blank=True)
    diametro_exterior = models.CharField(max_length=250, null=True, blank=True)
    diametro_interior = models.CharField(max_length=250, null=True, blank=True)
    diametro_rodillo = models.CharField(max_length=250, null=True, blank=True)
    cantidad_agujero_x_diametro_agujero = models.CharField(max_length=250, null=True, blank=True)
    cantidad_estrias_x_tipo_rosca = models.CharField(max_length=250, null=True, blank=True)
    cantidad_estrias_x_espesor_estrias = models.CharField(max_length=250, null=True, blank=True)  
    imagen = models.ImageField(upload_to="static/imagenes/motopartes")  
    modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_created=True)
    
class AgroParte(models.Model):
    id_catalano = models.CharField(max_length=250, null=False, blank=False)
    grupo = models.CharField(max_length=250, null=True, blank=True)
    medida_cub = models.CharField(max_length=250, null=True, blank=True)
    espesor_mm = models.CharField(max_length=250, null=True, blank=True)
    dientes = models.IntegerField(null=True, blank=True)
    rad_mm = models.CharField(max_length=250, null=True, blank=True)
    modelo = models.CharField(max_length=250, null=True, blank=True)
    marca = models.CharField(max_length=250, null=True, blank=True)
    cadena = models.CharField(max_length=250, null=True, blank=True)
    observacion = models.CharField(max_length=250, null=True, blank=True)
    diametro_exterior = models.CharField(max_length=250, null=True, blank=True)
    diametro_interior = models.CharField(max_length=250, null=True, blank=True)
    diametro_rodillo = models.CharField(max_length=250, null=True, blank=True)
    cantidad_agujero_x_diametro_agujero = models.CharField(max_length=250, null=True, blank=True)
    cantidad_estrias_x_tipo_rosca = models.CharField(max_length=250, null=True, blank=True)
    cantidad_estrias_x_espesor_estrias = models.CharField(max_length=250, null=True, blank=True)    
    imagen = models.ImageField(upload_to="static/imagenes/agropartes")  
    modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_created=True)
    
   
class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    razon_social = models.CharField(max_length=250, null=True, blank=True)
    puntos_moto = models.IntegerField()
    puntos_agro = models.IntegerField()
    cuit = models.CharField(max_length=30, null=True, blank=True)
    fecha_actualizacion = models.DateField(auto_now=True)
    rubro = models.IntegerField()
    
        

    
    