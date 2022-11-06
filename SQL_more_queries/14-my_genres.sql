-- Task 14
SELECT g.name
FROM tv_show_genres sg
INNER JOIN tv_genres g
ON g.id=sg.genre_id
INNER JOIN tv_shows s
ON s.id=sg.show_id 
WHERE s.title="Dexter"
ORDER BY g.name ASC;