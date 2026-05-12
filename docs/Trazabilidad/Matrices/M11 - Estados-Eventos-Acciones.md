### Estados → Eventos → Acciones → RF/Reglas de negocio

| Estado Inicial (Objeto) | Evento (Gatillo) | Acción del Sistema | Requisito Funcional (RF) / Regla de Negocio (RN) |
| :--- | :--- | :--- | :--- |
| **No Iniciado (Turno)** | El empleado hace clic en "Registrar Entrada". | El sistema captura hora/IP, crea el registro Marcaje y cambia el estado a "En Curso". | RF-04: Captura exacta del tiempo. <br> RN: Un empleado inactivo no puede iniciar turno. |
| **En Curso (Turno)** | El empleado hace clic en "Iniciar Receso". | Se registra el evento tipo 'R' y el estado del turno pasa a "En Pausa". | RF-04: Registro de pausas activas o almuerzo. <br> RN: Solo se puede iniciar receso si el turno está "En Curso". |
| **En Pausa (Turno)** | El empleado hace clic en "Registrar Entrada" (retorno). | Se registra el retorno y el estado vuelve a "En Curso". | RF-04: Trazabilidad de tiempos de descanso. |
| **En Curso (Turno)** | El empleado hace clic en "Registrar Salida". | Se registra el evento tipo 'S', se calcula el tiempo total trabajado y el estado pasa a "Finalizado". | RF-04: Fin de jornada. <br> RN: No se puede registrar salida sin una entrada previa. |
| **Nueva (Novedad/Permiso)** | El empleado diligencia y envía el formulario. | Se guarda el registro en la BD, cambia a "Pendiente" y se notifica al Coordinador. | RF-06: Radicación de permisos. <br> RN: Toda solicitud nueva nace en estado Pendiente. |
| **Pendiente (Novedad)** | El Coordinador hace clic en "Aprobar". | El estado cambia a "Aprobado" y se envía notificación al empleado. | RF-07: Flujo de aprobación. <br> RN: Solo perfiles de Coordinador/Director pueden aprobar. |
| **Pendiente (Novedad)** | El Coordinador hace clic en "Rechazar". | El estado cambia a "Rechazado" y el sistema exige un campo de observación/motivo. | RF-07: Flujo de aprobación. <br> RN: Todo rechazo debe estar justificado. |
| **Aprobado (Novedad)** | El empleado hace clic en "Cancelar Solicitud". | El estado cambia a "Cancelado" y se libera el tiempo en el reporte de horas. | RF-06: Gestión de permisos. <br> RN: Un permiso finalizado o en curso no se puede cancelar. |
| **Activo (Empleado)** | El Administrador inactiva el perfil desde el panel. | El estado cambia a "Inhabilitado", se revocan accesos web y se cierran sesiones activas. | RF-03: Gestión de talento humano. <br> RN: Bloqueo inmediato de accesos tras desvinculación. |
| **Asignado (Acceso SW)** | El Administrador revoca la licencia en el sistema. | El estado del acceso cambia a "Inhabilitado" y se registra la fecha de revocación. | RF-11: Control de software. <br> RN: Liberación de licencias corporativas. |
| **Programado (Evento)** | La fecha/hora del sistema alcanza la fecha del evento. | El estado del evento corporativo cambia a "En Curso". | RF-12: Calendario corporativo. |
| **En Curso (Evento)** | La fecha/hora del sistema supera la fecha de fin. | El estado cambia automáticamente a "Finalizado". | RF-12: Mantenimiento del catálogo de eventos. |