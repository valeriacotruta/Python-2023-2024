CREATE TABLE states (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255),
    capital_name VARCHAR(255),
    population INT,
    density DOUBLE,
    surface DOUBLE,
    neighbours VARCHAR(255),
    spoken_language VARCHAR(255),
    time_zone VARCHAR(255),
    political_regime VARCHAR(255)
);