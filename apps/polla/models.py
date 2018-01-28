from django.db import models

# Create your models here.
class Usuario(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    tipo = models.PositiveIntegerField()

    def __str__(self):
        return '{}'.format(self.username)

class Equipo(models.Model):
    nombre = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)

    def __str__(self):
        return '{}'.format(self.nombre)

class Partido(models.Model):
    eq_local = models.ForeignKey(Equipo, related_name='equipo_local', on_delete=models.CASCADE)
    eq_visita = models.ForeignKey(Equipo, related_name='equipo_visita', on_delete=models.CASCADE)
    resultado = models.PositiveIntegerField()
    fecha = models.DateTimeField()

    def __str__(self):
        return '{} vs {}'.format(self.eq_local, self.eq_visita)

class ParticipacionPolla(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    score = models.IntegerField()
    fecha = models.DateTimeField()

    def __str__(self):
        return '{} / {}'.format(self.usuario, self.fecha)

class Polla(models.Model):
    participacion = models.ForeignKey(ParticipacionPolla, on_delete=models.CASCADE)
    partido = models.ForeignKey(Partido, on_delete=models.CASCADE)
    resultado = models.PositiveIntegerField()
