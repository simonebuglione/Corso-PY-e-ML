"""Lo scopo di questo esercizio è creare un sistema di gestione per uan fabbrica 
che riproduce e vende vari tipi di prodotti. Gli studenti dovranno creare una classe base chiamata Prodotto e diverse classi derivate che rappresentano diversi tipi di prodotti. Inoltre, dovranno creare una classe Fabbrica che gestisce l'inventario e le vendite dei prodotti.
1. Classe Prodotto:
Attributi:
-nome (stringa che descrive il nome del prodotto)
-costo_produizione (costo per produrre il prodotto)
-prezzo_vendita(prezzo a cui il prodotto viene venduto al pugglico)
Metodi:
-calcola_profitto: restituisce la differenza tra il prezzo di vendita e il costo di produzione.
2. Classi Derivate:
-Creare almeno due classi derivate da Prodotto, per esempio Elettronica e Abbigliamento.
-Aggiungere attributi specifici per ciascun tipo di prodotto, come materiale per Abbigliamento e garanzia per Elettronica.
3. Classe Fabbrica:
Attributi:
Inventario: un dizionario che tiene traccia del tempo di ogni tipo di prodotto in magazzino.
Metodi:
-aggiungi_prodotto: aggiunge prodotti all'inventario.
-vendi_prodotto: diminuisce la quantità di un prodotto in inventario e stampa il profitto realizzato dalla vendita.
-resi_prodotto: aumenta la quantità di un prodotto restituito in inventario."""


class Prodotto:
    def __init__(self, nome, costo_produzione, prezzo_vendita):
        self.nome = nome
        self.costo_produzione = costo_produzione
        self.prezzo_vendita = prezzo_vendita

    def calcola_profitto(self):
        #prezzo - costo per vedere il profitto
        return self.prezzo_vendita - self.costo_produzione
        


class Elettronica(Prodotto):
    def __init__(self, nome, costo_produzione, prezzo_vendita, garanzia):
        super().__init__(nome, costo_produzione, prezzo_vendita)
        self.__garanzia = garanzia  #durata della garanzia in anni

    @property #consente di accedere al valore dell'attributo privato __garanzia da altre parti del codice
    def garanzia(self):
        return self.__garanzia

    @garanzia.setter #consente di modificare il valore dell'attributo privato __garanzia
    def garanzia(self, valore):
        if valore > 0:
            self.__garanzia = valore
        else:
            raise ValueError("La garanzia deve essere maggiore di zero")

    def __str__(self):
        return f"{self.nome} (Elettronica): Costo: {self.costo_produzione}, Prezzo: {self.prezzo_vendita}, Garanzia: {self.garanzia} anni"


class Abbigliamento(Prodotto):
    def __init__(self, nome, costo_produzione, prezzo_vendita, materiale):
        super().__init__(nome, costo_produzione, prezzo_vendita)
        self.__materiale = materiale  #materiale del prodotto

    @property
    def materiale(self):
        return self.__materiale

    @materiale.setter
    def materiale(self, valore):
        if valore:
            self.__materiale = valore
        else:
            raise ValueError("Il materiale non può essere vuoto")

    def __str__(self):
        return f"{self.nome} (Abbigliamento): Costo: {self.costo_produzione}, Prezzo: {self.prezzo_vendita}, Materiale: {self.materiale}"


class Fabbrica:
    def __init__(self):
        self.inventario = {}  #dizionario per memorizzare l'inventario

    def aggiungi_prodotto(self, prodotto, quantita):
        #aggiungere prodotti all'inventario
        if prodotto.nome in self.inventario:
            self.inventario[prodotto.nome]['quantita'] += quantita
        else:
            self.inventario[prodotto.nome] = {'prodotto': prodotto, 'quantita': quantita}
        print(f"Aggiunti {quantita} unità di {prodotto.nome} all'inventario.")

    def vendi_prodotto(self, nome_prodotto, quantita):
        #vende prodotto quindi diminuisce la quantità di prodotto in inventario e stampa il profitto
        if nome_prodotto in self.inventario:
            #verifica la disponibilità del prodotto (>=)
            if self.inventario[nome_prodotto]['quantita'] >= quantita:
                prodotto = self.inventario[nome_prodotto]['prodotto']
                #toglie il prodotto venduto dallo stock di prodotti disponibili
                self.inventario[nome_prodotto]['quantita'] -= quantita
                profitto = prodotto.calcola_profitto() * quantita
                print(f"Venduti {quantita} unità di {nome_prodotto}. Profitto: {profitto:.2f} euro")
            else:
                print(f"Non ci sono abbastanza unità di {nome_prodotto} in magazzino")
        else:
            print(f"Prodotto {nome_prodotto} non trovato nell'inventario")

    def resi_prodotto(self, nome_prodotto, quantita):
        #fa il reso di un prodotto, dunque restituendolo all'inventario
        if nome_prodotto in self.inventario:
            #uso += per aumentare la quantità dei prodotti dopo essere stati restituiti
            self.inventario[nome_prodotto]['quantita'] += quantita
            print(f"Restituiti {quantita} unità di {nome_prodotto} all'inventario")
        else:
            print(f"Prodotto {nome_prodotto} non trovato nell'inventario")


def gestisci_prodotto(self,prodotto, azione, quantita=1):
    if isinstance(prodotto, Prodotto):
        if azione == "aggiungi":
            self.aggiungi_prodotto(prodotto, quantita)
        elif azione == "vendi":
            self.vendi_prodotto(prodotto.nome, quantita)
        elif azione == "reso":
            self.resi_prodotto(prodotto.nome, quantita)
        else:
            print(f"Azione '{azione}' non rionosciuta per il prodotto {prodotto.nome}")
    else:
        print("Tipo di prodotto non valido")


#esempio di utilizzo
if __name__ == "__main__":
    fabbrica = Fabbrica()

    #creazione di prodotti
    prodotto1 = Elettronica("Smartphone", 200, 1000, 2)  #2 anni di garanzia
    prodotto2 = Abbigliamento("T-shirt", 10, 45, "Cotone")  #materiale cotone

    #aggiunta di prodotti all'inventario
    fabbrica.aggiungi_prodotto(prodotto1, 10)
    fabbrica.aggiungi_prodotto(prodotto2, 70)

    #vendita di prodotti
    fabbrica.vendi_prodotto("Smartphone", 5)
    fabbrica.vendi_prodotto("T-shirt", 45)

    #reso dei prodotti
    fabbrica.resi_prodotto("T-shirt", 8)



