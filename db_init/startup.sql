-- Create the receipts table if it does not already exist
CREATE DATABASE IF NOT EXISTS your_database_name
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

-- Switch to the database
USE your_database_name;

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id VARCHAR(255) NOT NULL,
    date DATE NOT NULL,
    total DECIMAL(10, 2) NOT NULL,
    comments VARCHAR(255), 
    eyes VARCHAR(50),  
    lifetext LONGTEXT  
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
