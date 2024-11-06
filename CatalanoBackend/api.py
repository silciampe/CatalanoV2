from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework.decorators import action 
from CatalanoBackend.serializers import UserSerializer  
from .models import MotoParte 
from .serializers import MotoParteSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class MotoParteViewSet(viewsets.ModelViewSet):
    queryset = MotoParte.objects.all()
    serializer_class = MotoParteSerializer
    
    def get_queryset(self):
        qs = MotoParte.objects.all()
        grupo = self.request.query_params.get('grupo')
        if grupo: 
            qs = qs.filter(grupo=grupo)
        return qs
    