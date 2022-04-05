Before starting:
Before starting, make sure you have the mysql-connector library installed, without it the program will not work. To install, execute the command in the CMD terminal:
pip install mysql-connector-python

Then you need to start the SQL server (e.g. using the XAMPP application) 

Description:
- The purpose of the program is to facilitate the work of entering data into the database. It is not necessary to enter complete SQL queries to check the contents of a table or to add / remove a record. 
- The program first creates a database named 'test python' and user 'python' with all the rights in this database.
- User can select appropriate menu item to execute sql command.
Menu:
1 - Create a new table
2 - Add a new column to the table
3 - Add a record to the table
4 - Deleting a column from a table
5 - Deleting a table
6 - Show column names from table
7 - Show table contents
0 - Exit

1 - It allows you to create a table with a given name by the user. As the table cannot be empty, there is also an 'id' column that can be removed after adding another, new column. 
2 - The user first gives the name of the table to which he wants to add a column, and then gives the name of the column with the type of data it will have, (e.g. name VARCHAR(25)).
3 - User can add record to existing table. At the beginning, the table structure is shown - what columns it contains. Then the user is asked to enter the value he wants to enter for each of the columns (Column names are also displayed).
4 - The user gives the name of the table and then the name of the column from the table that he wants to delete.
5 - Deleting a table with the name given to the user .
6 - The table structure is shown - what columns it contains.
7 - Shows all records in the table 
0 - Just exit ;)