from django.db import models
from apps.polla.models import Equipo, Usuario

# Create your models here.
class Demarcacion(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return '{}'.format(self.nombre)

class Jugador(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    equipo = models.ForeignKey(Equipo, related_name='equipo', on_delete=models.CASCADE)
    demarcacion = models.ForeignKey(Demarcacion, related_name='Demarcacion', on_delete=models.CASCADE, blank=True, null=True)
    ataque = models.PositiveIntegerField()
    defensa = models.PositiveIntegerField()
    velocidad = models.PositiveIntegerField()

    def __str__(self):
        return '{} {} | {}'.format(self.nombre, self.apellido, self.demarcacion)

class Formaciones(models.Model):
    cantidad_arqueros = models.PositiveIntegerField()
    cantidad_defensas = models.PositiveIntegerField()
    cantidad_centrocampistas = models.PositiveIntegerField()
    cantidad_delanteros = models.PositiveIntegerField()

    def __str__(self):
        return '{} - {} - {}'.format(self.cantidad_defensas, self.cantidad_centrocampistas, self.cantidad_delanteros)

class ParticipacionEquipoIdeal:
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    ataque = models.FloatField()
    defensa = models.FloatField()
    velocidad = models.FloatField()
    total = models.FloatField()
    fecha = models.DateTimeField()

    def __str__(self):
        return '{} / {}'.format(self.usuario, self.fecha)
