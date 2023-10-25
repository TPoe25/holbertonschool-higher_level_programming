-- Select shows with on linked genre
SELECT DISTINCT ts.title, tg.genre_id
FROM tv_shows ts
JOIN tv_show_genres tg ON ts.id = tg.show_id
ORDER BY ts.title, tg.genre_id ASC;