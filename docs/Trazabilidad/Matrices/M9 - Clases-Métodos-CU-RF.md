### Clases → Métodos → CU → RF

| Clase (Controlador/Servicio) | Métodos Principales | Caso de Uso (CU) Vinculado | Requisito Funcional (RF) Satisfecho |
| :--- | :--- | :--- | :--- |
| **AuthService** | login(), logout(), validarSesion(), recuperarPassword() | Autenticación y Perfil | RF-02: Autenticación segura y gestión de sesión por roles. |
| **EmpresaController** | crearEmpresa(), modificarEmpresa(), consultar(), inhabilitar() | Gestión de Empresas registradas | RF-01: Mantenimiento del catálogo de empresas (NIT, Nombre). |
| **EmpleadoController** | crearEmpleado(), modificarEmpleado(), consultar(), inhabilitar() | Gestión de Empleados, Tipos y Perfiles | RF-03: Gestión de talento humano y roles operativos/administrativos. |
| **JornadaController** | crearJornada(), asignarHorario(), consultarJornada() | Gestión de Jornada | RF-05: Parametrización de horarios laborales legales. |
| **AsistenciaService** | registrarEntrada(), iniciarReceso(), registrarSalida(), validarIP() | Seguimientos empleados (Marcaje) | RF-04: Captura de tiempo exacto del servidor e integridad de datos. |
| **PermisoController** | crearTipoPermiso(), solicitarPermiso(), consultarEstado(), cancelarSolicitud() | Tipos de permiso y Permisos solicitados | RF-06: Radicación de solicitudes con tipología específica (Médico, Personal). |
| **NovedadService** | evaluarSolicitud(), aprobarNovedad(), rechazarNovedad() | Gestión de Novedades (Evaluación) | RF-07: Flujo de aprobación exclusivo para Coordinador y Director. |
| **SoftwareController** | registrarSoftware(), gestionarTipos(), inhabilitarSoftware() | Tipo de software y Gestión de Software | RF-10: Inventario de activos digitales y licencias corporativas. |
| **AccesoSoftwareService** | asignarAcceso(), revocarAcceso(), consultarAccesos() | Acceso a software | RF-11: Trazabilidad de permisos en herramientas externas. |
| **EventoController** | programarEvento(), gestionarTiposEvento(), consultarEventos() | Tipos de eventos y Registro de eventos empresa | RF-12: Calendario y publicación de eventos corporativos. |
| **ReporteController** | generarInformeHoras(), generarInformeNomina(), exportarPDF() | Gestión de Informes | RF-08: Consolidación de tiempos para sistemas contables. |
| **ConsultaService** | buscarEmpleado(), filtrarJornadas(), filtrarEventos() | Gestión de Consultas | RF-09: Motor de búsqueda y filtrado de registros históricos. |