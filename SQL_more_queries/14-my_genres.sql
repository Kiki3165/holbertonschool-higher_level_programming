-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT tv_genres.name AS name
FROM tv_shows
INNER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
INNER JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id
WHERE tv_shows.title = 'Dexter'
ORDER BY name;