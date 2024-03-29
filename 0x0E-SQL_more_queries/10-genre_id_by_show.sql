-- lists all shows contained in hbtn_0d_tvshows that
-- have at least one genre linked.
--
-- Each record should display: tv_shows.title - tv_show_genres.genre_id
-- Results must be sorted in ascending order by tv_shows.title
-- and tv_show_genres.genre_id
-- You can use only one SELECT statement
-- The database name will be passed as an argument of the mysql command
SELECT ts.title, tsg.genre_id
FROM tv_show_genres tsg
JOIN tv_shows ts
ON tsg.show_id = ts.id
ORDER BY ts.title, tsg.genre_id;
