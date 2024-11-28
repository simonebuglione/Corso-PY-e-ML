"""1. Create un programma di gestione scolastica che utilizza un file txt come database, potrete aggiungere o eliminare un alunno e i suoi voti.
2. l'utente deve poter:
- aggiungere, rimuovere o aggiornare voti
- aggiungere, rimuovere o aggiornare voti
- aggiungere la possibilità di stampare nome alunno e sua media

la seconda è alunni"""


# Nome del file di database
database_file = "database_scolastico.txt"



class GestioneScolastica:
    def __init__(self, database_file):
        self.database_file = database_file

    def aggiungi_studente(self, studente):
        with open(self.database_file, "a") as file:
            file.write(studente.to_string() + "\n")
        print(f"Studente {studente.nome} aggiunto con voti {studente.voti}")

    def elimina_studente(self, nome):
        with open(self.database_file, "r") as file:
            lines = file.readlines()
        
        
        with open(self.database_file, "w") as file:
            trovato = False
            for line in lines:
                if not line.startswith(nome + ":"):
                    file.write(line)
                else:
                    trovato = True
                    

        if trovato:
            print(f"Studente {nome} eliminato.")
        else:
            print(f"Studente {nome} non trovato nel database.")

    def read_text_db(filepath):
        # file = open(filepath, "r", encoding = "utf-8")
        # stringa = file.read()
        # file.close()
        with open(self.database_file, "r") as file:
            stringa = file.read()
        righe = stringa.splitlines()

        dizionario = {}
        for indice in range(0, int(len(righe) - 1 / 2), 2):
            newdict = {righe[indice].replace("/n", "") : righe[indice + 1].replace("/n", "")}
            dizionario.update(newdict)
        return dizionario


        diz = read_text_db("text_db.txt")
        print(diz)


    def write_text_db(dizionario):
        file = open("text_db2.txt", "w", encoding = "utf-8")
        for key in dizionario.keys():
        stringa1 = key + "/n"
        stringa2 = dizionario.get(key) + "/n"
        file.write(stringa1)
        file.write(stringa2)
    file.close()
        


write_text_db(diz)

# Menu principale
#funzione principale
def main():
    alunni = GestioneScolastica(database_file)
    
    while True:
        print("1. Aggiungi alunno")
        print("2. Elimina alunno")
        print("3. Visualizza alunni")
        print("4. Media voti di un alunno")
        print("5. Esci")

        scelta = input("Scegli un'opzione(1/2/3/4/5): ")
        
        if scelta == "1":
            nome = input("Nome alunno: ")
            voti = list(map(int, input("Voti: ").split(",")))
            studente=studente(nome, voti)
            alunni.aggiungi_studente(studente)
        
        elif scelta == "2":
            nome = input("Nome alunno da eliminare: ")  # Corretto da studente.nome
            alunni.elimina_studente(nome)
        
        elif scelta == "3":
            alunni.visualizza_studenti()
        
        elif scelta == "4":
            nome = input("Inserisci il nome dell'alunno per calcolare la media: ")
            dizionario = alunni.read_text_db()
            if nome in dizionario:
                voti = list(map(int, dizionario[nome].split(",")))
                media = sum(voti) / len(voti) if voti else 0
                print(f"Media dei voti di {nome}: {media}")
            else:
                print(f"Studente {nome} non trovato nel database.")
        
        elif scelta == "5":
            print("Arrivederci!")
            break
        
        else:
            print("Scelta non valida")
            
#esegue il programma
if __name__ == "__main__":
    main()