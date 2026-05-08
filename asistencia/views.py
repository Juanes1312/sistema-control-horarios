from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .services import AsistenciaService

# Obligamos a que la persona deba haber iniciado sesión para ver esta página
@login_required(login_url='/admin/login/') 
def registrar_marcaje_view(request):
    if request.method == 'POST':
        # Capturamos el botón que presionó (E, S, o R)
        tipo = request.POST.get('tipo')
        
        # Truco de ingeniero: Capturamos la IP real desde donde se conecta
        ip = request.META.get('HTTP_X_FORWARDED_FOR')
        if ip:
            ip = ip.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')

        # Llamamos a nuestra Capa de Lógica
        exito, mensaje = AsistenciaService.registrar_evento(request.user, tipo, ip)

        # Enviamos el mensaje de éxito o error a la pantalla
        if exito:
            messages.success(request, mensaje)
        else:
            messages.error(request, mensaje)

    # Renderizamos la página HTML
    return render(request, 'registro.html')