-- A test script that prepares a MySQL server for the project

-- Create hbnb_test_db if it doesn't exist.
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Create user if it doesn't exist.
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grant all privileges on hbnb_test_db to hbnb_test
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- Grant the select privileges on performance_schema to hbnb_test.
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';

-- Flush privileges to apply changes immediately
FLUSH PRIVILEGES;
