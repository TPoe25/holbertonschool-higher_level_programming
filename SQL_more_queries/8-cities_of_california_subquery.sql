-- Use database hbtn_0d_usa
USE hbtn_0d_usa;

-- Use subquery to get state_id of California
SELECT id FROM states WHERE name = 'California' INTO @california_state_id;

-- select cities in California using state_id
SELECT * FROM cities WHERE state_id = @california_state_id ORDER BY id;