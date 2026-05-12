### Tablas relacionales → MER → PK → FK → Forma normal

| Tablas Relacionales (Físico) | Entidad MER (Lógico) | Llave Primaria (PK) | Llaves Foráneas (FK) | Forma Normal |
| :--- | :--- | :--- | :--- | :--- |
| **auth_user** | Usuario | id | Ninguna | 3FN |
| **asistencia_empleado** | Empleado | id | user_id (Ref. auth_user.id) | 3FN |
| **asistencia_marcaje** | Marcaje | id | empleado_id (Ref. asistencia_empleado.id) | 3FN |
| **asistencia_novedad** | Novedad/Permiso | id | empleado_id (Ref. asistencia_empleado.id) | 3FN |
| **tbl_empresas** | Empresa | id_empresa | - | 3FN |
| **tbl_jornadas** | Jornada | id_jornada | id_empresa | 3FN |
| **tbl_empleados** | Empleado | id_empleado | id_jornada, id_perfil | 3FN |
| **tbl_permisos** | Permiso | id_permiso | id_empleado, id_tipo | 3FN |