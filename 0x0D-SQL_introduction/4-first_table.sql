-- creates a table called first_table in the current
-- database in your MySQL server.
-- first_table description:
-- 	id INT
-- 	name VARCHAR(256)
-- The database name will be passed as an argument of the mysql command
-- If the table first_table already exists, script should not fail
-- the SELECT or SHOW statements not allowed
CREATE TABLE IF NOT EXISTS first_table(id INT, name VARCHAR(256));
