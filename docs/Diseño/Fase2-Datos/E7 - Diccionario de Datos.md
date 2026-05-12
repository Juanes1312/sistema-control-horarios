# Diccionario de Datos - Sistema de Control de Horarios (SCH)

### Entidad: EMPLEADO
| Atributo | Descripción en el sistema | Tipo de Dato | Restricciones |
| :--- | :--- | :--- | :--- |
| id_empleado | Identificador único del empleado. | INT | PK, NOT NULL |
| documento | Número de cédula de ciudadanía. | VARCHAR(20) | UNIQUE, NOT NULL |
| nombres | Nombres completos. | VARCHAR(50) | NOT NULL |
| apellidos | Apellidos completos. | VARCHAR(50) | NOT NULL |
| correo | Correo electrónico corporativo. | VARCHAR(100) | UNIQUE, NOT NULL |
| id_jornada | Enlace a la meta de horas asignada. | INT | FK, NOT NULL |
| estado_activo | Define si el empleado labora actualmente. | BOOLEAN | NOT NULL |

---

### Entidad: USUARIO
| Atributo | Descripción en el sistema | Tipo de Dato | Restricciones |
| :--- | :--- | :--- | :--- |
| id_usuario | Identificador de la cuenta lógica. | INT | PK, NOT NULL |
| id_empleado | Conexión con los datos del empleado. | INT | FK, NOT NULL |
| id_rol | Conexión con el nivel de permisos. | INT | FK, NOT NULL |
| username | Nombre de acceso al sistema. | VARCHAR(50) | UNIQUE, NOT NULL |
| password_hash | Contraseña encriptada por seguridad. | VARCHAR(255) | NOT NULL |

---

### Entidad: ROL
| Atributo | Descripción en el sistema | Tipo de Dato | Restricciones |
| :--- | :--- | :--- | :--- |
| id_rol | Identificador del nivel de jerarquía. | INT | PK, NOT NULL |
| nombre_rol | Nombre del cargo o actor. | VARCHAR(30) | UNIQUE, NOT NULL |

---

### Entidad: JORNADA
| Atributo | Descripción en el sistema | Tipo de Dato | Restricciones |
| :--- | :--- | :--- | :--- |
| id_jornada | Identificador de la regla de horario. | INT | PK, NOT NULL |
| nombre_jornada | Descripción rápida (Ej: "Lun-Vie 8-5"). | VARCHAR(50) | NOT NULL |
| horas_mensuales | Total de horas exigidas al mes. | INT | NOT NULL |

---

### Entidad: MARCAJE
| Atributo | Descripción en el sistema | Tipo de Dato | Restricciones |
| :--- | :--- | :--- | :--- |
| id_marcaje | ID único del evento de tiempo. | INT | PK, NOT NULL |
| id_usuario | Cuenta que realizó el marcaje. | INT | FK, NOT NULL |
| id_tipo_marcaje | Define si fue entrada, salida o receso. | INT | FK, NOT NULL |
| fecha_hora | Momento exacto extraído del servidor. | DATETIME | NOT NULL |
| ip_origen | Dirección de red desde donde se marcó. | VARCHAR(45) | NOT NULL |

---

### Entidad: TIPO_MARCAJE
| Atributo | Descripción en el sistema | Tipo de Dato | Restricciones |
| :--- | :--- | :--- | :--- |
| id_tipo_marcaje | Identificador del momento. | INT | PK, NOT NULL |
| nombre_tipo | (Entrada, Salida, Receso 1, Receso 2). | VARCHAR(20) | NOT NULL |

---

### Entidad: PERMISO
| Atributo | Descripción en el sistema | Tipo de Dato | Restricciones |
| :--- | :--- | :--- | :--- |
| id_permiso | ID único de la novedad radicada. | INT | PK, NOT NULL |
| id_usuario_solicita | Usuario operativo que pide la ausencia. | INT | FK, NOT NULL |
| id_usuario_evalua | Usuario coordinador que aprueba/rechaza. | INT | FK |
| id_tipo_permiso | Motivo de la novedad. | INT | FK, NOT NULL |
| id_estado | Estado actual de la solicitud en el flujo. | INT | FK, NOT NULL |
| fecha_inicio | Día que inicia la ausencia. | DATE | NOT NULL |
| fecha_fin | Día que finaliza la ausencia. | DATE | NOT NULL |
| motivo_texto | Justificación detallada del empleado. | TEXT | NOT NULL |

---

### Entidad: TIPO_PERMISO y ESTADO_PERMISO
| Atributo | Descripción en el sistema | Tipo de Dato | Restricciones |
| :--- | :--- | :--- | :--- |
| id_tipo / id_estado | Identificador (Aplica para ambas tablas). | INT | PK, NOT NULL |
| descripcion | Ej: "Médica" o "Aprobado". | VARCHAR(30) | NOT NULL |

---

### Entidad: ACCESO_IP
| Atributo | Descripción en el sistema | Tipo de Dato | Restricciones |
| :--- | :--- | :--- | :--- |
| id_acceso | Identificador de la regla de seguridad. | INT | PK, NOT NULL |
| direccion_ip | Dirección IPv4 o IPv6 autorizada. | VARCHAR(45) | UNIQUE, NOT NULL |
| estado_bloqueo | 0 = Permitida, 1 = Bloqueada. | BOOLEAN | NOT NULL |

---

### Entidad: EVENTO_AUDITORIA
| Atributo | Descripción en el sistema | Tipo de Dato | Restricciones |
| :--- | :--- | :--- | :--- |
| id_evento | ID único del log en el sistema. | INT | PK, NOT NULL |
| id_usuario | Responsable que ejecutó la acción. | INT | FK, NOT NULL |
| modulo | Sección afectada (Ej: "Gestión Permisos"). | VARCHAR(50) | NOT NULL |
| accion | Ej: "CREATE", "UPDATE", "DELETE". | VARCHAR(50) | NOT NULL |
| fecha_hora | Momento de la modificación. | DATETIME | NOT NULL |