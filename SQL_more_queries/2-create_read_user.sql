-- Create database if does not exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Create user user_0d_2 if not exists
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED by 'user_0d_2_pwd';

-- Grant SELECT privileges to hdtn_0d_2 database and user_0d_2
GRANT SELECT ON hdtn_0d_2.* TO 'user_0d_2'@'localhost';