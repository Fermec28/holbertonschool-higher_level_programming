-- Write a script that lists all Comedy shows in the database 
SELECT tv_shows.title  AS title FROM tv_genres INNER JOIN tv_show_genres ON tv_show_genres.genre_id = tv_genres.id INNER JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id WHERE tv_genres.name = 'Comedy' ORDER BY title;
