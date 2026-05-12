### DDL → Modelo Relacional → PK → FK → Restricciones

| Código DDL (Script SQL) | Modelo Relacional (Tabla) | Llave Primaria (PK) | Llave Foránea (FK) | Restricciones de Integridad (Constraints) |
| :--- | :--- | :--- | :--- | :--- |
| **CREATE TABLE tbl_empresas** | Empresa | id_empresa | N/A | nit (UNIQUE, NOT NULL), nombre (NOT NULL). |
| **CREATE TABLE tbl_jornadas** | Jornada | id_jornada | id_empresa | horas_semanales (CHECK <= 48), descripcion (NOT NULL). |
| **CREATE TABLE auth_user** | Usuario (Sistemas) | id | N/A | username (UNIQUE), password (HASHED), is_active (BOOLEAN). |
| **CREATE TABLE asistencia_empleado** | Empleado | id | user_id, id_empresa, id_jornada | documento (UNIQUE), user_id (ONE-TO-ONE), activo (DEFAULT TRUE). |
| **CREATE TABLE asistencia_marcaje** | Marcaje (Asistencia) | id | empleado_id | tipo (CHECK IN 'E', 'R', 'S'), fecha_hora (NOT NULL), ip_origen (NOT NULL). |
| **CREATE TABLE tbl_tipos_permiso** | Tipo de Permiso | id_tipo | N/A | nombre (UNIQUE), requiere_soporte (BOOLEAN). |
| **CREATE TABLE asistencia_novedad** | Novedad / Permiso | id | empleado_id, tipo_id | estado (DEFAULT 'Pendiente'), fecha_inicio (NOT NULL), fecha_fin (> fecha_inicio). |
| **CREATE TABLE tbl_software** | Software | id_software | id_tipo_sw | licencia (NOT NULL), version (NOT NULL). |
| **CREATE TABLE tbl_acceso_software** | Acceso Software | id_acceso | id_software, id_empleado | nivel_permiso (NOT NULL), fecha_asignacion (NOT NULL). |
| **CREATE TABLE tbl_tipos_evento** | Tipo de Evento | id_tipo_ev | N/A | descripcion (NOT NULL). |
| **CREATE TABLE tbl_eventos_empresa** | Registro Eventos | id_evento | id_tipo_ev, id_empresa | fecha_evento (NOT NULL), ubicacion (NOT NULL). |