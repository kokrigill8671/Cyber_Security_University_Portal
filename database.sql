<<<<<<< HEAD
CREATE DATABASE cyber_portal;

USE cyber_portal;

CREATE TABLE students (

id INT AUTO_INCREMENT PRIMARY KEY,

name VARCHAR(100) NOT NULL,

email VARCHAR(100) UNIQUE NOT NULL,

password VARCHAR(255) NOT NULL,

course VARCHAR(100),

semester INT,

phone VARCHAR(20),

address TEXT,

photo VARCHAR(255)

);

CREATE TABLE admins (

id INT AUTO_INCREMENT PRIMARY KEY,

username VARCHAR(100),

password VARCHAR(255)

);

INSERT INTO admins(username,password)

VALUES

=======
CREATE DATABASE cyber_portal;

USE cyber_portal;

CREATE TABLE students (

id INT AUTO_INCREMENT PRIMARY KEY,

name VARCHAR(100) NOT NULL,

email VARCHAR(100) UNIQUE NOT NULL,

password VARCHAR(255) NOT NULL,

course VARCHAR(100),

semester INT,

phone VARCHAR(20),

address TEXT,

photo VARCHAR(255)

);

CREATE TABLE admins (

id INT AUTO_INCREMENT PRIMARY KEY,

username VARCHAR(100),

password VARCHAR(255)

);

INSERT INTO admins(username,password)

VALUES

>>>>>>> 856e12cee79502ecf54a6c0b66c9d2720f3d7548
('admin','admin123');