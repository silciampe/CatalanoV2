from CatalanoBackend.models import *
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

class ClienteInline(admin.StackedInline):
    model = Cliente
    can_delete = False
    
    
class Cliente(UserAdmin):
    inlines = (ClienteInline,)
    
class AgroParteAdmin(admin.ModelAdmin):
    model = AgroParte
    list_display = ['id_catalano', 'grupo', 'marca', 'modelo', 'observacion']
    list_filter = ["grupo", "modelo"]
    
    
class MotoParteAdmin(admin.ModelAdmin):
    model = MotoParte
    list_display = ['id_catalano', 'grupo', 'marca', 'modelo']
    list_filter = ["grupo", "modelo"]


class PremioAdmin(admin.ModelAdmin):
    model = Premio
    list_display = ['nombre', 'descripcion', 'puntos']
    list_filter = ['nombre', 'descripcion', 'puntos']
    
admin.site.unregister(User)
admin.site.register(AgroParte, AgroParteAdmin)
admin.site.register(MotoParte, MotoParteAdmin)
admin.site.register(Premio, PremioAdmin)
admin.site.register(User, Cliente)