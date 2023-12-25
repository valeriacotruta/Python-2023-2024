CREATE DATABASE states_of_the_world;
USE states_of_the_world;
drop database states_of_the_world;
SHOW TABLES;


desc states;
delete from states;
delete from neighbours;
delete from official_languages;
delete from time_zones;

SELECT * from states;
SELECT * from neighbours;
SELECT * from official_languages;
SELECT * from time_zones;

SELECT state_id FROM official_languages WHERE spoken_language LIKE "%Chinese%";
SELECT state_id FROM time_zones WHERE time_zone LIKE "%UTC+09:00%";


CREATE TABLE states (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) UNIQUE,
    capital_name VARCHAR(255),
    population INT,
    density DOUBLE,
    surface DOUBLE,
    political_regime VARCHAR(255)
);

CREATE TABLE neighbours (
    id INT PRIMARY KEY AUTO_INCREMENT,
    neighbour VARCHAR(255),
    state_id int,
    FOREIGN KEY (state_id) REFERENCES states(id)
);

CREATE TABLE official_languages (
    id INT PRIMARY KEY AUTO_INCREMENT,
    spoken_language VARCHAR(255),
    state_id int,
    FOREIGN KEY (state_id) REFERENCES states(id)
);

CREATE TABLE time_zones (
    id INT PRIMARY KEY AUTO_INCREMENT,
    time_zone VARCHAR(255),
    state_id int,
    FOREIGN KEY (state_id) REFERENCES states(id)
);