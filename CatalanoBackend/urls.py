"""
URL configuration for CatalanoBackend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from rest_framework import routers

from CatalanoBackend import api, settings, views, auth

router = routers.DefaultRouter()
router.register(r'users', api.UserViewSet)
router.register(r'motopartes', api.MotoParteViewSet)
router.register(r'agropartes', api.AgroParteViewSet)
router.register(r'premios', api.PremioViewSet)
router.register(r'catalogo', api.CatalogoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/importarMotopartes/', views.ImportarMotopartes.as_view(), name='importarMotopartes'),
    path('api/importarAgropartes/', views.ImportarAgropartes.as_view(), name='importarAgropartes'),
    path('api/importarClientes/', views.ImportarClientes.as_view(), name='importarClientes'),
    re_path('login/', auth.login, name='login'),
    re_path('logout/', auth.logout, name='logout'),
    re_path('registro/', auth.registro),
    re_path('perfil/', auth.perfil),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
