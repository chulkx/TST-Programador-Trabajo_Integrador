CREATE DATABASE IF NOT EXISTS inmobiliaria;

use inmobiliaria;

create table IF NOT EXISTS tipo (
    id_tipo int not null auto_increment primary key,
    nombre_tipo varchar(50)
);

create table IF NOT EXISTS estado(
    id_estado int not null auto_increment primary key,
    nombre_estado varchar(50)
);

create table IF NOT EXISTS operatoria_comercial(
    id_operatoria_comercial int not null auto_increment primary key,
    nombre_operatoria_comercial varchar(50)
);

create table IF NOT EXISTS propietario(
    id_propietario int not null auto_increment primary key,
    nombre varchar(50),
    direccion varchar(50),
    contacto varchar(50)
);

CREATE TABLE IF NOT EXISTS propiedad(
    id_propiedad int AUTO_INCREMENT PRIMARY KEY,
    id_tipo int NOT NULL,
    id_estado int not null,
    id_operatoria_comercial int not null,
    id_propietario  int not null,
    nombre varchar(100) not null,
    direccion varchar(100) not null,
    contacto varchar(100) not null,
    FOREIGN KEY (id_tipo) REFERENCES tipo(id_tipo),
    FOREIGN KEY (id_estado) REFERENCES estado(id_estado),
    FOREIGN KEY (id_operatoria_comercial) REFERENCES operatoria_comercial(id_operatoria_comercial),
    FOREIGN KEY (id_propietario) REFERENCES propietario(id_propietario)
);


use inmobiliaria;


INSERT INTO propietario VALUES (null, 'Gustavo Godoy', 'Embalse', '1231232332');
INSERT INTO propietario VALUES (null, 'Gus Godoy', 'Embalse', '1234324566');
INSERT INTO propietario VALUES (null, 'G Godoy', 'Embalse', '1234324567');
INSERT INTO propietario VALUES (null, 'Otro Godoy', 'Embalse', '1234324568');
INSERT INTO propietario VALUES (null, 'Mas Godoy', 'Embalse', '1234324569');

INSERT INTO tipo VALUES (null,'Casa');
INSERT INTO tipo VALUES (null,'Departamento');
INSERT INTO tipo VALUES (null,'Quinta');
INSERT INTO tipo VALUES (null,'Duplex');

INSERT INTO estado VALUES (null,'Disponible'); #1
INSERT INTO estado VALUES (null,'No disponible'); #2
INSERT INTO estado VALUES (null, 'Vendida'); #3
INSERT INTO estado VALUES (null, 'Alquilada'); #4

INSERT INTO operatoria_comercial VALUES (null,'Alquiler');
INSERT INTO operatoria_comercial VALUES (null,'Venta');


SELECT p.id_propiedad, t.nombre_tipo, o.nombre_operatoria_comercial, e.nombre_estado, pro.nombre, p.nombre, p.direccion, p.contacto, t.nombre_tipo FROM propiedad as p JOIN tipo as t ON p.id_tipo = t.id_tipo JOIN estado as e ON p.id_estado = e.id_estado JOIN operatoria_comercial as o ON p.id_operatoria_comercial = o.id_operatoria_comercial JOIN propietario as pro ON p.id_propietario = pro.id_propietario