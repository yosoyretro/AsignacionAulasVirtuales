from django.db import models

# Create your models here.
class Perfil(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=100) 
    estado = models.CharField(max_length=3,default="A")
    
class Usuarios(models.Model):
    id = models.AutoField(primary_key=True)
    img = models.BinaryField()
    cedula = models.CharField(max_length=15)
    nombres = models.CharField(max_length=75)
    apellidos = models.CharField(max_length=100)
    clave = models.CharField(max_length=20)
    edad = models.IntegerField()
    genero = models.CharField(max_length=50)
    pais_natal = models.CharField(max_length=70)
    ciuda_natal = models.CharField(max_length=100)
    id_perfil = models.ForeignKey(Perfil,on_delete=models.CASCADE)
    estado = models.CharField(max_length=3,default="A")

class Curso(models.Model):
    id = models.AutoField(primary_key=True)
    curso = models.CharField(max_length=75)
    estado = models.CharField(max_length=3,default="A")
    
class Materia(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=100)
    estado = models.CharField(max_length=3,default="A")
    
class AsignacionMaterias(models.Model):
    id = models.AutoField(primary_key=True)
    id_materia = models.ForeignKey(Materia,on_delete=models.CASCADE)
    id_usuario = models.ForeignKey(Usuarios,on_delete=models.CASCADE)
    estado = models.CharField(max_length=3,default="A")

class Asistencia(models.Model):
    id = models.AutoField(primary_key=True)
    total_asistencia = models.IntegerField(default = 0)
    minimo_asistencia = models.IntegerField(default = 80)
    estado = models.CharField(max_length=3,default="A")

class AulaVirutal(models.Model):
    id = models.AutoField(primary_key=True)
    id_asistencia = models.ForeignKey(Asistencia,on_delete=models.CASCADE)
    id_estudiante = models.ForeignKey(Usuarios,on_delete=models.CASCADE)
    id_asignacion_materia = models.ForeignKey(AsignacionMaterias,on_delete=models.CASCADE)
    aprobado = models.CharField(max_length=50,default="-")
    estado = models.CharField(max_length=3,default="A")