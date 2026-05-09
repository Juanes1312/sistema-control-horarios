Técnicas de elicitación

Para el levantamiento, análisis y definición de los requisitos del Sistema de Control de Horarios (SCH) para Virtual Llantas, se empleó una combinación de técnicas de elicitación. Esto permitió capturar las necesidades desde todas las perspectivas de la empresa (gerencial, administrativa y operativa):
1. Entrevista Estructurada
•	¿Con quién se aplicó? Con el Director de la empresa y el Administrador encargado del área técnica/nómina.
•	¿Qué información se obtuvo? Se comprendió la problemática a nivel gerencial. Gracias a esta técnica se definieron las reglas de negocio más críticas: la necesidad de restringir los marcajes únicamente a las direcciones IP de la empresa (para evitar fraudes), la definición de los perfiles de usuario (jerarquías) y la necesidad de generar reportes consolidados automáticos para agilizar el pago de la nómina.
2. Observación Directa del Proceso
•	¿Con quién se aplicó? Con los Coordinadores de área, observando cómo realizaban su trabajo diario de control de personal.
•	¿Qué información se obtuvo? Se evidenció la pérdida de tiempo real que sufrían los coordinadores al tener que consolidar planillas de Excel, WhatsApps y correos sueltos para saber quién había faltado o quién tenía permiso. De esta observación nació el requisito fundamental de crear un "flujo de novedades" interno en el software, donde el empleado solicita el permiso y el coordinador lo aprueba o rechaza con un solo clic. También permitió identificar los 4 momentos exactos de marcaje diario: entrada, receso 1, receso 2 y salida.
3. Análisis Documental
•	¿Con quién se aplicó? Revisión de los formatos físicos y digitales (archivos de Excel) que Virtual Llantas usaba hasta el momento para llevar la asistencia.
•	¿Qué información se obtuvo? Permitió identificar exactamente qué campos de datos debían existir en la nueva base de datos MySQL. Se extrajeron variables como: tipos de documentos, jornadas laborales exactas (horas al mes requeridas) y los tipos de novedades más comunes (citas médicas, calamidades, etc.), asegurando que el nuevo sistema no omitiera ninguna métrica que la empresa ya estuviera midiendo.
