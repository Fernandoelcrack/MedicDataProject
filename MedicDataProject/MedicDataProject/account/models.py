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
    edadG = models.CharField(max_length=255, verbose_name='Edad del paciente')
    peso = models.CharField(max_length=20, verbose_name='Talla')
    operaciones = models.CharField(max_length=255, verbose_name='Operaciones')
    lesiones=models.CharField(max_length=255, verbose_name='Lesiones')
    alergias=models.CharField(max_length=255, verbose_name='Alergias')
    enfermedades=models.CharField(max_length=255, verbose_name='Enfermedades')
    tipoSangre=models.CharField(max_length=255, verbose_name='Tipo de Sangre')
    fecha=models.DateTimeField(auto_now_add=True)
    fecha_actG=models.DateTimeField(auto_now=True)
    # doctorG = models.CharField(max_length=255, verbose_name='Nombre del doctor')
    idPg = models.ForeignKey(User, blank=True, on_delete=models.CASCADE, verbose_name='Usuario paciente', related_name='paciente')
    idDg = models.ForeignKey(User, blank=True, on_delete=models.CASCADE, verbose_name='Usuario doctor', related_name='doctor')

    class Meta:
        ordering=('nombreG',)

    def __str__(self):
        return self.nombreG

class ExpedienteO(models.Model):
    idEo = models.AutoField(primary_key=True)
    nombreO = models.CharField(max_length=255, verbose_name='Nombre del paciente')
    edadO = models.CharField(max_length=255, verbose_name='Edad del paciente')
    gojoD=models.CharField(max_length=255, verbose_name="Graduacion ojo derecho")
    gojoI=models.CharField(max_length=255, verbose_name="Graduacion ojo izquierdo")
    padecimientos=models.CharField(max_length=255, verbose_name="Padecimientos")
    cambioMicas=models.CharField(max_length=255, verbose_name="Cambio de micas")
    fechaO=models.DateTimeField(auto_now_add=True)
    fecha_actO=models.DateField(auto_now=True)
    idPg = models.ForeignKey(User, blank=True, on_delete=models.CASCADE, verbose_name='Usuario paciente', related_name='pacienteo')
    idDo = models.ForeignKey(User, blank=True, on_delete=models.CASCADE, verbose_name='Usuario doctor', related_name='doctoro')

    class Meta:
        ordering=('nombreO',)

    def __str__(self):
        return self.nombreO

class ExpedienteD(models.Model):
    idEd = models.AutoField(primary_key=True)
    nombreD = models.CharField(max_length=255, verbose_name='Nombre del paciente')
    edadD = models.CharField(max_length=255, verbose_name='Edad del paciente')
    NDiente1 = models.CharField(max_length=255, verbose_name='Nombre del diente1')
    NDiente2 = models.CharField(max_length=255, verbose_name='Nombre del diente2')
    NDiente3 = models.CharField(max_length=255, verbose_name='Nombre del diente3')
    NDiente4 = models.CharField(max_length=255, verbose_name='Nombre del diente4')
    NDiente5 = models.CharField(max_length=255, verbose_name='Nombre del diente5')
    Descripcion= models.CharField(max_length=550, verbose_name="Descripcion")
    fechaD=models.DateTimeField(auto_now_add=True)
    fecha_actD=models.DateField(auto_now=True)
    idPg = models.ForeignKey(User, blank=True, on_delete=models.CASCADE, verbose_name='Usuario paciente', related_name='paciented')
    idDd = models.ForeignKey(User, blank=True, on_delete=models.CASCADE, verbose_name='Usuario doctor', related_name='doctord')

    class Meta:
        ordering=('nombreD',)

    def __str__(self):
        return self.nombreD
        
class Profile(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=255, verbose_name='Nombre(s)')
    apellidos = models.CharField(max_length=255, verbose_name='Apellidos')
    telefonoc = models.CharField(max_length=255, verbose_name='Teléfono celular')
    telconsultorio = models.CharField(max_length=255, verbose_name='Telefono consultorio')
    lugart = models.CharField(max_length=255, verbose_name='Lugar de trabajo')
    direcciont = models.CharField(max_length=255, verbose_name='Direccion de trabajo')
    especialidad = models.CharField(max_length=255, verbose_name='Especilidad general')
    otras = models.CharField(max_length=255, verbose_name='Otras Especilidades')
    profile_title = models.ImageField(default="titulo.png", null=True, blank=True)
    profile_pic = models.ImageField(default="perfil.png", null=True, blank=True)

    def __str__(self):
        return self.nombre      

class Perfil(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    nom = models.CharField(max_length=255, verbose_name='Nombre del usuario')
    apell = models.CharField(max_length=255, verbose_name='Apellidos del paciente')
    edad = models.CharField(max_length=255, verbose_name='Edad del paciente')
    telc = models.CharField(max_length=255, verbose_name='Teléfono celular')
    domicilio = models.CharField(max_length=255, verbose_name='Domicilio')
    seguro = models.CharField(max_length=255, verbose_name='Seguro Medico')
    profile_pic = models.ImageField(default="perfil1.png", null=True, blank=True)

    def __str__(self):
        return self.nombre   