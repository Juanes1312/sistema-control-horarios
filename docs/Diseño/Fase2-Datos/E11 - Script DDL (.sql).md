Script DDL

-- =============================================================
-- SCRIPT DDL: SISTEMA DE CONTROL DE HORARIOS (SCH)
-- EMPRESA: VIRTUAL LLANTAS
-- =============================================================

-- 1. CREACIÓN DE LA BASE DE DATOS
CREATE DATABASE IF NOT EXISTS sistema_control_horarios;
USE sistema_control_horarios;

-- =============================================================
-- 2. CREACIÓN DE TABLAS (ORDENADAS POR DEPENDENCIAS)
-- =============================================================

-- TABLA: ROL
-- Almacena los niveles de acceso: Administrador, Director, Coordinador, Operativo.
CREATE TABLE ROL (
    id_rol INT AUTO_INCREMENT PRIMARY KEY,
    nombre_rol VARCHAR(30) NOT NULL UNIQUE,
    descripcion VARCHAR(150),
    INDEX (nombre_rol)
) ENGINE=InnoDB COMMENT='Catálogo de roles y jerarquías del sistema';

-- TABLA: JORNADA
-- Define las metas de horas mensuales y días laborales.
CREATE TABLE JORNADA (
    id_jornada INT AUTO_INCREMENT PRIMARY KEY,
    nombre_jornada VARCHAR(50) NOT NULL,
    horas_mensuales INT NOT NULL,
    dias_laborables VARCHAR(100) NOT NULL
) ENGINE=InnoDB COMMENT='Configuración de reglas de tiempo laboral';

-- TABLA: TIPO_MARCAJE
-- Catálogo estático: Entrada, Salida, Receso 1, Receso 2.
CREATE TABLE TIPO_MARCAJE (
    id_tipo_marcaje INT AUTO_INCREMENT PRIMARY KEY,
    nombre_tipo VARCHAR(20) NOT NULL
) ENGINE=InnoDB COMMENT='Tipos de registros de tiempo diarios';

-- TABLA: TIPO_PERMISO
-- Catálogo de motivos: Médica, Luto, Personal, Vacaciones.
CREATE TABLE TIPO_PERMISO (
    id_tipo_permiso INT AUTO_INCREMENT PRIMARY KEY,
    nombre_tipo VARCHAR(30) NOT NULL
) ENGINE=InnoDB COMMENT='Motivos para la radicación de novedades';

-- TABLA: ESTADO_PERMISO
-- Flujo de aprobación: Pendiente, Aprobado, Rechazado.
CREATE TABLE ESTADO_PERMISO (
    id_estado INT AUTO_INCREMENT PRIMARY KEY,
    nombre_estado VARCHAR(20) NOT NULL
) ENGINE=InnoDB COMMENT='Estados del flujo de aprobación de permisos';

-- TABLA: EMPLEADO
-- Información demográfica y vinculación a jornada.
CREATE TABLE EMPLEADO (
    id_empleado INT AUTO_INCREMENT PRIMARY KEY,
    documento VARCHAR(20) NOT NULL UNIQUE,
    nombres VARCHAR(50) NOT NULL,
    apellidos VARCHAR(50) NOT NULL,
    correo VARCHAR(100) NOT NULL UNIQUE,
    telefono VARCHAR(15),
    fecha_contratacion DATE NOT NULL,
    id_jornada INT NOT NULL,
    estado_activo BOOLEAN NOT NULL DEFAULT 1,
    CONSTRAINT fk_empleado_jornada FOREIGN KEY (id_jornada) REFERENCES JORNADA(id_jornada)
) ENGINE=InnoDB COMMENT='Datos maestros del personal de Virtual Llantas';

-- TABLA: USUARIO
-- Credenciales de acceso ligadas al empleado y rol.
CREATE TABLE USUARIO (
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    id_empleado INT NOT NULL,
    id_rol INT NOT NULL,
    username VARCHAR(50) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    ultimo_login DATETIME,
    estado_activo BOOLEAN NOT NULL DEFAULT 1,
    CONSTRAINT fk_usuario_empleado FOREIGN KEY (id_empleado) REFERENCES EMPLEADO(id_empleado),
    CONSTRAINT fk_usuario_rol FOREIGN KEY (id_rol) REFERENCES ROL(id_rol)
) ENGINE=InnoDB COMMENT='Gestión de credenciales y seguridad de acceso';

