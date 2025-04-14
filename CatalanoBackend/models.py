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
    imagen = models.ImageField(upload_to="imagenes/motopartes")  
    modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
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
    imagen = models.ImageField(upload_to="imagenes/agropartes")  
    modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
   
class Cliente(models.Model):
    TIPO_CLIENTE = [
        ('Agro', 'Agro'),
        ('Moto', 'Moto'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    razon_social = models.CharField(max_length=250, null=True, blank=True)
    puntos = models.IntegerField()
    tipo_cliente = models.CharField(max_length=4, choices=TIPO_CLIENTE, default='Moto')
    cuit = models.CharField(max_length=30, null=True, blank=True)
    fecha_actualizacion = models.DateField(auto_now=True)
    rubro = models.IntegerField()
    id_catalano = models.CharField(max_length=250, null=True, blank=True)
    

class Premio(models.Model):
    nombre = models.CharField(max_length=250, null=True, blank=True)
    descripcion = models.CharField(max_length=250, null=True, blank=True)
    puntos_motoparte = models.IntegerField()
    puntos_agroparte = models.IntegerField()
    stock = models.IntegerField()
    orden = models.IntegerField()
    imagen = models.ImageField(upload_to="imagenes/premios")  
    modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

class Catalogo(models.Model):
    nombre = models.CharField(max_length=250, null=True, blank=True)
    orden = models.IntegerField()
    imagen = models.ImageField(upload_to="imagenes/catalogo")  
    archivo = models.FileField(upload_to="imagenes/catalogos/archivos")

        

    
    