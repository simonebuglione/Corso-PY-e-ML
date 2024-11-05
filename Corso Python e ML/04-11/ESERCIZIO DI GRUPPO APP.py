# Classe per rappresentare ogni utente
class Utente:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.punteggio = 0  # Inizializza il punteggio a 0

# Lista globale per memorizzare gli utenti
lista_utenti = []

def registrazione():
    print("Benvenuto nella fase di registrazione!")
    
    while True:
        username = input("Inserisci un nome utente: ")
        # Controlla se l'utente è già registrato
        if any(utente.username == username for utente in lista_utenti):
            print("Nome utente già esistente. Scegli un altro nome utente.")
        else:
            break

    password = input("Inserisci una password: ")
    # Crea un nuovo oggetto utente e lo aggiunge alla lista
    nuovo_utente = Utente(username, password)
    lista_utenti.append(nuovo_utente)
    
    print(f"Registrazione completata! Benvenuto/a {username}.")

def mostra_utenti():
    print("Utenti registrati:")
    for utente in lista_utenti:
        print(f"- {utente.username}")

def login():
    print("Benvenuto nella fase di login!")
    while True:
        nomeutente_login = input("Inserisci il tuo nome utente: ")
        password_login = input("Inserisci la tua password: ")
        
        # Controlla se le credenziali sono corrette
        for utente in lista_utenti:
            if utente.username == nomeutente_login and utente.password == password_login:
                print(f"Login riuscito! Benvenuto/a {nomeutente_login}.")
                return  # Uscita dal metodo dopo il login riuscito
            
        print("Credenziali errate! Riprova!")

# Esempio di utilizzo delle funzioni
registrazione()  # Chiede di registrare un nuovo utente
mostra_utenti()  # Mostra gli utenti registrati
login()          # Permette di effettuare il login
