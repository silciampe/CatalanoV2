from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from CatalanoBackend.serializers import UserSerializer, ClienteSerializer
from CatalanoBackend.models import User, Cliente

from django.shortcuts import get_object_or_404


@api_view(['POST'])
def login(request):
    try:
        user = User.objects.get(username=request.data['username'])
    except User.DoesNotExist:
        return Response({"mensaje": "Usuario o contraseña incorrectos"}, status=status.HTTP_400_BAD_REQUEST)
    
    if not user.check_password(request.data['password']):
        return Response({"mensaje": "Usuario o contraseña incorrectos"}, status=status.HTTP_400_BAD_REQUEST)
    
    token = Token.objects.get_or_create(user=user)
    serializer_context = {
            'request': request,
        }
    serializer = UserSerializer(instance=user, context=serializer_context)
                                                                                    
    return Response({"token": token[0].key, "user": serializer.data}, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def logout(request):
    user = request.user
    token = Token.objects.get(user=user)
    token.delete()
                                                                                    
    return Response({"success": True}, status=status.HTTP_200_OK)

@api_view(['POST'])
def registro(request):
    
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

        user = User.objects.get(username=serializer.data['username'])
        user.set_password(serializer.data['password'])
        user.save()

        token = Token.objects.create(user=user)

        return Response(token.key, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def perfil(request):
    user = request.user
    if not Cliente.objects.filter(user=user).exists():
        user.client = Cliente.objects.create(user = user, 
                                             razon_social = 'fede aguer', 
                                             puntos_moto = 10, 
                                             puntos_agro = 20, 
                                             rubro = 1)
    
    serializer = ClienteSerializer(instance=user.cliente)

    return Response(serializer.data, status=status.HTTP_200_OK)
