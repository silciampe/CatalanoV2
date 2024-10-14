from django.db import models

class MotoPartes(models.Model):
    id_catalano = models.CharField(max_length=250, null=False, blank=False)
    articulo = models.CharField(max_length=250, null=True, blank=True)
    grupo = models.CharField(max_length=250, null=True, blank=True)
    modelo_marca = models.CharField(max_length=250, null=True, blank=True)
    paso_de_la_cadena = models.CharField(max_length=250, null=True, blank=True)
    dientes = models.CharField(max_length=250, null=True, blank=True)
    compatible = models.CharField(max_length=250, null=True, blank=True)
    imagen = models.CharField(max_length=20, null=True, blank=True)
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
    modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_created=True)
    
class AgroPartes(models.Model):
    id_catalano = models.CharField(max_length=250, null=False, blank=False)
    grupo = models.CharField(max_length=250, null=True, blank=True)
    medida_cub = models.CharField(max_length=250, null=True, blank=True)
    espesor_mm = models.CharField(max_length=250, null=True, blank=True)
    dientes = models.CharField(max_length=250, null=True, blank=True)
    rad_mm = models.CharField(max_length=250, null=True, blank=True)
    imagen = models.CharField(max_length=20, null=True, blank=True)
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
    modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_created=True)
    
class Albums(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)    
    date = models.DateField(null=True, blank=True)    
    enabled = models.BooleanField(default=True)
    modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_created=True)
    
class PremiosCategorias(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    created = models.DateTimeField(auto_created=True)
    modified = models.DateTimeField(auto_now=True)
    
class Premios(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    points = models.IntegerField(null=True, blank=True) 
    award_category_id = models.IntegerField(null=True, blank=True) 
    new = models.BooleanField(default=False)  
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_created=True)
    modified = models.DateTimeField(auto_now=True)
    
class BrwFiles(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    record_id = models.PositiveBigIntegerField(null=True, blank=True)
    model = models.CharField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    category_code = models.CharField(max_length=10, null=True, blank=True)
    order = models.IntegerField(null=True, blank=True)
    created = models.DateTimeField(auto_created=True)
    modified = models.DateTimeField(auto_now=True)
    
class BrwImages(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    record_id = models.PositiveBigIntegerField(null=True, blank=True)
    model = models.CharField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    category_code = models.CharField(max_length=10, null=True, blank=True)
    created = models.DateTimeField(auto_created=True)
    modified = models.DateTimeField(auto_now=True)
    
class BrwUsers(models.Model):
    email = models.CharField(max_length=255, null=True, blank=True)
    password = models.CharField(max_length=255, null=True, blank=True)
    root = models.BooleanField(default=False)  
    last_login = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_created=True)
    modified = models.DateTimeField(auto_now=True)
    
class Mensajes(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    telephone = models.CharField(max_length=255, null=True, blank=True)
    subject = models.CharField(max_length=255, null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_created=True)
    modified = models.DateTimeField(auto_now=True)
    
class OrderProducts(models.Model):
    order_id = models.IntegerField()
    product_id = models.IntegerField()
    quantity = models.IntegerField()
    user_id = models.IntegerField()
    id_catalano = models.IntegerField()
    created = models.DateTimeField(auto_created=True)
    modified = models.DateTimeField(auto_now=True)
    
class OrderRecipients(models.Model):
    email = models.CharField(max_length=250, null=True, blank=True)
    enabled = models.BooleanField(default=True)  
    created = models.DateTimeField(auto_created=True)
    modified = models.DateTimeField(auto_now=True)
    
class OrderStatuses(models.Model):
    name = models.CharField(max_length=250, null=True, blank=True)
    sort = models.IntegerField()
    enabled = models.BooleanField(default=True)  
    created = models.DateTimeField(auto_created=True)
    modified = models.DateTimeField(auto_now=True)
    

class OrderTexts(models.Model):
    title = models.CharField(max_length=250, null=True, blank=True)
    text = models.TextField()
    created = models.DateTimeField(auto_created=True)
    modified = models.DateTimeField(auto_now=True)
    
class Orders(models.Model):
    user_id = models.IntegerField()
    order_status_id = models.IntegerField()
    message = models.TextField()
    confirmed = models.BooleanField(default=True)  
    created = models.DateTimeField(auto_created=True)
    modified = models.DateTimeField(auto_now=True)
    
class Pages(models.Model):
    title = models.CharField(max_length=250, null=True, blank=True)
    text = models.TextField()
    created = models.DateTimeField(auto_created=True)
    modified = models.DateTimeField(auto_now=True)
    
class Pdfs(models.Model):
    created = models.DateTimeField(auto_created=True)
    modified = models.DateTimeField(auto_now=True)
    
class PostCategories(models.Model):
    name = models.CharField(max_length=250, null=True, blank=True)
    sort = models.IntegerField()
    created = models.DateTimeField(auto_created=True)
    modified = models.DateTimeField(auto_now=True)
    
class post(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    abstract = models.CharField(max_length=255, null=True, blank=True)
    text = models.TextField()
    publication_date = models.DateField()
    highlighted = models.BooleanField(default=True) 
    enabled = models.BooleanField(default=True) 
    created = models.DateTimeField(auto_created=True)
    modified = models.DateTimeField(auto_now=True)
    email = models.CharField(max_length=250, null=True, blank=True)
    created = models.DateTimeField(auto_created=True)
    modified = models.DateTimeField(auto_now=True)

class Textos(models.Model):
    key = models.CharField(max_length=255, null=True, blank=True)
    text = models.TextField()
    created = models.DateTimeField(auto_created=True)
    modified = models.DateTimeField(auto_now=True)

class UserTexts(models.Model):
    key = models.CharField(max_length=255, null=True, blank=True)
    title = models.CharField(max_length=250, null=True, blank=True)
    text = models.TextField()
    modified = models.DateTimeField(auto_now=True)

class Usuarios(models.Model):
    razon_social = models.CharField(max_length=250, null=True, blank=True)
    puntos_moto = models.IntegerField()
    puntos_agro = models.IntegerField()
    cuit = models.CharField(max_length=30, null=True, blank=True)
    password = models.CharField(max_length=255, null=True, blank=True)
    fecha_actualizacion = models.DateField(auto_now=True)
    rubro = models.IntegerField()
    email = models.EmailField(max_length=255)

        

    
    