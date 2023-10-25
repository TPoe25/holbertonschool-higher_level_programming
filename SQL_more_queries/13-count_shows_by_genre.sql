-- list all genres and number of shows linked
SELECT tg.name AS genre, COUNT(tsg.show_id) AS number_of_shows
FROM tv_genres tg
LEFT JOIN tv_show_genres tsg ON tg.id = tsg.genre_id
GROUP BY tg.id, tg.name
HAVING number_of_shows > 0
ORDER BY number_of_shows DESC;