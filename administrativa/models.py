from django.db import models

class Perfil(models.Model):
    descripcion = models.CharField(max_length=255)
    estado = models.CharField(max_length=3)

    def __str__(self):
        return self.descripcion

class Usuarios(models.Model):
    img = models.BinaryField()
    cedula = models.CharField(max_length=15)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    clave = models.CharField(max_length=25)
    edad = models.IntegerField()
    genero = models.CharField(max_length=25)
    pais_natal = models.CharField(max_length=100)
    ciudad_natal = models.CharField(max_length=100)
    id_perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    estado = models.CharField(max_length=3)

    def __str__(self):
        return f'{self.nombres} {self.apellidos}'

class EducacionGlobal(models.Model):
    img = models.BinaryField()
    nombres_institucion = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=100)
    referencia_ubicacion = models.CharField(max_length=500)
    estado = models.CharField(max_length=3)

    def __str__(self):
        return self.nombres_institucion
class ConfiguracionEducacionGlobal(models.Model):
    total_asistencia = models.IntegerField()
    id_educacion_global = models.ForeignKey(EducacionGlobal, on_delete=models.CASCADE)
    estado = models.CharField(max_length=3)
    def __str__(self):
        return self.nombres_institucion
class Curso(models.Model):
    numero = models.IntegerField()
    curso = models.CharField(max_length=75)
    estado = models.CharField(max_length=3)

    def __str__(self):
        return self.curso

class Paralelo(models.Model):
    paralelo = models.CharField(max_length=75)
    estado = models.CharField(max_length=3)

    def __str__(self):
        return self.paralelo

class Materia(models.Model):
    materia = models.CharField(max_length=75)
    estado = models.CharField(max_length=3)

    def __str__(self):
        return self.materia

class AulaVirtual(models.Model):
    id_educacion_global = models.ForeignKey(EducacionGlobal, on_delete=models.CASCADE)
    id_materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    id_curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    id_paralelos = models.ForeignKey(Paralelo, on_delete=models.CASCADE)
    tutor = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    estado = models.CharField(max_length=3)

    def __str__(self):
        return f'AulaVirtual {self.id}'
class AulaVirtualEstudiantes(models.Model):
    estudiante = models.ForeignKey(AulaVirtual, on_delete=models.CASCADE)
    cantidad_asistencia = models.FloatField()
    estado = models.CharField(max_length=3)
    def __str__(self):
        return f'AulaVirtualEstudiantes {self.id}'
