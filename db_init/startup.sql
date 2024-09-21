-- Create the receipts table if it does not already exist
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id VARCHAR(255) NOT NULL,
    date DATE NOT NULL,
    total DECIMAL(10, 2) NOT NULL,
    comments VARCHAR(255), 
    eyes VARCHAR(50),  
    lifetext LONGTEXT  
);
