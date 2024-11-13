import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    port=8889
)

mycursor=mydb.cursor()


#creo database
mycursor.execute("CREATE DATABASE IF NOT EXISTS pythonmysql")


#seleziono il database
mydb.database = "pythonmysql"

#creo una tabella
query="CREATE TABLE IF NOT EXISTS utenti (nome VARCHAR(50), indirizzo VARCHAR(50))"
mycursor.execute(query)

#inserisco un record nella tabella
query ="INSERT INTO utenti (nome, indirizzo) VALUES (%s, %s)"
valori=("simone", "via roma")

valori [("giovanni", "via campania")
        ("alessandro", "via torino")]

mycursor.executemany(query, valori)
mydb.commit()

#print del numero di righe inserite
print(mycursor.rowcount, "Record inseriti") #quante righe ha inserito con questa query

#visualizzo dataabse esistenti
query="SHOW DATABASES"
mycursor.execute(query) #esegue query per mostrare i database

#stampa dei risultaati
for x in mycursor:
    print(x)

print(mydb)
