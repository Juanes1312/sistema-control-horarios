### Prototipo → Wireframes → Interacciones → Pantallas destino

| Elemento del Prototipo (Hotspot) | Wireframe Origen | Interacción (Evento UX) | Pantalla Destino / Comportamiento del Sistema |
| :--- | :--- | :--- | :--- |
| **Carga de Sistema (Logo)** | Pantalla de Carga (Splash) | Animación Automática | Transición fluida donde las letras se mueven para formar el logo de Virtual Llantas de manera limpia, redirigiendo a W-01 (Login) tras 2 segundos. |
| **Botón [Ingresar al Sistema]** | W-01: Login | Clic / Tap | Valida credenciales y redirige a W-02 (Panel Operativo) o al Dashboard correspondiente según el rol. |
| **Botón [Registrar Entrada]** | W-02: Panel Operativo | Clic / Tap | Despliega Overlay (Ventana Modal) de éxito, deshabilita este botón y habilita el botón [Iniciar Receso]. |
| **Enlace "Olvide mi contraseña"** | W-01: Login | Clic | Redirige a W-01B (Recuperación de Credenciales). |
| **Opción Menú [Bandeja de Equipo]** | W-02 / W-03 (Menú Lateral) | Clic | Navega hacia W-04 (Bandeja de Equipo y Autorizaciones). |
| **Icono [Aprobar ✔] en tabla** | W-04: Bandeja de Equipo | Clic | La fila seleccionada cambia visualmente a estado "Aprobado" y los botones de acción desaparecen. |
| **Icono [Rechazar X] en tabla** | W-04: Bandeja de Equipo | Clic | Despliega Modal obligando a ingresar texto de justificación, luego actualiza la fila a "Rechazado". |
| **Botón [+ Nueva Empresa]** | W-05: Módulo Admin | Clic | Abre formulario emergente para ingresar NIT y Nombre. Al guardar, actualiza la tabla de datos. |
| **Fila de "Empleado" en tabla** | W-06: Gestión Empleados | Doble Clic | Abre W-06B (Ficha Técnica del Empleado) en modo detalle/edición. |
| **Selector de Rango de Fechas** | W-12: Dashboard Analítico | Selección (Dropdown) | Recarga dinámicamente las gráficas de horas laboradas sin cambiar de pantalla. |
| **Botón [Exportar Nómina]** | W-12: Dashboard Analítico | Clic | Inicia la descarga automática del archivo (.XLSX / .PDF) desde el navegador. |
| **Botón [Asignar Licencia]** | W-09: Catálogo Licencias | Clic | Abre W-10 (Matriz de Accesos) prefiltrada con el software seleccionado. |
| **Icono [Perfil / Cerrar Sesión]** | Barra de Navegación Global | Clic | Destruye la sesión activa y redirige inmediatamente a W-01 (Login). |