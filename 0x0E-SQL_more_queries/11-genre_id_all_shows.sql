-- import the database dump of hbtn_0d_tvshows 
-- a script that lists all shows contained in the database 
-- each record should display tv_shows.title -tv_show_genres.genre_id
-- result must be sorted in ascending order by rv_shows.title and tv_show_genres.genre_id
-- if a show doesn't have a genre ,display NULL

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_show_genres
RIGHT JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
