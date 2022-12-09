-- CREATE DATABASE =
CREATE DATABASE HolaMundo;
-- CREATE TABLES =
USE HolaMundo;
CREATE TABLE animales (
    id int not null AUTO_INCREMENT,
    type varchar(255) not null,
    state varchar(100) not null,
    PRIMARY KEY (id)
);
CREATE TABLE User (
    Id int not null AUTO_INCREMENT,
    Name varchar(50) not null,
    Age int not null,
    Email varchar(100) not null,
    PRIMARY KEY (Id)
);
CREATE TABLE products (
    id int not null AUTO_INCREMENT,
    name varchar(50) not null,
    created_by int not null,
    marca varchar(50) not null,
    PRIMARY KEY(id),
    FOREIGN KEY(created_by) REFERENCES User(Id)
);
RENAME TABLE products TO product;
-- VIEW STRUCTURE = 
SHOW TABLES;
SHOW DATABASES;