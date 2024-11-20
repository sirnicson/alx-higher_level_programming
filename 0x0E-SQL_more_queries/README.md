# 0x0E. SQL - More Queries

his project contains various SQL tasks that involve querying, creating, and modifying MySQL databases. These queries explore database management concepts, including creating users, creating and manipulating tables, inserting records, and querying complex relationships.


## Requirements

- Allowed editors: vi, vim, emacs
- All files will be executed on Ubuntu 20.04 LTS using MySQL 8.0 (version 8.0.25)
- All files must end with a newline
- SQL queries must include a comment just before the query explaining what it does (e.g., -- query description)
- SQL keywords should be in uppercase (e.g., SELECT, WHERE, etc.)
- A README.md file must be included in the root folder of the project
- Files will be tested using wc for line length

## Task Requirements:

- Task-specific comments: Each SQL script must include a comment describing the task and the expected behavior of the query.
- SQL keywords: Ensure that all SQL keywords are written in uppercase.

## Task Descriptions

0. My Privileges!
Create a script that lists all privileges of the MySQL users user_0d_1 and user_0d_2 on the MySQL server (localhost).
File: 0-privileges.sql

1. Root User
Create a script to create the MySQL user user_0d_1 with all privileges on the MySQL server. The password for this user should be user_0d_1_pwd.
File: 1-create_user.sql

2. Read User
Create the database hbtn_0d_2 and user user_0d_2 with only SELECT privileges.
File: 2-create_read_user.sql

3. Always a Name
Create the table force_name with two fields: id INT and name VARCHAR(256) which cannot be null.
File: 3-force_name.sql

4. ID Can't Be Null
Create the table id_not_null with id INT defaulting to 1 and name VARCHAR(256).
File: 4-never_empty.sql

5. Unique ID
Create the table unique_id with id INT (default 1) that must be unique, and name VARCHAR(256).
File: 5-unique_id.sql

6. States Table
Create the database hbtn_0d_usa and the table states with the following specifications:
- id INT (unique, auto-generated, can't be null, primary key)
- name VARCHAR(256) (can't be null)
File: 6-states.sql

7. Cities Table
Create the database hbtn_0d_usa and the table cities with the following specifications:
- id INT (unique, auto-generated, can't be null, primary key)
- state_id INT (can't be null, foreign key to states.id)
- name VARCHAR(256) (can't be null)
File: 7-cities.sql

8. Cities of California
List all cities from California in the hbtn_0d_usa database, sorted by cities.id. Do not use JOIN.
File: 8-cities_of_california_subquery.sql

9. Cities by States
List all cities from hbtn_0d_usa sorted by cities.id, including the name of the state they belong to.
File: 9-cities_by_state_join.sql

10. Genre ID by Show
List all shows in hbtn_0d_tvshows that have at least one genre, sorted by tv_shows.title and tv_show_genres.genre_id.
File: 10-genre_id_by_show.sql

11. Genre ID for All Shows
List all shows in hbtn_0d_tvshows, including shows with no genre, sorted by tv_shows.title and tv_show_genres.genre_id.
File: 11-genre_id_all_shows.sql

12. No Genre
List all shows from hbtn_0d_tvshows that have no genre linked, sorted by tv_shows.title.
File: 12-no_genre.sql

13. Number of Shows by Genre
List all genres from hbtn_0d_tvshows, displaying the number of shows linked to each genre. Sort the results by the number of shows linked in descending order.
File: 13-count_shows_by_genre.sql

14. My Genres
List all genres for the show "Dexter" in hbtn_0d_tvshows, sorted by genre name.
File: 14-my_genres.sql

15. Only Comedy
List all comedy shows in hbtn_0d_tvshows, sorted by show title.
File: 15-comedy_only.sql

16. List Shows and Genres
List all shows and genres linked to those shows in hbtn_0d_tvshows. If a show has no genre, display NULL in the genre column. Sort by show title and genre name.
File: 16-shows_by_genre.sql

17. Not My Genre
Write a script to list all genres not linked to any shows.
File: 100-not_my_genre.sql


18. No Comedy Tonight!
Write a script that lists all shows without the genre Comedy in the database hbtn_0d_tvshows.
File: 101-not_a_comedy.sql

19. Rotten Tomatoes
Write a script that lists all shows from hbtn_0d_tvshows_rate by their rating sum.
File: 102-rating_shows.sql

20. Best Genre
Write a script that lists all genres in the database hbtn_0d_tvshows_rate by their rating sum.
103-rating_genres.sql
