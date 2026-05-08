# Sistema de Control de Horarios (SCH) - Virtual Llantas

## ¿Qué módulo implementas?
En este repositorio se implementa el **Módulo Central de Asistencia**, el cual se encarga de gestionar el registro diario de los tiempos de los empleados (entradas, salidas y recesos), validando la ubicación de red (IP) y el estado activo del trabajador.

## ¿Qué tablas cubre tu módulo?
El módulo cubre principalmente las siguientes tablas del Modelo Entidad-Relación:
- `asistencia_empleado` (Extensión del usuario del sistema con datos laborales).
- `asistencia_marcaje` (Registro transaccional de tiempos con trazabilidad de IP).
- `auth_user` (Tabla nativa de autenticación).

## ¿Qué framework elegiste y por qué?
Se eligió **Django (Python)** por las siguientes razones:
1. **Filosofía "Batteries Included":** Proporciona un panel de administración robusto de forma nativa, lo que aceleró la gestión de empleados sin necesidad de programar CRUDs desde cero.
2. **Manejo de Tiempos:** Excelente soporte nativo para zonas horarias (configurado en `America/Bogota`), algo crítico para un sistema de horarios.
3. **ORM Potente:** Permite mapear fácilmente el modelo relacional a la base de datos MySQL, previniendo inyecciones SQL.

## ¿Cómo ejecutar el proyecto?
Sigue estos pasos para levantar el entorno local:
1. Clona este repositorio: `git clone <URL_DEL_REPO>`
2. Crea y activa el entorno virtual: `python3 -m venv venv` y luego `source venv/bin/activate`
3. Instala las dependencias: `pip install -r requirements.txt` *(Nota: en Linux, asegúrate de tener instalados `pkg-config` y `libmysqlclient-dev` para el conector de MySQL).*
4. Crea una base de datos en MySQL llamada `sistema_control_horarios`.
5. Ejecuta las migraciones: `python manage.py migrate`
6. Levanta el servidor: `python manage.py runserver`

## ¿Cuál es el repositorio de tu compañero?
[Enlace al repositorio de mi compañero - Nombre de tu compañero] 
*(Nota: Reemplaza esto con el link real si aplica en tu equipo de trabajo).*
