

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema bienes_raices_future
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `bienes_raices_future` ;

-- -----------------------------------------------------
-- Schema bienes_raices_future
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `bienes_raices_future` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `bienes_raices_future` ;

-- -----------------------------------------------------
-- Tabla `bienes_raices_future`.`estado`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `bienes_raices_future`.`estado` (
  `id_Estado` INT NOT NULL,
  `Nombre_Estado` VARCHAR(255) NULL DEFAULT NULL,
  PRIMARY KEY (`id_Estado`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Tabla `bienes_raices_future`.`operatoriacomercial`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `bienes_raices_future`.`operatoriacomercial` (
  `id_operatoria_comercial` INT NOT NULL AUTO_INCREMENT,
  `nombre_operatoria_comercial` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`id_operatoria_comercial`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Tabla `bienes_raices_future`.`propietario`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `bienes_raices_future`.`propietario` (
  `id_Propietario` INT NOT NULL,
  `nombre` VARCHAR(255) NOT NULL,
  `direccion` VARCHAR(255) NOT NULL,
  `contacto` VARCHAR(255) NOT NULL,
  `id_Propiedad` INT NOT NULL,
  PRIMARY KEY (`id_Propietario`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

CREATE UNIQUE INDEX `id_Propiedad` ON `bienes_raices_future`.`propietario` (`id_Propiedad` ASC) VISIBLE;


-- -----------------------------------------------------
-- Tabla `bienes_raices_future`.`tipo`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `bienes_raices_future`.`tipo` (
  `id_Tipo` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `nombre_tipo` VARCHAR(255) NULL DEFAULT NULL,
  PRIMARY KEY (`id_Tipo`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Tabla `bienes_raices_future`.`propiedad`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `bienes_raices_future`.`propiedad` (
  `id_Propiedad` INT NOT NULL,
  `id_tipo` INT UNSIGNED NOT NULL,
  `id_estado` INT NOT NULL,
  `id_operacion_comercial` INT NOT NULL,
  `id_propietario` INT NOT NULL,
  `nombre` VARCHAR(255) NOT NULL,
  `direccion` VARCHAR(255) NOT NULL,
  `contacto` VARCHAR(255) NULL DEFAULT NULL,
  PRIMARY KEY (`id_Propiedad`, `id_tipo`, `id_estado`, `id_operacion_comercial`, `id_propietario`),
  CONSTRAINT `fk_propiedad_estado`
    FOREIGN KEY (`id_estado`)
    REFERENCES `bienes_raices_future`.`estado` (`id_Estado`),
  CONSTRAINT `fk_propiedad_idpropiedad`
    FOREIGN KEY (`id_Propiedad`)
    REFERENCES `bienes_raices_future`.`propietario` (`id_Propiedad`),
  CONSTRAINT `fk_propiedad_OperatoriaComercial`
    FOREIGN KEY (`id_operacion_comercial`)
    REFERENCES `bienes_raices_future`.`operatoriacomercial` (`id_operatoria_comercial`),
  CONSTRAINT `fk_propiedad_propietario`
    FOREIGN KEY (`id_propietario`)
    REFERENCES `bienes_raices_future`.`propietario` (`id_Propietario`),
  CONSTRAINT `fk_propiedad_Tipo`
    FOREIGN KEY (`id_tipo`)
    REFERENCES `bienes_raices_future`.`tipo` (`id_Tipo`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

CREATE INDEX `fk_propiedad_Tipo` ON `bienes_raices_future`.`propiedad` (`id_tipo` ASC) VISIBLE;

CREATE INDEX `fk_propiedad_propietario` ON `bienes_raices_future`.`propiedad` (`id_propietario` ASC) VISIBLE;

CREATE INDEX `fk_propiedad_estado` ON `bienes_raices_future`.`propiedad` (`id_estado` ASC) VISIBLE;

CREATE INDEX `fk_propiedad_OperatoriaComercial` ON `bienes_raices_future`.`propiedad` (`id_operacion_comercial` ASC) VISIBLE;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
