#Author: Aaron Mclynn
#Date:18/9/26
#Desc:DataBase Table 2

import sqlite3

db_connection = sqlite3.connect("mydatabase.db")

cursor = db_connection.cursor()

createTable = '''create table if not exists users(
Name text primary key,
Department text not null,
Salary integer
) STRICT'''

cursor.execute(createTable)
db_connection.commit()

addData = '''insert into users (Name,Department,Salary) values (?,?,?)'''
cursor.execute(addData,('John Doe','Engineering',75000))
cursor.execute(addData,('Jane Smith','HR',60000))
cursor.execute(addData,('Mike Johns','Finance',70000))
cursor.execute(addData,('Sarah Brown','Marketing',65000))
cursor.execute(addData,('Chris White','Sales',62000))

db_connection.commit()

fetchData = '''select * from users'''
cursor.execute(fetchData)

rowsInTable = cursor.fetchall()
for row in rowsInTable:
    print(row)



