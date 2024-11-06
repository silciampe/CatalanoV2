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
    
admin.site.unregister(User)
admin.site.register(AgroParte, AgroParteAdmin)
admin.site.register(MotoParte, MotoParteAdmin)
admin.site.register(User, Cliente)