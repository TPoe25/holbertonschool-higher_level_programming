-- List all tables in database
USE tables;

-- Retrieve table names for information_schema
SELECT table_name FROM information_schema.tables
Where table_schema = DATABASE();