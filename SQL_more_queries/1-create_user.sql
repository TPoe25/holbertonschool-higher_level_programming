-- Create user 0d1 if not exists
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Grant all privileges to user 0d1
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';