-- Task 9
-- Join tables
SELECT c.id, c.name, s.name
FROM cities as c 
JOIN states as s
ON c.state_id=s.id
ORDER BY c.id ASC;