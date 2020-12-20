----------------------------
-- DDL TABLA ETAPA
----------------------------
CREATE DATABASE UNIGRASAS;

USE UNIGRASAS;

SHOW TABLES;

-- -----------------------------------------------------
-- TABLE `UNIGRASAS`.`TIPO_PERSONA`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `UNIGRASAS`.`TIPO_PERSONA` (
  `IDTIPO_PERSONA` INT NOT NULL AUTO_INCREMENT,
  `NOMBRE` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`IDTIPO_PERSONA`))
ENGINE = INNODB
DEFAULT CHARACTER SET = UTF8MB4
COLLATE = UTF8MB4_0900_AI_CI;


-- -----------------------------------------------------
-- TABLE `UNIGRASAS`.`CLIENTE`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `UNIGRASAS`.`CLIENTE` (
  `IDCLIENTE` INT NOT NULL AUTO_INCREMENT,
  `IDTIPO_PERSONA` INT NOT NULL,
  `NIT` DOUBLE NULL DEFAULT NULL,
  `NOMBRE` VARCHAR(45) NULL DEFAULT NULL,
  `EMAIL` VARCHAR(45) NULL DEFAULT NULL,
  `TELEFONO` DOUBLE NULL DEFAULT NULL,
  `F_REGISTRO` DATETIME NULL DEFAULT NULL,
  PRIMARY KEY (`IDCLIENTE`),
  INDEX `FK_CLIENTE_TIPO_PERSONA1_IDX` (`IDTIPO_PERSONA` ASC) VISIBLE,
  CONSTRAINT `FK_CLIENTE_TIPO_PERSONA1`
    FOREIGN KEY (`IDTIPO_PERSONA`)
    REFERENCES `UNIGRASAS`.`TIPO_PERSONA` (`IDTIPO_PERSONA`))
ENGINE = INNODB
DEFAULT CHARACTER SET = UTF8MB4
COLLATE = UTF8MB4_0900_AI_CI;


-- -----------------------------------------------------
-- TABLE `UNIGRASAS`.`EMPRESA`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `UNIGRASAS`.`EMPRESA` (
  `IDEMPRESA` INT NOT NULL AUTO_INCREMENT,
  `IDTIPO_PERSONA` INT NOT NULL,
  `NIT` INT NULL DEFAULT NULL,
  `DIGITO_VERIFICACION` INT NULL DEFAULT NULL,
  `RAZON_SOCIAL` VARCHAR(45) NULL DEFAULT NULL,
  `DIRECCION` VARCHAR(45) NULL DEFAULT NULL,
  `PAIS` VARCHAR(45) NULL DEFAULT NULL,
  `CIUDAD` VARCHAR(45) NULL DEFAULT NULL,
  `CIIU` VARCHAR(45) NULL DEFAULT NULL,
  `MATRICULA` INT NULL DEFAULT NULL,
  PRIMARY KEY (`IDEMPRESA`),
  INDEX `FK_EMPRESA_TIPO_PERSONA1_IDX` (`IDTIPO_PERSONA` ASC) VISIBLE,
  CONSTRAINT `FK_EMPRESA_TIPO_PERSONA1`
    FOREIGN KEY (`IDTIPO_PERSONA`)
    REFERENCES `UNIGRASAS`.`TIPO_PERSONA` (`IDTIPO_PERSONA`))
ENGINE = INNODB
DEFAULT CHARACTER SET = UTF8MB4
COLLATE = UTF8MB4_0900_AI_CI;


-- -----------------------------------------------------
-- TABLE `UNIGRASAS`.`MEDIO_PAGO`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `UNIGRASAS`.`MEDIO_PAGO` (
  `IDMEDIO_PAGO` INT NOT NULL AUTO_INCREMENT,
  `NOMBRE` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`IDMEDIO_PAGO`))
ENGINE = INNODB
DEFAULT CHARACTER SET = UTF8MB4
COLLATE = UTF8MB4_0900_AI_CI;


-- -----------------------------------------------------
-- TABLE `UNIGRASAS`.`METODO_PAGO`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `UNIGRASAS`.`METODO_PAGO` (
  `IDMETODO_PAGO` INT NOT NULL AUTO_INCREMENT,
  `NOMBRE` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`IDMETODO_PAGO`))
