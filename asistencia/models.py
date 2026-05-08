from django.db import models
from django.contrib.auth.models import User

class Empleado(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    documento = models.CharField(max_length=20, unique=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

class Marcaje(models.Model):
    TIPOS = [('E', 'Entrada'), ('R', 'Receso'), ('S', 'Salida')]
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=1, choices=TIPOS)
    fecha_hora = models.DateTimeField(auto_now_add=True)
    ip_origen = models.GenericIPAddressField()

    def __str__(self):
        return f"{self.empleado} - {self.tipo} - {self.fecha_hora}"