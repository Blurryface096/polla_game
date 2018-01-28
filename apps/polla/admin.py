from django.contrib import admin
from apps.polla.models import Usuario, Equipo, Partido, ParticipacionPolla

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Equipo)
admin.site.register(Partido)
admin.site.register(ParticipacionPolla)
