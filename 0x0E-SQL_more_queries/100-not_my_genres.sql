-- Write a script that lists all Comedy shows in the database
SELECT tv_genres.name
FROM tv_genres
WHERE tv_genres.id NOT IN (
      SELECT tv_genres.id
      FROM  tv_shows
      INNER JOIN tv_show_genres
      ON  tv_shows.id = tv_show_genres.show_id
      INNER JOIN tv_genres
       ON tv_genres.id = tv_show_genres.genre_id
       WHERE tv_shows.title = 'DEXTER'
)
ORDER BY name;
