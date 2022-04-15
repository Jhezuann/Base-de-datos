CREATE TABLE Usuarios(id Serial, name text, surname text, age int, email text, adress text);

INSERT INTO Usuarios(name, surname, age, email, adress) VALUES
	('Elias', 'Guanipa', 24, 'eliasguanipa@gmail.com', 'Venezuela');
INSERT INTO Usuarios(name, surname, age, email, adress) VALUES
	('Jhezuann', 'Perez', 20, 'jhezuannperez@gmail.com', 'chile');

select * from Usuarios;