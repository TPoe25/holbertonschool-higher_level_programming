-- Make a second table if not exisit
USE tables;

-- Create the second_table
CREATE TABLE IF NOT EXISTS second_table (
    id INT,
    name VARCHAR(256)
    score INT
);

-- Insert multiple rows into second table
INSERT INTO second_table (id, name, score)
VALUES
    (1, 'John', 10)
    (2, 'Alex', 3)
    (3, 'Bob', 14)
    (4, 'George', 8);