### Relaciones MER → Cardinalidades → Reglas de negocio

| Relaciones MER | Cardinalidad | Reglas de Negocio Justificativas |
| :--- | :--- | :--- |
| **Usuario "tiene un" Empleado** | 1 a 1 (1:1) | RN-05: Un usuario del sistema (credenciales) corresponde a un único perfil laboral, garantizando la identidad del trabajador. |
| **Empleado "registra" Marcaje** | 1 a Muchos (1:N) | RN-06: Un empleado realiza múltiples marcajes a lo largo del mes (entradas, salidas), pero cada registro de tiempo pertenece a un solo empleado. |
| **Empleado "solicita" Novedad** | 1 a Muchos (1:N) | RN-07: El empleado puede radicar varias solicitudes de permisos en el año, pero cada solicitud está ligada a un único trabajador. |
| **Empresa - Empleado** | 1 : N | Una empresa agrupa múltiples empleados; el empleado solo pertenece a una. |
| **Empleado - Jornada** | N : M | Un empleado puede rotar entre jornadas; una jornada aplica a varios empleados. |
| **Software - Acceso** | 1 : N | Un software puede tener múltiples niveles de acceso definidos. |
| **Empleado - Novedad** | 1 : N | Las novedades son individuales y trazables por historial de empleado. |