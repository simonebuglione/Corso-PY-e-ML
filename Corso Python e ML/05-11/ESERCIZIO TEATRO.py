"""creare una classe base Posto che rappresenta un singolo posto nel teatro. Da questa, deriveranno diverse classi per tipi specifici di posti, come postoVIP e PostoStandard. Sarà inoltre necessaria una classe Teatro per gestire tutti i posti e le prenotazioni.

1.Classe Posto:
-_numero (intero: numero del posto)
-_fila (stringa: fila in cui si trova il posto)
-_occupato (booleano: stato del posto, se è occupato o meno)
Metodi:
-prenota(): prenota il posto se non è già occupato.
libera(): libera il posto se è occupato.
Getter per numero e fila, e uno stato che indica se il posto è occupato.
2. Classi Derivate: 
PostoVIP:
-Aggiunge un attributo per servizi_extra (e.g., accesso al lounge, servizio in posto).
-Sovrascrive il metodo prenota() per includere la gestione dei servizi extra.
PostoStandard:
-Potrebbe avere un costo aggiuntivo per la prenotazione online o altri servizi meno esclusivi.
3. Classe Teatro:
Attributi:
-_posti: lista di tutti i posti nel teatro.
Metodi:
-prenota_posto(numero, fila): trova e prenota un posto specifico.
-stampa_posti_occupati(): mostra tutti i posti occupati"""



class Posto:
    def __init__ (self, numero: int, fila: str):
        self._numero =numero
        self._fila = fila
        self.occupato =False

    def prenota(self):
        #prenotazione del posto se libero
         if not self._occupato:
            self._occupato = True
            print(f"Posto {self._fila}{self._numero} prenotato")
        else:
            print(f"Posto {self._fila}{self._numero} già occupato")


def libera(self):
    #funzione che libera il posto se occupato
    if self._occupato:
        self.occupato=False
        print(f"Posto{self._fila}{self._numero} liberato")
    else:
        print(f"Posto{self._fila}{self._numero} già libero")

@property
def numero(self):
    return self.numero

@property
def occupato (self):
    return self._occupato
    