-- List all comedy shows
SELECT ts.title
FROM tv_genres tg
JOIN tv_show_genres tsg ON tg.id = tsg.genre_id
JOIN tv_shows ts ON tsg.show_id = ts.id
WHERE tg.name = 'Comedy'
ORDER BY ts.title ASC;