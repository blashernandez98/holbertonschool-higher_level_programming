-- Task 16
SELECT s.title, g.name
FROM tv_shows s
JOIN tv_show_genres sg
ON s.id=sg.show_id
JOIN tv_genres g
ON sg.genre_id=g.id
ORDER BY s.title, g.name;