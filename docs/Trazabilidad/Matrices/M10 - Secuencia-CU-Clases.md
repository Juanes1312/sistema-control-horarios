### Diagramas de secuencia → CU → Clases → Flujos alternativos

| Diagramas de Secuencia (DS) | Caso de Uso (CU) Relacionado | Clases Involucradas | Flujos Alternativos (Rutas de Excepción) |
| :--- | :--- | :--- | :--- |
| **DS_01_Autenticacion** | Autenticación y Perfil | AuthService, Usuario, SessionManager | A1: Credenciales inválidas (mostrar error). <br> A2: Usuario inactivo/bloqueado (denegar acceso). |
| **DS_02_GestionEmpresa** | Gestión de Empresas registradas | EmpresaController, EmpresaRepository | A1: Intento de registro con NIT duplicado. <br> A2: Cancelación de la operación antes de guardar. |
| **DS_03_GestionEmpleado** | Gestión de Empleados y Tipos | EmpleadoController, AuthService, Perfil | A1: Documento de identidad ya existe. <br> A2: Creación de empleado sin asignar una jornada válida. |
| **DS_04_ParametrizarJornada** | Gestión de Jornada | JornadaController, Jornada | A1: El total de horas excede el máximo legal permitido (48h). <br> A2: Cruce o superposición de turnos. |
| **DS_05_RegistrarMarcaje** | Seguimientos empleados (Eventos) | AsistenciaService, Marcaje, Empleado | A1: La IP de origen no coincide con la red permitida. <br> A2: Intento de "Salida" sin tener una "Entrada" previa. <br> A3: Empleado en estado inhabilitado intenta marcar. |
| **DS_06_SolicitudPermiso** | Tipos de permiso, Permisos solicitados | PermisoController, Permiso | A1: Falta adjuntar documento soporte (ej. excusa médica). <br> A2: Fechas de inicio y fin son ilógicas (fin antes que inicio). |
| **DS_07_EvaluacionNovedad** | Gestión de Novedades | NovedadService, Permiso, Notificacion | A1: El Coordinador rechaza la solicitud (debe exigir justificación). <br> A2: El empleado cancela la solicitud antes de ser evaluada. |
| **DS_08_ControlSoftware** | Tipo de software, Gestión de Software | SoftwareController, Software | A1: Intento de registrar un software con licencia ya expirada. <br> A2: Omisión de campos obligatorios (versión, fabricante). |
| **DS_09_AsignacionAcceso** | Acceso a software | AccesoSoftwareService, Empleado | A1: El empleado ya posee un acceso activo a ese software. <br> A2: Intento de asignar acceso a un empleado inhabilitado. |
| **DS_10_ProgramarEvento** | Tipos de eventos, Eventos empresa | EventoController, Evento | A1: Conflicto de horarios con otro evento corporativo global. <br> A2: El tipo de evento seleccionado ha sido inhabilitado. |
| **DS_11_GeneracionInformes** | Gestión de Informes (Nómina, Horas) | ReporteController, ConsultaService | A1: No hay datos de marcajes en el rango de fechas seleccionado. <br> A2: Error de conexión al intentar exportar el consolidado a PDF/Excel. |
| **DS_12_MotorConsultas** | Gestión de consultas | ConsultaService, FiltroDinamico | A1: Criterios de búsqueda vacíos (retorna todo por defecto). <br> A2: Búsqueda de empleado que no existe en la base de datos. |