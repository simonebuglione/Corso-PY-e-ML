class Ristorante:
    def __init__(self, nome, tipo_cucina):
        #inizializza il nome del ristorante, il tipo di cucina e lo stato di apertura
        self.nome = nome
        self.tipo_cucina = tipo_cucina
        self.aperto = False
        self.menu = {}

    def descrivi_ristorante(self):
        #stampa una descrizione del ristorante
        print(f"Ristorante '{self.nome}', specializzato in cucina {self.tipo_cucina}")


    def stato_apertura(self):
        #stampa se il ristorante è aperto o chiuso
        if self.aperto:
            print(f"Il ristorante '{self.nome}' è aperto")
        else:
            print(f"Il ristorante '{self.nome}' è chiuso")

    def apri_ristorante(self):
        #imposta lo stato del ristorante su aperto
        self.aperto = True
        print(f"Il ristorante '{self.nome}' è ora aperto")

    def chiudi_ristorante(self):
        #imposta lo stato del ristorante su chiuso
        self.aperto = False
        print(f"Il ristorante '{self.nome}' è ora chiuso")

    def aggiungi_al_menu(self, piatto, prezzo):
        #aggiunge un piatto al menu
        self.menu[piatto] = prezzo
        print(f"Il piatto '{piatto}' è stato aggiunto al menu al prezzo di {prezzo}€")

    def togli_dal_menu(self, piatto):
        #rimuove un piatto dal menu se esiste
        if piatto in self.menu:
            del self.menu[piatto]
            print(f"Il piatto '{piatto}' è stato rimosso dal menu")
        else:
            print(f"Il piatto '{piatto}' non è presente nel menu")

    def stampa_menu(self):
        #stampa tutti i piatti nel menu con i rispettivi prezzi
        if self.menu:
            print("Menu del ristorante:")
            for piatto, prezzo in self.menu.items():
                print(f"- {piatto}: {prezzo}€")
        else:
            print("Il menu è vuoto")

#test della classe Ristorante
#creazione di un'istanza di Ristorante
mio_ristorante = Ristorante("La Dolce Vita", "italiana")

#test dei metodi della classe
mio_ristorante.descrivi_ristorante()
mio_ristorante.stato_apertura()

#apertura del ristorante
mio_ristorante.apri_ristorante()
mio_ristorante.stato_apertura()


#aggiunta di piatti al menu
mio_ristorante.aggiungi_al_menu("Spaghetti alla Carbonara", 12.50)
mio_ristorante.aggiungi_al_menu("Pizza Margherita", 8.00)
mio_ristorante.aggiungi_al_menu("Tiramisu", 5.00)

#stampa del menu
mio_ristorante.stampa_menu()

#rimozione di un piatto dal menu
mio_ristorante.togli_dal_menu("Pizza Margherita")
mio_ristorante.stampa_menu()

#chiusura del ristorante
mio_ristorante.chiudi_ristorante()
mio_ristorante.stato_apertura()