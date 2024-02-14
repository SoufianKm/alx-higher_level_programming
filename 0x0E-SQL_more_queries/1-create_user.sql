-- creates the MySQL server user user_0d_1.
--
-- user_0d_1 should have all privileges on your MySQL server
-- The user_0d_1 password should be set to user_0d_1_pwd
-- If the user user_0d_1 already exists, your script should not fail
CREATE USER IF NOT EXISTS 'USER_0d_1'@'LOCALHOST' IDENTIFIED BY 'user_01_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'USER_0d_1'@'LOCALHOST' WITH GRANT OPTION;
