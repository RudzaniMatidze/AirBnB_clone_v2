-- A script that prepares a MySQL server for the project.

-- Create hbnb_dev_db database if it doesn't exist.
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Create user if it doesn't exist.
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Grant all previleges on hbnb_dev_db to hbnb_dev.
GRANT ALL PREVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- Grant the select previleges on performance_schema to hbnb_dev
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

-- Flush privileges to apply changes immediately.
FLUSH PRIVILEGES;
