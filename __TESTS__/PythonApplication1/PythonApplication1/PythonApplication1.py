import mysql.connector

mydb = mysql.connector.connect(
    host ="localhost",
    user = "root",
    password="root",
    database="mypydb"
)
print(mydb)

mycursor = mydb.cursor()

mycursor.execute("create database if not exists mypydb")

mycursor.execute("show databases")

for x in mycursor:
    print(x)