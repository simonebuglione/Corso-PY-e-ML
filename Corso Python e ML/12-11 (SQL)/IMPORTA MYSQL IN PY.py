import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    port=8889
)

mycursor=mydb.cursor()
query="create database pythonmysql"
mycursor.execute

print(mydb)