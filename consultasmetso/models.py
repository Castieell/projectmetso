from django.db import models





class Usuarios(models.Model ):

    first_last_name = models.CharField("apellido paterno", max_length=255)
    second_last_name = models.CharField("apellido materno", max_length=255)
    name = models.CharField("primer nombre", max_length=255)
    employee_rut = models.CharField("rut empleado", max_length=255)
    cargo = models.CharField("cargo del empleado", default = 'no definido', max_length=255)
    OPCIONES_CONTRATO = [
        ('base', 'Base'),
        ('spot', 'Spot'),]
    contrato = models.CharField(
        "cargo del empleado",
        choices=OPCIONES_CONTRATO,
        default='',  
        max_length=10,
    )
      

    class Meta:
        verbose_name = ("")
        verbose_name_plural = ("usuarios")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})

class Certificados(models.Model):

    nombre_certificado = models.CharField("nombre del certificado", max_length=255)
    fecha_certificado = models.DateField("fecha agregado al sistema", auto_now_add=False)


    class Meta:
        verbose_name = ("")
        verbose_name_plural = ("certificados")

    def __str__(self):
        return self.nombre_certificado

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})
    



class certificateUsers(models.Model):

    fecha_realizacion = models.DateField("fecha vencimiento", auto_now_add=False, null=True, blank=True)
    usuarios = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    certificado = models.ForeignKey(Certificados ,on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("")
        verbose_name_plural = ("Información del empleado")

    def __str__(self):
        return f"(self.certificado.nombre_certificado)"

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})




# Create your models here.
