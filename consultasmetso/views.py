from django.shortcuts import render
from django.http import HttpResponse
import datetime
from rest_framework.views import APIView
from consultasmetso.models import Usuarios, Certificados, certificateUsers
from rest_framework import status
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class UsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuarios
        fields = '__all__'

class CertificadosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificados
        fields = '__all__'

class certificateUsersSerializer(serializers.ModelSerializer):
    usuarios = UsuariosSerializer(read_only=True)
    certificado = CertificadosSerializer(read_only=True)
    
    class Meta:
        model = certificateUsers
        fields = '__all__'




def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

class Empleados(APIView):
    #authentication_classes = [BasicAuthentication]
    #permission_classes = [IsAuthenticated]
    
    def get(self, request, format=None):
        empleados = Usuarios.objects.all()
        serializer = UsuariosSerializer(empleados, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

class EmpleadosCertificados(APIView):
    def get(self, request, format=None):
        empleados = certificateUsers.objects.all()
        serializer = certificateUsersSerializer(empleados, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)