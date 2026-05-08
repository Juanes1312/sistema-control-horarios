# Registro de Decisiones de Arquitectura (ADR)

## Decisión #01
**¿Qué decidí?**
Implementar una separación estricta de responsabilidades mediante una Arquitectura de 3 Capas dentro del patrón estándar de Django (Modelo-Vista-Template), creando un archivo específico `services.py` (Capa de Lógica).

**¿Por qué?**
Para evitar el "Anti-patrón" de *Fat Views* (Vistas pesadas). Al aislar la lógica de validación de IP y el estado del empleado en un "Service", el código se vuelve reutilizable. Si en el futuro se desea crear una API móvil o implementar un reloj biométrico, se puede reutilizar la misma lógica de negocio sin tocar el código web (HTML).

**¿Qué artefacto de diseño respalda esta decisión?**
El **Diagrama de Componentes UML** estructurado inicialmente en el documento de arquitectura, donde se especifica claramente un componente para la interfaz y un módulo de Lógica Core independiente.

**Trazabilidad Diseño → Código:**
- **Diseño:** Diagrama de Clases Detallado (Clase `AsistenciaService` y Clase `Marcaje`).
- **Requisito:** RNF-05 (Seguridad por IP).
- **Código:** Implementado físicamente en el archivo `asistencia/services.py`, método `registrar_evento()`, donde se evalúan las reglas antes de llamar a `models.py` para la persistencia.