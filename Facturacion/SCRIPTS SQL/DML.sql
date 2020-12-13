USE UNIGRASAS;


----------------------------
-- DML TABLA ROL
----------------------------
INSERT INTO ROL (NOMBRE) VALUES ('administrador');
INSERT INTO ROL (NOMBRE) VALUES ('vendedor');
INSERT INTO ROL (NOMBRE) VALUES ('consulta');


----------------------------
-- DML TABLA GENERO
----------------------------
INSERT INTO GENERO (NOMBRE) VALUES ('Hombre');
INSERT INTO GENERO (NOMBRE) VALUES ('Mujer');


----------------------------
-- DML TABLA TIPOPERSONA
----------------------------
INSERT INTO TIPO_PERSONA(NOMBRE) VALUES ('Persona natural');
INSERT INTO TIPO_PERSONA(NOMBRE) VALUES ('Persona jurídica');


----------------------------
-- DML TABLA EMPRESA
----------------------------
INSERT INTO `UNIGRASAS`.`EMPRESA` (`IDTIPO_PERSONA`, `NIT`, `DIGITO_VERIFICACION`, `RAZON_SOCIAL`, `DIRECCION`, `PAIS`, `CIUDAD`, `CIIU`, `MATRICULA`)
VALUES (2, 830090675, 7, 'UNIGRASAS COLOMBIA S.A.S', 'Carrera 97 # 24c-51', 'Colombia', 'Bogotá', '4631', '01120659');


----------------------------
-- DML TABLA USUARIO
----------------------------
INSERT INTO `UNIGRASAS`.`USUARIO` (`NOMBRE`, `APELLIDO`, `IDGENERO`, `NICKNAME`, `DESCRIPCION`, `IDROL`, `AVATAR`, `CONTRASENA`, `TOKEN`, `IDENTIFICACION`, `IDEMPRESA`, `TELEFONO`, `EMAIL`)
VALUES ('Nardia', 'Unigrasas', 1, 'nardia', 'Administrador del sistema', 1, 'https://wpimg.wallstcn.com/f778738c-e4f8-4870-b634-56703b4acafe.gif', '123456', 'nardia-token', 830090675, 1, 3507259492, 'nardia.unigrasas2015@gmail.com');


----------------------------
-- DML TABLA CLIENTE
----------------------------
INSERT INTO `UNIGRASAS`.`CLIENTE` (`IDTIPO_PERSONA`, `NIT`, `NOMBRE`, `EMAIL`, `TELEFONO`, `F_REGISTRO`)
VALUES (1, 3507259492, 'PRODUCTOS LACTEOS DEL TOLIMA S.A.S', 'gerenciacomercial@maxifritos.com', 3002179843, CURRENT_TIMESTAMP);


----------------------------
-- DML TABLA METODO_PAGO
----------------------------
INSERT INTO `UNIGRASAS`.`METODO_PAGO` (`NOMBRE`) VALUES ('Contado');
INSERT INTO `UNIGRASAS`.`METODO_PAGO` (`NOMBRE`) VALUES ('Crédito');


----------------------------
-- DML TABLA MEDIO_PAGO
----------------------------
INSERT INTO `UNIGRASAS`.`MEDIO_PAGO` (`NOMBRE`) VALUES ('Transferencia débito bancaria');
INSERT INTO `UNIGRASAS`.`MEDIO_PAGO` (`NOMBRE`) VALUES ('Consignación bancaria');
INSERT INTO `UNIGRASAS`.`MEDIO_PAGO` (`NOMBRE`) VALUES ('PSE');


----------------------------
-- DML TABLA ITEM
----------------------------
INSERT INTO `UNIGRASAS`.`ITEM` (`COD_ITEM`, `NOMBRE`, `PRECIO`, `DESCRIPCION`) VALUES (10001, 'MARGARINA INDUSTRIAL AVELLANA T.C', 1, '');


----------------------------
-- DML TABLA FACTURA
----------------------------
INSERT INTO `UNIGRASAS`.`FACTURA` (`IDCLIENTE`, `IDMETODO_PAGO`, `IDMEDIO_PAGO`, `IDUSUARIO`, `DIVISA`, `F_EMISION`, `F_VENCIMIENTO`, `F_PAGO`, `TOTAL`, `DESCRIPCION`)
VALUES (1, 1, 3, 1, 'COP - Colombia, Pesos', CURRENT_TIMESTAMP, NULL, NULL, 0, '');

----------------------------
-- DML TABLA FACTURA_HAS_ITEM
----------------------------
INSERT INTO `UNIGRASAS`.`FACTURA_HAS_ITEM` (`IDFACTURA`, `IDITEM`, `CANTIDAD`) VALUES (1, 1, 120);