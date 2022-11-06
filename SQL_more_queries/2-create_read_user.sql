-- Task 2
-- Create db and user with select privileges
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
USE hbtn_0d_2;
GRANT SELECT ON * TO 'user_0d_2'@'localhost';