from CatalanoBackend.models import *
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

class ClienteInline(admin.StackedInline):
    model = Cliente
    can_delete = False
    
    
class Cliente(UserAdmin):
    inlines = (ClienteInline,)
    
admin.site.unregister(User)
admin.site.register(AgroParte)
admin.site.register(MotoParte)
admin.site.register(User, Cliente)