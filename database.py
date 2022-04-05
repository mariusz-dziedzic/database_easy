# pip install mysql-connector-python
import mysql.connector

###############################
# Create database and user:
mydb = mysql.connector.connect(
  host="localhost",
  user="root"
  )

mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS test_python")
mycursor.execute("CREATE USER IF NOT EXISTS python@localhost")
mycursor.execute("GRANT ALL PRIVILEGES ON test_python.* TO python@localhost ")
mydb.close()
###############################


###############################
# Establishing a connection:
mydb = mysql.connector.connect(
  host="localhost",
  user="python",
  database="test_python")
###############################


def menu():
    print("*****MENU*****")
    print("1 - Create a new table")
    print("2 - Add a new column to the table")
    print("3 - Add a record to the table")
    print("4 - Deleting a column from a table")
    print("5 - Deleting a table")
    print("6 - Show column names from table")
    print("7 - Show table contents")
    print("0 - Exit")


def create_table(table_name):
    try:
        mycursor.execute("CREATE TABLE IF NOT EXISTS " + table_name + " (id INT PRIMARY KEY AUTO_INCREMENT)")
        print("Created table", table_name)
        print("Remember that the created table contains the 'id' column (the table cannot be empty) ")
        print("If you want to remove it, add a new column to the database and then remove the 'id' column ")
    except:
        print("Something is wrong")


def add_column(table_name, column_name):
    try:
        mycursor.execute("ALTER TABLE " + table_name + " ADD " + column_name)
        print("Added column " + column_name + " to table " + table_name)
    except:
        print("Something is wrong")


def insert_into(table_name):
    try:
        show_name_column(table_name)
        place = ', '.join(['%s'] * count_column)
        sql = "INSERT INTO " + table_name + "(" + insert_list + ")" + " VALUES (" + place + ")"
        val = []
        for i in column_list:
            value = input("Enter a value for " + i + ": ")
            val.append(value)
        print(val)
        mycursor.execute(sql, val)
        mydb.commit()
    except:
        print("Something is wrong")


def drop_column(table_name, column_name):
    try:
        mycursor.execute("ALTER TABLE " + table_name + " DROP COLUMN " + column_name)
        print("Deleted column " + column_name + " from table " + table_name)
    except:
        print("Something is wrong")


def drop_table(table_name):
    try:
        mycursor.execute("DROP TABLE  " + table_name)
        print("Deleted table", table_name)
    except:
        print("Something is wrong")


def show_name_column(table_name):
    try:
        global insert_list
        global count_column
        global column_list
        mycursor.execute("SHOW FIELDS FROM " + table_name)
        fields = mycursor.fetchall()
        count_column = len(fields)
        print("The table has ", count_column, "column/s: ")
        column_list = []
        for i, f in enumerate(fields):
            print(i+1, "-", f[0])
            column_list.append(f[0])
        sep = ", "
        insert_list = (sep.join(column_list))
    except:
        print("Something is wrong")





menu()
mycursor = mydb.cursor()

# Selecting a menu item:
x = "start"
while x != "0":
    x = input("\nNumber: ")
    if x == "1":
        y = input("Enter a table name: ")
        create_table(y)
    if x == "2":
        y = input("Enter a table name: ")
        z = input("Enter the name of the column with the type: ")
        add_column(y, z)
    if x == "3":
        y = input("Enter a table name: ")
        insert_into(y)
    if x == "4":
        y = input("Enter a table name: ")
        z = input("Enter the name of the column to be deleted: ")
        drop_column(y, z)
    if x == "5":
        y = input("Enter the name of the table to be deleted: ")
        drop_table(y)
    if x == "6":
        y = input("Enter a table name: ")
        show_name_column(y)
    if x == "7":
        y = input("Enter a table name: ")
        try:
            mycursor.execute("SELECT * FROM " +y)
            myresult = mycursor.fetchall()
            for x in myresult:
                print(x)
        except:
            print("Something is wrong")

mydb.close()
input()
