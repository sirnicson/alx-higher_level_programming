0x0D. SQL - Introduction
This project aims to introduce basic concepts and commands in SQL. It covers tasks related to databases, tables, records, and basic data manipulation using MySQL.

Requirements
General Requirements:
Allowed editors: vi, vim, emacs.
All files should be executed on Ubuntu 20.04 LTS using MySQL 8.0 (version 8.0.25).
All files must end with a new line.
SQL queries should have a comment above them.
All files should start with a comment describing the task.
SQL keywords should be in uppercase (e.g., SELECT, WHERE).
A README.md file is mandatory in the root directory.
The length of files will be tested using wc.
Tasks
0. List databases
File: 0-list_databases.sql
Lists all databases in your MySQL server.
1. Create a database
File: 1-create_database_if_missing.sql
Creates a database if it doesn't already exist.
2. Delete a database
File: 2-remove_database.sql
Deletes the hbtn_0c_0 database, if it exists, without using SELECT or SHOW.
3. List tables
File: 3-list_tables.sql
Lists all tables in a specified database.
4. First table
File: 4-first_table.sql
Creates a first_table in the current database with columns: id INT and name VARCHAR(256).
5. Full description
File: 5-full_table.sql
Prints the full description of the first_table.
6. List all in table
File: 6-list_values.sql
Lists all rows in the first_table of a specified database.
7. First add
File: 7-insert_value.sql
Inserts a row into first_table with id = 89 and name = "Best School".
8. Count 89
File: 8-count_89.sql
Displays the number of records with id = 89 in first_table.
9. Full creation
File: 9-full_creation.sql
Creates second_table with columns id INT, name VARCHAR(256), score INT, and adds specific rows.
10. List by best
File: 10-top_score.sql
Lists all records from second_table ordered by score in descending order.
11. Select the best
File: 11-best_score.sql
Lists all records with score >= 10 from second_table, ordered by score.
12. Cheating is bad
File: 12-no_cheating.sql
Updates Bob's score to 10 in second_table, without using his id.
13. Score too low
File: 13-change_class.sql
Removes all records with score <= 5 from second_table.
14. Average
File: 14-average.sql
Computes the average score from second_table.
15. Number by score
File: 15-groups.sql
Lists the number of records for each score in second_table, sorted by the number of records in descending order.
16. Say my name
File: 16-no_link.sql
Lists records from second_table where the name field is not NULL, ordered by descending score.
17. Go to UTF8
File: 100-move_to_utf8.sql
Converts the hbtn_0c_0 database, first_table, and the name field to UTF-8 encoding (utf8mb4).
18. Temperatures #0
File: 101-avg_temperatures.sql
Displays the average temperature (Fahrenheit) by city, ordered by temperature in descending order.
19. Temperatures #1
File: 102-top_city.sql
Displays the top 3 cities by temperature during July and August, ordered by temperature in descending order.
20. Temperatures #2
File: 103-max_state.sql
Displays the maximum temperature of each state, ordered by state name.
