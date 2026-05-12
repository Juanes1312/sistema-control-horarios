### Componentes/Módulos → Arquetipos → RF → Interfaces

| Componente / Módulo del Sistema | Arquetipos (Perfiles) | Requisito Funcional (RF) | Interfaces de Usuario (Pantallas / Wireframes) |
| :--- | :--- | :--- | :--- |
| **Módulo de Seguridad y Control de Accesos** | Todos (Admin, Director, Coord, Empleado) | RF-02: Autenticación segura y control de sesión. | P_Login (W-01: Inicio de sesión) <br> P_Perfil (W-13: Gestión de perfil personal) |
| **Módulo Operativo (Control de Asistencia)** | Empleado | RF-04: Captura de tiempo exacto e IP. <br> RF-06: Radicación de solicitudes de permisos. | P_Dashboard_Emp (W-02: Panel operativo / Reloj) <br> P_Solicitud_Permiso (W-03: Formulario de Novedades) |
| **Módulo de Coordinación (Auditoría)** | Coordinador | RF-07: Flujo de aprobación jerárquico. | P_Bandeja_Coordinador (W-04: Bandeja de Equipo y Autorizaciones) |
| **Módulo de Administración RRHH y Configuración** | Administrador, Director | RF-01: Gestión de empresas. <br> RF-03: Gestión de talento humano. <br> RF-05: Parametrización de horarios. <br> RF-12: Mantenimiento de eventos. | P_Gestion_Empresas (W-05) <br> P_Gestion_Empleados (W-06) <br> P_Parametrizacion_Jornada (W-07) <br> P_Calendario_Eventos (W-11) |
| **Módulo de Inventario TI (Control de Software)** | Administrador | RF-10: Control de activos corporativos. <br> RF-11: Trazabilidad de permisos de red. | P_Inventario_Software (W-09: Catálogo TI) <br> P_Asignacion_Accesos (W-10: Matriz de Permisos) |
| **Módulo Gerencial y Reportes (BI)** | Director | RF-08: Exportación de datos para nómina. <br> RF-09: Motor de búsqueda histórica. | P_Reportes_Gerenciales (W-12: Dashboard Analítico / Exportación) |