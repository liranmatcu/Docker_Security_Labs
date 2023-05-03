-- Creates database
DROP DATABASE IF EXISTS injectionAttack;
CREATE DATABASE injectionAttack;
USE injectionAttack;

-- For products TABLE
DROP TABLE IF EXISTS products;
CREATE TABLE products (
  id int NOT NULL,
  product_name varchar(30) NOT NULL,
  product_type varchar(30) NOT NULL,
  description varchar(200) NOT NULL,
  price int NOT NULL,
  PRIMARY KEY (id)
);

INSERT INTO products (id, product_name, product_type, description, price) VALUES
	(1, 'pillows', 'bedroom linen', 'soft fluffy pillows', 50),
	(5, 'book shelf', 'furniture', 'hard balsa wood furniture', 320),
	(6, 'pressure cooker', 'kitchen', '5 ltr. pressure cooker for the entire family', 120),
	(7, 'shampoo', 'healthcare', 'anti dandruff shampoo for oily hair', 11),
	(8, 'floodlight', 'lighting', 'bright light for the backyard', 200),
	(9, 'headphones', 'computers', 'high quality Bose headphones', 250),
	(10, 'hammer', 'tools', 'used for building things', 20),
	(11, 'milk', 'grocery', 'fresh milk from the cow farm', 3),
	(12, 'bicycle', 'vehicles', 'the best in the market, now ride to office!', 1000);
    
-- For users TABLE
DROP TABLE IF EXISTS users;
CREATE TABLE users (
	  id int NOT NULL,
    username varchar(100) NOT NULL,
    psswd varchar(50) NOT NULL,
    email varchar(50) NOT NULL,
    description varchar(200) NOT NULL,
    PRIMARY KEY (id)
);

INSERT INTO users (id, username, psswd, email, description) VALUES
	(1, 'admin', '21232f297a57a5a743894a0e4a801fc3', 'admin@eureka.edu', 'Alert! This is the admin!!'),
	(2, 'bob', '5f4dcc3b5aa765d61d8327deb882cf99', 'bobby123@gmail.com', 'That is some high quality H2O!'),
	(3, 'batman', '9aeaed51f2b0f6680c4ed4b07fb1a83c', 'batman@wayne-tech.com', 'I am BATMAN'),
	(4, 'luke', '9aeaed51f2b0f6680c4ed4b07fb1a83c', 'skywalker@star.org', 'I feel the good in you'),
	(5, 'alice', 'c93239cae450631e9f55d71aed99e918', 'alice12@gmail.com', 'In wonderland right now :O'),
	(6, 'voldemort', '856936b417f82c06139c74fa73b1abbe', 'voldemort@hogwarts.edu', 'How dare you! Avada kedavra!'),
	(7, 'frodo', 'f0f8820ee817181d9c6852a097d70d8d', 'frodo432@rings.org', 'Need to go to Mordor. Like right now!'),
	(8, 'sam', 'a55287e9d0b40429e5a944d10132c93e', 'sam@yahoo.com', 'Sam the good guy!'),
	(65, 'eva', 'e52848c0eb863d96bc124737116f23a4', 'eva@example.com', 'New user');
    