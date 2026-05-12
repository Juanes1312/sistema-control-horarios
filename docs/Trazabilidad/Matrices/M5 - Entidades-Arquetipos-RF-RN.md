### Entidades → Arquetipos → RF → Reglas de negocio

| Entidades (MER) | Arquetipos (Perfiles) | Requisito Funcional (RF) | Reglas de Negocio |
| :--- | :--- | :--- | :--- |
| **Empleado** | Administrador | RF-01: Gestión de perfiles. | RN-01: El documento de identidad debe ser único en todo el sistema. |
| **Marcaje** | Operativo (Empleado) | RF-04: Registro de tiempos. | RN-02: Un empleado en estado "Inactivo" no puede registrar entradas ni salidas. |
| **Novedad/Permiso** | Coordinador | RF-07: Flujo de aprobación. | RN-03: Solo el perfil Coordinador o superior puede cambiar el estado de un permiso a "Aprobado". |
| **Usuario (Auth)** | Todos los roles | RF-02: Autenticación. | RN-04: Todo empleado debe tener un usuario activo para acceder al Dashboard. |
| **Empresa** | Administrador | RF-01: Gestión de empresas. | La empresa debe tener un NIT válido y único. |
| **Jornada** | Director / Coord. | RF-03: Definición de horarios. | La jornada no puede exceder las 48 horas semanales legales. |
| **Permiso** | Empleado / Coord. | RF-06: Solicitud de permisos. | Las solicitudes deben radicarse con al menos 24h de antelación. |
| **Software** | Administrador | RF-10: Control de activos. | Solo se registran software con licencia corporativa vigente. |