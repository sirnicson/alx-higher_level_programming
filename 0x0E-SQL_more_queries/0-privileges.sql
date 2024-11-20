-- Lists all privileges of the MySQL users `user_0d_1` and `user_0d_2` on my server (in localhost).
SELECT * FROM information_schema.user_privileges
WHERE GRANTEE IN ("'user_0d_1'@'localhost'", "'user_0d_2'@'localhost'");

