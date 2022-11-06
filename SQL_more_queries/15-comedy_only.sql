-- Task 15
SELECT s.title
FROM tv_show_genres sg
INNER JOIN tv_genres g
ON g.id=sg.genre_id
INNER JOIN tv_shows s
ON s.id=sg.show_id 
WHERE g.name="Comedy"
ORDER BY s.title ASC;