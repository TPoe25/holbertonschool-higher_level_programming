-- List all tables in database

-- connects to mysql server
USE mysql;

-- Retrieve table names for information_schema
SELECT table_name
FROM information_schema.tables
WHERE table_schema = DATABASE();