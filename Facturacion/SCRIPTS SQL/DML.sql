TRUNCATE TABLE PROCESO RESTART IDENTITY CASCADE;
TRUNCATE TABLE ETAPA_PROCESO RESTART IDENTITY CASCADE;
TRUNCATE TABLE PROCESO_CAUSAL RESTART IDENTITY CASCADE;
----------------------------
-- DML TABLA ROL
----------------------------
INSERT INTO ROL (DESCRIPCION) VALUES ('administrador');
INSERT INTO ROL (DESCRIPCION) VALUES ('abogado');
INSERT INTO ROL (DESCRIPCION) VALUES ('consulta');

----------------------------
-- DML TABLA USUARIO
----------------------------
INSERT INTO USUARIOS(NOMBRE, APELLIDO, GENERO, NICKNAME, DESCRIPCION, ROL, AVATAR, CONTRASENA, TOKEN) VALUES ('Madia', 'Ortega', 1, 'mortega', 'Directora de investigaciones - Administrador', 1, 'https://wpimg.wallstcn.com/f778738c-e4f8-4870-b634-56703b4acafe.gif', MD5('123456'), 'mortega-token');
INSERT INTO USUARIOS(NOMBRE, APELLIDO, GENERO, NICKNAME, DESCRIPCION, ROL, AVATAR, CONTRASENA, TOKEN) VALUES ('Marco', 'Campaña', 2, 'mcampana', 'Abogado DIEG', 2, 'https://wpimg.wallstcn.com/f778738c-e4f8-4870-b634-56703b4acafe.gif', MD5('123456'), 'mcampana-token');
INSERT INTO USUARIOS(NOMBRE, APELLIDO, GENERO, NICKNAME, DESCRIPCION, ROL, AVATAR, CONTRASENA, TOKEN) VALUES ('Nathalia', 'Pinzon', 1, 'npinzon', 'Abogada DIEG', 2, 'https://wpimg.wallstcn.com/f778738c-e4f8-4870-b634-56703b4acafe.gif', MD5('123456'), 'npinzon-token');
INSERT INTO USUARIOS(NOMBRE, APELLIDO, GENERO, NICKNAME, DESCRIPCION, ROL, AVATAR, CONTRASENA, TOKEN) VALUES ('Juan Camilo', 'Herrera', 2, 'jherrera', 'Abogado DIEG', 2, 'https://wpimg.wallstcn.com/f778738c-e4f8-4870-b634-56703b4acafe.gif', MD5('123456'), 'jherrera-token');

----------------------------
-- DML TABLA TIPOPERSONA
----------------------------
INSERT INTO TIPOPERSONA(NOMBRE) VALUES ('Persona natural');
INSERT INTO TIPOPERSONA(NOMBRE) VALUES ('Persona jurídica');
