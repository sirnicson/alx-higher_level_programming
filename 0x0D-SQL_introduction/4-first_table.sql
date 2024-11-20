-- Script to create first_table in the specified database
-- If first_table already exists, the script will not fail

CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256)
);
