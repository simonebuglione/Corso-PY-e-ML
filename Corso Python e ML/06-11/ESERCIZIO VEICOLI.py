"""creare una classe base Veicolo con attributi comuni a tutti i veicoli e metodi per operazioni comuni come l'accensione e lo spegnimento. Derivando questa classe, creeranno specifiche classi per Auto, Furgone e Motocicletta, aggiungendo caratteristiche uniche per ciascun tipo di veicolo. Infine, dovranno implementare una classe GestoreParcoVeicoli per amministrare l'insieme dei veicoli.

Classe Veicolo:
Attributi privati:
_marca (stringa)
_modello (stringa)
_anno (intero)
_accensione (booleano)
Metodi:
accendi(): cambia lo stato di _accensione a vero.
spegni(): cambia lo stato di _accensione a falso.
Classi Derivate:
Auto:
Attributi aggiuntivi come _numero_porte
Metodo specifico come suona_clacson()
Furgone:
Attributi per _capacità_carico
Metodo per carica() e scarica()
Motocicletta:
Attributo per _tipo (e.g., sportiva, touring)
Metodo per esegui_wheelie() se il tipo è sportivo
Classe GestoreParcoVeicoli:
Attributi:
_veicoli: lista di tutti i veicoli.
Metodi:
aggiungi_veicolo(veicolo): aggiunge un veicolo alla lista.
rimuovi_veicolo(marca, modello): rimuove un veicolo specifico dalla lista.
lista_veicoli(): stampa un elenco di tutti i veicoli nel parco."""



from abc import ABC, abstractmethod

class Veicolo(ABC): #questa è la classe astratta perchè eredita da ABC
    def __init__(self, marca, modello, anno):
        self._marca =marca  #qui incapsulamento attributi privati
        self._modello =modello
        self._anno =anno
        self._accensione =False


#metodo per accendere il veicolo
def accendi(self):
    self._accensione =True
    print(f"{self._marca}{self._modello} è acceso")


#metodo per spegnere il veicolo
def spegni(self):
    self._accensione =False
    print(f"{self._marca}{self._modello} è spento")



#metodo astratto da implementare nelle classi derivate 
@abstractmethod
def get_into(self):
    pass

#metodo per ottenere info di base sul veicolo
def info_base(self):
    return f"Marca: {self.marca}, Modello {self._modello}, Anno: {self._anno}"

#METODO EXTRA: stmpa tutte le info del veicolo
def stampa_info(self): 
    print(self.info_base()) 
    accensione ="acceso" if self-accensione else "spento"
    print(f"Stato {accensione}")

