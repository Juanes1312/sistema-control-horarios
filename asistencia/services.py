from .models import Marcaje, Empleado

class AsistenciaService:
    @staticmethod
    def registrar_evento(user, tipo_evento, ip_origen):
        # 1. Verificar que el usuario tenga un perfil de Empleado
        try:
            empleado = user.empleado
        except Empleado.DoesNotExist:
            return False, "Error: Tu usuario no tiene un perfil de empleado asignado."

        # 2. Regla de negocio: Verificar si el empleado está activo
        if not empleado.activo:
            return False, "Error: Tu usuario se encuentra inactivo."

        # 3. Crear el registro en la base de datos
        Marcaje.objects.create(
            empleado=empleado,
            tipo=tipo_evento,
            ip_origen=ip_origen
        )
        
        return True, "¡Asistencia registrada con éxito!"