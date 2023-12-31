import json
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
from django.http import JsonResponse
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render

#def es_usuario_autorizado(user):
    # Define la lógica para determinar si el usuario está autorizado o no
    #return user.is_authenticated and user.groups.filter(name='GrupoAutorizado').exists()

#@user_passes_test(es_usuario_autorizado)
#def mi_vista(request):
    # Tu lógica de vista aquí
    #return render(request, 'mi_app/mi-vista/', 'mi_app/certificateUsers/')


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
    
class RecursosHumanos(APIView):
    #authentication_classes = [BasicAuthentication]
    #permission_classes = [IsAuthenticated]
    
    def get(self, request, format=None):
        empleados = Usuarios.objects.all()
        serializer = UsuariosSerializer(empleados, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

class EmpleadosCertificados(APIView):


    def getCertificate(self, user_id):
        certificate = certificateUsers.objects.filter(usuarios_id=user_id)
        return certificate

    def get(self, request, format=None):
        empleados = Usuarios.objects.all()
        users = []
        for empleado in empleados:
            certificates = self.getCertificate(empleado.pk)
            serializer = UsuariosSerializer(empleado)
            serializer_certificates = certificateUsersSerializer(certificates, many=True).data
            certificates_array = []
            for serializer_certificate in serializer_certificates:
                serializer_certificate['certificado']['fecha_relizacion'] = serializer_certificate['fecha_realizacion']
                certificates_array.append(serializer_certificate['certificado'])
            users_with_certificate = {
                'user': serializer.data,
                'certificate': certificates_array
            }
            users.append(users_with_certificate)

        return Response(users, status=status.HTTP_201_CREATED)