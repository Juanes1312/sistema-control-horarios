Normalización (3FN)

Demostrar que el diseño lógico propuesto para la base de datos del Sistema de Control de Horarios (SCH) elimina la redundancia de datos y previene anomalías de inserción, actualización y borrado durante su futura implementación, garantizando el cumplimiento de la Tercera Forma Normal (3FN).

Vista No Normalizada (Requisitos del Cliente)
A partir de la recolección de requisitos con Virtual Llantas, si se planteara una estructura plana (tipo hoja de cálculo) para registrar los eventos diarios del sistema, la vista de los datos luciría así:

| ID_Registro | Fecha_Hora_Evento | Tipo_Evento | Doc_Empleado | Nombre_Empleado | Cargo | NIT_Empresa | Nombre_Empresa |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | 2026-05-11 08:00 | Entrada | 102030 | L. Pérez | Operario | 900.123.456 | Virtual Llantas |
| 2 | 2026-05-11 12:00 | Receso | 102030 | L. Pérez | Operario | 900.123.456 | Virtual Llantas |

Esta estructura presenta una alta anomalía de redundancia. Los datos maestros del empleado y de la empresa se repetirán innecesariamente por cada marcaje diario, lo que penalizaría el rendimiento del futuro servidor.

Aplicación de la Primera Forma Normal (1FN)
Regla de Diseño: Garantizar la atomicidad de los atributos y definir una Llave Primaria (PK). 
Acción Propuesta: El modelo propuesto cumple con 1FN dado que no se diseñaron atributos multivaluados (ej. no se guardan múltiples marcajes en un solo campo de texto) y se establece un identificador único transaccional (ID_Registro). No obstante, las dependencias de datos maestros obligan a avanzar a la siguiente forma.

Aplicación de la Segunda Forma Normal (2FN)
Regla de Diseño: Cumplir 1FN y eliminar las dependencias parciales. 
Acción Propuesta: Se proyecta la separación conceptual entre la entidad transaccional (el evento de tiempo) y la entidad maestra (el trabajador). Los datos del empleado no dependen del momento en que marca la entrada, sino de su propia identidad. 
Proyección en 2FN (División lógica):
* Entidad Evento: PK: id_marcaje | fecha_hora | tipo_evento | FK: documento_empleado
* Entidad Sujeto: PK: documento_empleado | nombre | cargo | nit_empresa | nombre_empresa

Aplicación de la Tercera Forma Normal (3FN) - (Modelo Lógico Final)
Regla de Diseño: Cumplir 2FN y eliminar las dependencias transitivas (ningún atributo no clave debe depender de otro atributo no clave).
Acción Propuesta: En la "Entidad Sujeto" proyectada en el paso anterior, el nombre_empresa depende del nit_empresa, generando una dependencia transitiva respecto a la llave principal del empleado. Para solucionar esto en el diseño final, se aísla la información de la empresa en su propia tabla catálogo. 

Modelo Relacional Final Propuesto (Garantizando 3FN):

Entidad 1: Empresas
| Llave Primaria (PK) | Atributos | Dependencia Funcional Validada |
| :--- | :--- | :--- |
| id_empresa | nit, nombre_empresa | Dependen de forma exclusiva y directa de la llave de la empresa. |

Entidad 2: Empleados
| Llave Primaria (PK) | Atributos | Dependencia Funcional Validada |
| :--- | :--- | :--- |
| id_empleado | documento, nombre, cargo, FK: id_empresa | Dependen de forma exclusiva del empleado. La empresa queda como una referencia foránea. |

Entidad 3: Marcajes_Asistencia
| Llave Primaria (PK) | Atributos | Dependencia Funcional Validada |
| :--- | :--- | :--- |
| id_marcaje | fecha_hora, tipo, FK: id_empleado | Dependen de forma exclusiva del evento temporal registrado. |

Justificación de Diseño para Implementación
Al aplicar este proceso de normalización matemática durante la etapa de arquitectura, se garantiza que la futura fase de codificación (DDL) y el despliegue del motor MySQL cuenten con un esquema robusto. Esta estructura en 3FN evitará bloqueos de base de datos y permitirá que el módulo de informes procese miles de registros mensuales de Virtual Llantas sin comprometer la integridad de la información maestra ni saturar el almacenamiento del servidor.