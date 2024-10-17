-- This script creates a table named 'users' with specified attributes.
CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL  AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255)
);
