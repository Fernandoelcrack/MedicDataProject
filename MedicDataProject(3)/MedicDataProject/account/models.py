from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
#from django.utils.html import escape, make_safe

# Create your models here.
class User (AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_patient = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)

class ExpedienteG(models.Model):
    idEg = models.AutoField(primary_key=True)
    nombreG = models.CharField(max_length=255, verbose_name='Nombre del paciente')
    peso = models.CharField(max_length=20, verbose_name='Talla')
    operaciones = models.CharField(max_length=255, verbose_name='Operaciones')
    lesiones=models.CharField(max_length=255, verbose_name='Lesiones')
    alergias=models.CharField(max_length=255, verbose_name='Alergias')
    enfermedades=models.CharField(max_length=255, verbose_name='Enfermedades')
    tipoSangre=models.CharField(max_length=255, verbose_name='Tipo de Sangre')
    fecha=models.DateTimeField(auto_now_add=True)
    fecha_actG=models.DateTimeField(auto_now=True)
    # doctorG = models.CharField(max_length=255, verbose_name='Nombre del doctor')
    idPg = models.ForeignKey(User, blank=True, on_delete=models.CASCADE, verbose_name='Usuario paciente')

    class Meta:
        ordering=('nombreG',)

class ExpedienteO(models.Model):
    idEo = models.AutoField(primary_key=True)
    nombreO = models.CharField(max_length=255, verbose_name='Nombre del paciente')
    gojoD=models.CharField(max_length=255, verbose_name="Graduacion ojo derecho")
    gojoI=models.CharField(max_length=255, verbose_name="Graduacion ojo izquierdo")
    padecimientos=models.CharField(max_length=255, verbose_name="Padecimientos")
    cambioMicas=models.CharField(max_length=255, verbose_name="Cambio de micas")
    fechaO=models.DateTimeField(auto_now_add=True)
    fecha_actO=models.DateField(auto_now=True)
    idPg = models.ForeignKey(User, blank=True, on_delete=models.CASCADE)

    class Meta:
        ordering=('nombreO',)

class ExpedienteD(models.Model):
    idEd = models.AutoField(primary_key=True)
    nombreD = models.CharField(max_length=255, verbose_name='Nombre del paciente')
    NDiente = models.CharField(max_length=255, verbose_name='Nombre del diente')
    Descripcion= models.CharField(max_length=255, verbose_name="Descripcion")
    fechaD=models.DateTimeField(auto_now_add=True)
    fecha_actD=models.DateField(auto_now=True)
    idPg = models.ForeignKey(User, blank=True, on_delete=models.CASCADE)

    class Meta:
        ordering=('nombreD',)



