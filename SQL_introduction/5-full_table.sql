-- Prints the full descrement of first_table
USE tables;

-- Get table info from information_schema
SELECT table_name, create_table
FROM information_schema.tables
WHERE table_name = 'first_table' AND table_schema = DATABASE();