-- TABLA: MARCAJE
-- Registros de tiempo capturados.
CREATE TABLE MARCAJE (
    id_marcaje INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario INT NOT NULL,
    id_tipo_marcaje INT NOT NULL,
    fecha_hora_exacta DATETIME NOT NULL,
    ip_origen VARCHAR(45) NOT NULL,
    CONSTRAINT fk_marcaje_usuario FOREIGN KEY (id_usuario) REFERENCES USUARIO(id_usuario),
    CONSTRAINT fk_marcaje_tipo FOREIGN KEY (id_tipo_marcaje) REFERENCES TIPO_MARCAJE(id_tipo_marcaje)
) ENGINE=InnoDB COMMENT='Registro de asistencias y tiempos reales';

-- TABLA: PERMISO
-- Gestión de novedades y aprobaciones.
CREATE TABLE PERMISO (
    id_permiso INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario_solicita INT NOT NULL,
    id_usuario_evalua INT,
    id_tipo_permiso INT NOT NULL,
    id_estado INT NOT NULL,
    fecha_inicio DATE NOT NULL,
    fecha_fin DATE NOT NULL,
    motivo_texto TEXT NOT NULL,
    CONSTRAINT fk_permiso_solicita FOREIGN KEY (id_usuario_solicita) REFERENCES USUARIO(id_usuario),
    CONSTRAINT fk_permiso_evalua FOREIGN KEY (id_usuario_evalua) REFERENCES USUARIO(id_usuario),
    CONSTRAINT fk_permiso_tipo FOREIGN KEY (id_tipo_permiso) REFERENCES TIPO_PERMISO(id_tipo_permiso),
    CONSTRAINT fk_permiso_estado FOREIGN KEY (id_estado) REFERENCES ESTADO_PERMISO(id_estado)
) ENGINE=InnoDB COMMENT='Solicitudes de ausencias y seguimiento de novedades';

-- TABLA: ACCESO_IP
-- Lista blanca de IPs autorizadas.
CREATE TABLE ACCESO_IP (
    id_acceso INT AUTO_INCREMENT PRIMARY KEY,
    direccion_ip VARCHAR(45) NOT NULL UNIQUE,
    alias_equipo VARCHAR(50),
    estado_bloqueo BOOLEAN NOT NULL DEFAULT 0
) ENGINE=InnoDB COMMENT='Restricciones de seguridad por red';

-- TABLA: EVENTO_AUDITORIA
-- Log de acciones para cumplimiento de seguridad.
CREATE TABLE EVENTO_AUDITORIA (
    id_evento INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario INT NOT NULL,
    modulo_afectado VARCHAR(50) NOT NULL,
    accion_realizada VARCHAR(50) NOT NULL,
    fecha_hora DATETIME NOT NULL,
    CONSTRAINT fk_auditoria_usuario FOREIGN KEY (id_usuario) REFERENCES USUARIO(id_usuario)
) ENGINE=InnoDB COMMENT='Histórico de eventos para auditoría técnica';

-- =============================================================
-- 3. DATOS DE PRUEBA (INSERT BÁSICOS)
-- =============================================================

-- Insertar Roles
INSERT INTO ROL (nombre_rol, descripcion) VALUES 
('Administrador', 'Control total técnico y de seguridad'),
('Director', 'Consulta de reportes y gestión gerencial'),
('Coordinador', 'Gestión de equipos y aprobación de permisos'),
('Operativo', 'Registro de marcajes y solicitudes de permisos');

-- Insertar Jornadas
INSERT INTO JORNADA (nombre_jornada, horas_mensuales, dias_laborables) VALUES 
('Administrativa L-V', 160, 'Lunes a Viernes'),
('Operativa Completa', 192, 'Lunes a Sábado');

-- Insertar Catálogos de Marcaje y Permiso
INSERT INTO TIPO_MARCAJE (nombre_tipo) VALUES ('Entrada'), ('Receso 1'), ('Receso 2'), ('Salida');
INSERT INTO TIPO_PERMISO (nombre_tipo) VALUES ('Cita Médica'), ('Calamidad'), ('Vacaciones'), ('Luto');
INSERT INTO ESTADO_PERMISO (nombre_estado) VALUES ('Pendiente'), ('Aprobado'), ('Rechazado');

-- Insertar Empleado y Usuario de Prueba (Admin)
INSERT INTO EMPLEADO (documento, nombres, apellidos, correo, fecha_contratacion, id_jornada) 
VALUES ('12345678', 'Juan', 'Rincón', 'juan.rincon@virtualllantas.com', '2024-01-15', 1);

INSERT INTO USUARIO (id_empleado, id_rol, username, password_hash) 
VALUES (1, 1, 'admin_jrincon', 'hash_seguro_de_prueba');

-- Insertar una IP permitida
INSERT INTO ACCESO_IP (direccion_ip, alias_equipo) VALUES ('192.168.1.50', 'Servidor Central');
