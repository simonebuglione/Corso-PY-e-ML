import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    port=8889
)

mycursor=mydb.cursor()


#creo database
query="create database pythonmysql"
mycursor.execute(query)


#visualizzo dataabse esistenti
query="show databases"
mycursor.execute(query) #esegue query per mostrare i database

#stampa dei risultaati
for x in mycursor:
    print(x)

print(mydb)

#creo una query per creare una tabella
#query="create table if not exist utenti (nome varchar(50), indirizzo varchar(50))"

query ="insert into utenti (nome, indirizzo) values(%s%s)"
valori=("simone", "via roma")

mycursor=mydb.cursor()

mycursor.execute(query)