# Bitácora de Desarrollo

## Entrada #01
— **Fecha:** 08/May/2026
— **¿Qué hice?:** Configuración inicial del proyecto con Django. Creación del entorno virtual, conexión a la base de datos MySQL e implementación de la arquitectura de 3 capas (Models, Views, Services) para el Caso de Uso de Registro de Marcaje.
— **¿Qué problema encontré?:** 1. Error al intentar instalar `mysqlclient` en el entorno WSL2 por falta de herramientas de compilación de C (`pkg-config: not found`).
2. Error de conflicto de historiales al hacer el primer `git push` debido a que el repositorio remoto en GitHub tenía un README generado por defecto.
— **¿Cómo lo resolví?:** 1. Instalé las dependencias del sistema operativo (`sudo apt install pkg-config default-libmysqlclient-dev`) antes de volver a ejecutar pip. 
2. Utilicé el comando de forzado local (`--force`) para el primer push, asegurando que el código de mi máquina fuera la fuente de verdad.
— **¿Usé IA?:** Sí.
— **¿Qué ajusté del resultado?:** Ajusté la configuración de la IA para forzar la zona horaria de Colombia (`America/Bogota`) en el archivo `settings.py` y modifiqué el script generado del servicio para capturar la IP real desde las cabeceras HTTP de Django.