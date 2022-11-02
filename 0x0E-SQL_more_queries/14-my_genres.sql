-- uses the hbtn_0d_tvshows database to list all genre of the show Dexter
SELECT a.name FROM tv_genre  a JOIN tv_show_genre b ON a.id = b.genre_id JOIN tv_shows c ON c.id = b.show_id WHERE c.title = 'Dexter' ORDER BY a.namw ASC;
