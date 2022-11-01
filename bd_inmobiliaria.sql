CREATE DATABASE IF NOT EXISTS inmobiliaria;

use inmobiliaria;

create table tipo (
    id_tipo int not null auto_increment primary key,
    nombre_tipo varchar(50)
);

create table estado(
    id_estado int not null auto_increment primary key,
    nombre_estado varchar(50)
);

create table operatoria_comercial(
    id_operatoria_comercial int not null auto_increment primary key,
    nombre_operatoria_comercial varchar(50)
);

create table propietario(
    id_propietario int not null auto_increment primary key,
    nombre varchar(50),
    direccion varchar(50),
    contacto varchar(50),
    id_propiedad  int not null
);

CREATE TABLE propiedad(
    id_propiedad int AUTO_INCREMENT PRIMARY KEY,
    id_tipo int NOT NULL,
    id_estado int not null,
    id_operatoria_comercial int not null,
    id_propietario int not null,
    nombre varchar(100) not null,
    direccion varchar(100) not null,
    contacto varchar(100) not null,
    FOREIGN KEY (id_tipo) REFERENCES tipo(id_tipo),
    FOREIGN KEY (id_estado) REFERENCES estado(id_estado),
    FOREIGN KEY (id_operatoria_comercial) REFERENCES operatoria_comercial(id_operatoria_comercial),
    FOREIGN KEY (id_propietario) REFERENCES propietario(id_propietario)
);

ALTER TABLE propietario ADD CONSTRAINT `fk_propiedad` FOREIGN KEY (id_propiedad) REFERENCES propiedad (id_propiedad);