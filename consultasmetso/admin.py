from django.contrib import admin
from consultasmetso.models import Usuarios, Certificados, certificateUsers



@admin.register(Usuarios)
class Admin(admin.ModelAdmin):
    search_fields = ("id", "employee_rut", "name", "first_last_name", "second_last_name", )
    list_display = ("id", "employee_rut", "name", "first_last_name", "second_last_name", )

@admin.register(Certificados)
class Admin(admin.ModelAdmin):
    search_fields = ("id", "nombre_certificado")
    list_display = ("id", "fecha_certificado", "nombre_certificado")

@admin.register(certificateUsers)
class Admin(admin.ModelAdmin):
    search_fields = ("id", "certificado")
    list_display = ("fecha_realizacion", "usuarios", "certificado")

    def nombre_relacionado(self_obj):
        return obj.certificado.nombre_certificado

    Certificados.short_description = 'Nombre del certificado'


