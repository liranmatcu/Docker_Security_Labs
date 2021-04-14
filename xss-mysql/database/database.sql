CREATE TABLE IF NOT EXISTS xss_db.comments (
	comment_id INT UNSIGNED auto_increment PRIMARY KEY NOT NULL,
	username varchar(100) NOT NULL,
	comment varchar(280) NOT NULL
);

TRUNCATE TABLE xss_db.comments;

INSERT INTO xss_db.comments (comment_id,username,comment)
	VALUES (1,'Eureka','I love it!');

INSERT INTO xss_db.comments (comment_id,username,comment)
	VALUES (2,'Kate','That is so cute!!');