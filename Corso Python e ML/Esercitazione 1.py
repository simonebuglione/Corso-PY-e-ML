#dati
utenti = []  
lista_articoli = [  
    {"nome": "pc", "prezzo": 700, "quantità": 10},
    {"nome": "Mouse", "prezzo": 20, "quantità": 50}
]

#registrazione
def registrazione():
    username = input("nome utente: ")  
    password = input("password: ")     
    utenti.append({"username": username, "password": password})  
    print("Registrazione completata")  

#login
def login():
    username = input("nome utente: ")  
    password = input("password: ")     
    for utente in utenti:              
        if utente["username"] == username and utente["password"] == password:
            return utente              
    print("Nome utente o password errati.")  
    return None

def visualizza_articoli():
    for articolo in lista_articoli:  
        print(f"Nome: {articolo['nome']}, Prezzo: {articolo['prezzo']}, Quantità: {articolo['quantità']}")



def main():
    while True:
        print("1. Registrazione")
        print("2. Login")
        scelta = input("Scegli un'opzione: ")  

        if scelta == "1":
            registrazione()  
        elif scelta == "2":
            utente = login()  
            if utente:
                visualizza_articoli()  
        else:
            print("Scelta non valida.")  

if __name__ == "__main__":
    main()  