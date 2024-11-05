"""devi scrivere un programma python che simuli un sistema di login. il sistema deve permettere all'utente di inserire un nome utente e una password. poi, deve verificare se la cominazione di nome utente e password è corretta. per semplicità, puoi hardcodare una coppia di nome utente e password che sia considerata corretta. 
reuisiti:
1. input dellutente:
il programma chiede all'utente di inserire il nome utentepoi, chiede all'utente di inserire la password.
2. verifica delle credenziali:
il programma controlla se il nome utente e la password inseriti corrispondano a quelli predefiniti.
puoi decidere di avere le credenziali hardcoded nel codice per questo esercizio. ad esempio, puoi usare "admin" come nome utente e "12345" come password.
3. output del programma:
se il nome utente e la password sono corretti, stampa un messaggio di benvenuto.
altrimentim informa l'utente che le credenziali sono errate.
4. modifica dati del programma:
inserisci una condizione interna che si occui di cambiare un dato specifico tra quelli inseriti.
appena loggato fai scegliere fra due opzioni di domanda segreta e la risposta (Qual è il colore preferito, quale anlimale preferito)"""


import random

# funzione login
def login():
    #credenziali 
    username_corretto = "admin"
    password_corretto = "12345"
    

    # input per l'utente
    username = input("nome utente: ")
    password = input("password: ")
    
    #verifica  credenziali
    if username == username_corretto and password == password_corretto:
        print("Benvenuto!")
        return True
    else:
        print("Credenziali errate,riprova!")
        return False


#funzione per la registrazione
def registrazione(users):
    username = input("Nome utente: ")

    #se il nome è gia presente nel dizionario:
    if username in users:
        print("Il nome utente è già in uso. Scegline un altro")
        return False
    password = input("password: ")

    #aggiunge le credenziali alla lista degli utenti, registrazoine completata
    users[username] = password  
    print("Registrazione avvenuta con successo!")
    return True

#funzione per modificare la risposta alla domanda segreta
def modifica_risposta():
    print("Puoii modificare la tua risposta alla domanda segreta")
    print("Scegli una domanda tra le seguenti:")
    print("1. colore preferito?")
    print("2. animale preferito?")
    
    scelta = input("inserisci il numero della tua scelta: ")
    
    if scelta== "1":
        risposta =input("Inserisci il tuo colore preferito: ")
        print(f"risposta alla domanda sul colore preferito aggiornata a: {risposta}")
    elif scelta == "2":
        risposta = input("Inserisci il tuo animale preferito: ")
        print(f"risposta alla domanda sull'animale preferito aggiornata a: {risposta}")
    else:
        print("scelta non valida")


#se sia rriva fin qui si ha accesso al gioco dei numeri
def gioco_numeri():
    numero_da_indovinare = random.randint(1, 100)
    tentativi = 0
    
    print("Benvenuto al gioco dei numeri!")
    print("indovina un numero tra 1 e 100")
    
    while True:
        tentativo = int(input("Inserisci il numero: "))
        tentativi += 1
        
        if tentativo < numero_da_indovinare:
            print("Il numero da indovinare è maggiore.")
        elif tentativo > numero_da_indovinare:
            print("Il numero da indovinare è minore.")
        else:
            print(f"Complimenti! Hai indovinato il numero {numero_da_indovinare} in {tentativi} tentativi!")
            break

#funzione principale
def main():
    if login():
        modifica_risposta()  # permetto all'utente di cambiare la risposta alla domanda segreta
        gioco_numeri()  # Inizia il gioco dei numeri

#esecuzione del programma
if __name__ == "__main__":
    main()
