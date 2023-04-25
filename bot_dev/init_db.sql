CREATE DATABASE self_storage IF NOT EXISTS;
USE self_storage;

DROP TABLE user IF EXISTS;
CREATE TABLE user(
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    tg_username VARCHAR(20),
    nickname VARCHAR(20),
    phone VARCHAR(11),
    adress VARCHAR(80)
);


DROP TABLE box IF EXISTS;
CREATE TABLE box(
    box_id INT PRIMARY KEY AUTO_INCREMENT,
    box_name VARCHAR(30),
    user_id INT NOT NULL,
    created_at DATE,
    finished_at DATE,
    items_size DECIMAL(4, 2),
    items_weight DECIMAL(4, 2),
    salt BINARY(32),
    encrypted_key BINARY(32),
    FOREIGN KEY (user_id) REFERENCES user (user_id) ON DELETE CASCADE
);

DROP TABLE stuff IF EXISTS;
CREATE TABLE stuff(
    stuff_id INT PRIMARY KEY AUTO_INCREMENT,
    box_id INT NOT NULL,
    user_id INT NOT NULL,
    item_name VARCHAR(30),
    FOREIGN KEY (box_id) REFERENCES box (box_id) ON DELETE CASCADE,
    FOREIGN KEY (user_id) REFERENCES user (user_id) ON DELETE CASCADE
);
