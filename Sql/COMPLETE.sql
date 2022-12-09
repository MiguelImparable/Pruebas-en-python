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
USE HolaMundo;
-- INSERT FORMS =
insert into animales (type, state) VALUES ("Chanchito", "Feliz");
insert into animales (type, state) VALUES ("Dragon", "Feliz");
insert into animales (type, state) VALUES ("Felipe", "Triste");
insert into User (Name, Age, Email) VALUES ('Oscar', '25', 'oscar@gmail.com');
insert into User (Name, Age, Email) VALUES ('Layla', '15', 'Layla@gmail.com');
insert into User (Name, Age, Email) VALUES ('Nicolas', '36', 'Nico@gmail.com');
insert into User (Name, Age, Email) VALUES ('Chanchito', '7', 'chanchito@gmail.com');
insert into product (name, created_by, marca)
values
    ('ipad', 1, 'apple'),
    ('iphone', 1, 'apple'),
    ('watch', 2, 'apple'),
    ('macbook', 1, 'apple'),
    ('imac', 3, 'apple'),
    ('ipad mini', 2, 'apple');
-- MODIFICACIONES TABLA ANIMALES = 
UPDATE animales SET state = "Feliz" WHERE id = 3;       -- Requiere un id en su condicion
DELETE FROM animales WHERE id = 2;                      -- Requiere un id en su condicion
-- TABLES VIEW ANIMALES & USER =
SELECT * FROM animales;
SELECT * FROM User;
SELECT * FROM product;
SELECT * FROM User LIMIT 1;
SELECT * FROM User WHERE Age >= 15 OR Email = 'Layla@gmail.com';
SELECT * FROM User WHERE Age BETWEEN 15 AND 30;
SELECT * FROM User WHERE Email LIKE '%gmail.com';
SELECT * FROM User ORDER BY Age ASC;                    -- Organizar en order ascendente
SELECT * FROM User ORDER BY Age DESC;                   -- Organizar en orden descendente
SELECT max(Age) AS mayor FROM User;                     -- Extraer el mayor valor
SELECT min(Age) AS menor FROM User;                     -- Extraer el menor valor
SELECT Id AS Identificacion, Name AS Nombre FROM User;  -- Cambiar de nombre las tablas
-- LEFT JOIN = 
SELECT U.Id, U.Email, P.name FROM User U LEFT JOIN product P ON U.Id = P.created_by;
SELECT U.Id, U.Email, P.name FROM User U RIGHT JOIN product P ON U.Id = P.created_by;
SELECT U.Id, U.Email, P.name FROM User U INNER JOIN product P ON U.Id = P.created_by;
select U.Id, U.name, P.id, P.name FROM User U CROSS JOIN product P;
select count(Id), marca from product group by marca;
select count(p.id), u.name from product p left join User u on u.id = p.created_by 
group by p.created_by having count(p.id) >= 2;
-- CREAR TABLES = 
USE HolaMundo;
TRUNCATE TABLE animales;
TRUNCATE TABLE User;
TRUNCATE TABLE product;
-- VIEW TABLES =
SELECT * FROM animales;
SELECT * FROM User;
SELECT * FROM product;
-- DELETE DATABASE =
DROP TABLE product;
DROP DATABASE HolaMundo;