ENGINE = INNODB
DEFAULT CHARACTER SET = UTF8MB4
COLLATE = UTF8MB4_0900_AI_CI;


-- -----------------------------------------------------
-- TABLE `UNIGRASAS`.`ROL`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `UNIGRASAS`.`ROL` (
  `IDROL` INT NOT NULL AUTO_INCREMENT,
  `NOMBRE` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`IDROL`))
ENGINE = INNODB
DEFAULT CHARACTER SET = UTF8MB4
COLLATE = UTF8MB4_0900_AI_CI;


-- -----------------------------------------------------
-- TABLE `UNIGRASAS`.`GENERO`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `UNIGRASAS`.`GENERO` (
  `IDGENERO` INT NOT NULL AUTO_INCREMENT,
  `NOMBRE` VARCHAR(45) NULL,
  PRIMARY KEY (`IDGENERO`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- TABLE `UNIGRASAS`.`USUARIO`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `UNIGRASAS`.`USUARIO` (
  `IDUSUARIO` INT NOT NULL AUTO_INCREMENT,
  `NOMBRE` VARCHAR(45) NULL DEFAULT NULL,
  `APELLIDO` VARCHAR(45) NULL,
  `IDGENERO` INT NOT NULL,
  `NICKNAME` VARCHAR(45) NULL,
  `DESCRIPCION` VARCHAR(45) NULL DEFAULT NULL,
  `IDROL` INT NOT NULL,
  `AVATAR` LONGTEXT NULL DEFAULT NULL,
  `CONTRASENA` LONGTEXT NULL DEFAULT NULL,
  `TOKEN` VARCHAR(45) NULL DEFAULT NULL,
  `IDENTIFICACION` DOUBLE NULL,
  `IDEMPRESA` INT NOT NULL,
  `TELEFONO` DOUBLE NULL,
  `EMAIL` VARCHAR(45) NULL,
  PRIMARY KEY (`IDUSUARIO`),
  INDEX `FK_USUARIO_EMPRESA1_IDX` (`IDEMPRESA` ASC) VISIBLE,
  INDEX `FK_USUARIO_ROL1_IDX` (`IDROL` ASC) VISIBLE,
  INDEX `FK_USUARIO_GENERO1_IDX` (`IDGENERO` ASC) VISIBLE,
  CONSTRAINT `FK_USUARIO_EMPRESA1`
    FOREIGN KEY (`IDEMPRESA`)
    REFERENCES `UNIGRASAS`.`EMPRESA` (`IDEMPRESA`),
  CONSTRAINT `FK_USUARIO_ROL1`
    FOREIGN KEY (`IDROL`)
    REFERENCES `UNIGRASAS`.`ROL` (`IDROL`),
  CONSTRAINT `FK_USUARIO_GENERO1`
    FOREIGN KEY (`IDGENERO`)
    REFERENCES `UNIGRASAS`.`GENERO` (`IDGENERO`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = INNODB
DEFAULT CHARACTER SET = UTF8MB4
COLLATE = UTF8MB4_0900_AI_CI;


-- -----------------------------------------------------
-- TABLE `UNIGRASAS`.`ESTADO`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `UNIGRASAS`.`ESTADO` (
  `IDESTADO` INT NOT NULL AUTO_INCREMENT,
  `NOMBRE` VARCHAR(45) NULL,
  PRIMARY KEY (`IDESTADO`))
ENGINE = INNODB;


-- -----------------------------------------------------
-- TABLE `UNIGRASAS`.`FACTURA`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `UNIGRASAS`.`FACTURA` (
  `IDFACTURA` INT NOT NULL AUTO_INCREMENT,
  `IDCLIENTE` INT NOT NULL,
  `IDMETODO_PAGO` INT NULL DEFAULT NULL,
  `IDMEDIO_PAGO` INT NULL DEFAULT NULL,
  `IDUSUARIO` INT NOT NULL,
  `IDESTADO` INT NOT NULL,
  `DIVISA` VARCHAR(45) NULL DEFAULT NULL,
  `F_EMISION` DATETIME NULL DEFAULT NULL,
  `F_VENCIMIENTO` DATETIME NULL DEFAULT NULL,
  `F_PAGO` DATETIME NULL DEFAULT NULL,
  `TOTAL` DOUBLE NULL DEFAULT NULL,
  `DESCRIPCION` VARCHAR(45) NULL DEFAULT NULL,
  `F_REGISTRO` DATETIME NULL DEFAULT NULL,
  PRIMARY KEY (`IDFACTURA`),
  INDEX `FK_FACTURA_CLIENTE1_IDX` (`IDCLIENTE` ASC) VISIBLE,
  INDEX `FK_FACTURA_METODO_PAGO1_IDX` (`IDMETODO_PAGO` ASC) VISIBLE,
  INDEX `FK_FACTURA_MEDIO_PAGO1_IDX` (`IDMEDIO_PAGO` ASC) VISIBLE,
  INDEX `FK_FACTURA_USUARIO1_IDX` (`IDUSUARIO` ASC) VISIBLE,
  INDEX `FK_FACTURA_ESTADO1_IDX` (`IDESTADO` ASC) VISIBLE,
  CONSTRAINT `FK_FACTURA_CLIENTE1`
    FOREIGN KEY (`IDCLIENTE`)
    REFERENCES `UNIGRASAS`.`CLIENTE` (`IDCLIENTE`),
  CONSTRAINT `FK_FACTURA_MEDIO_PAGO1`
    FOREIGN KEY (`IDMEDIO_PAGO`)
    REFERENCES `UNIGRASAS`.`MEDIO_PAGO` (`IDMEDIO_PAGO`),
  CONSTRAINT `FK_FACTURA_METODO_PAGO1`
    FOREIGN KEY (`IDMETODO_PAGO`)
    REFERENCES `UNIGRASAS`.`METODO_PAGO` (`IDMETODO_PAGO`),
  CONSTRAINT `FK_FACTURA_USUARIO1`
    FOREIGN KEY (`IDUSUARIO`)
    REFERENCES `UNIGRASAS`.`USUARIO` (`IDUSUARIO`),
  CONSTRAINT `FK_FACTURA_ESTADO1`
    FOREIGN KEY (`IDESTADO`)
    REFERENCES `UNIGRASAS`.`ESTADO` (`IDESTADO`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = INNODB
AUTO_INCREMENT = 1
DEFAULT CHARACTER SET = UTF8MB4
COLLATE = UTF8MB4_0900_AI_CI;


-- -----------------------------------------------------
-- TABLE `UNIGRASAS`.`ITEM`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `UNIGRASAS`.`ITEM` (
  `IDITEM` INT NOT NULL AUTO_INCREMENT,
  `COD_ITEM` DOUBLE NOT NULL,
  `NOMBRE` VARCHAR(45) NOT NULL,
  `PRECIO` INT NULL DEFAULT NULL,
  `DESCRIPCION` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`IDITEM`))
ENGINE = INNODB
DEFAULT CHARACTER SET = UTF8MB4
COLLATE = UTF8MB4_0900_AI_CI;


-- -----------------------------------------------------
-- TABLE `UNIGRASAS`.`FACTURA_HAS_ITEM`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `UNIGRASAS`.`FACTURA_HAS_ITEM` (
  `IDFACTURA` INT NULL,
  `IDITEM` INT NULL,
  `CANTIDAD` INT NULL DEFAULT NULL,
  `PRECIO` INT NULL DEFAULT NULL,
  INDEX `FK_FACTURA_HAS_ITEM_ITEM1_IDX` (`IDITEM` ASC) VISIBLE,
  INDEX `FK_FACTURA_HAS_ITEM_FACTURA1_IDX` (`IDFACTURA` ASC) VISIBLE,
  CONSTRAINT `FK_FACTURA_HAS_ITEM_FACTURA1`
    FOREIGN KEY (`IDFACTURA`)
    REFERENCES `UNIGRASAS`.`FACTURA` (`IDFACTURA`),
  CONSTRAINT `FK_FACTURA_HAS_ITEM_ITEM1`
    FOREIGN KEY (`IDITEM`)
    REFERENCES `UNIGRASAS`.`ITEM` (`IDITEM`))
ENGINE = INNODB
DEFAULT CHARACTER SET = UTF8MB4
COLLATE = UTF8MB4_0900_AI_CI;
