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
        self._occupato =False

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
            self._occupato=False
            print(f"Posto {self._fila}{self._numero} liberato")
        else:
            print(f"Posto {self._fila}{self._numero} già libero")

    @property
    def numero(self):
        return self._numero

    @property
    def fila(self):
        return self._fila

    @property
    def occupato(self):
        return self._occupato


class PostoVIP(Posto):
    def __init__(self, numero: int, fila: str, servizi_extra: str):
        super().__init__(numero, fila)
        self.servizi_extra =servizi_extra
    
    def prenota(self):
        #prenotazione del posto vip includendo la gestione dei servizi extra
        if not self._occupato:
            self._occupato =True
            print(f"Posto VIP {self._fila}{self._numero} prenotato con servizi extra: {self.servizi_extra}")
        else:
            print(f"Posto VIP {self._fila}{self._numero} già occupato")


class PostoStandard(Posto):
    def __init__(self, numero: int, fila: str, costo_extra: float = 0.0):
        super().__init__(numero, fila)
        self.costo_extra = costo_extra
    
    def prenota(self):
        #prenotazione del posto standard e gestione costo extra
        if not self._occupato:
            self._occupato=True
            print(f"Posto standard {self._fila}{self._numero} prenotato con costo extra: {self.costo_extra}")
        else:
            print(f"Posto standard {self._fila}{self._numero} già occupato")


class Teatro:
    def __init__(self):
        self._posti =[]

    def aggiungi_posto(self, posto: Posto):
        #aggiunge un posto alla lista dei posti del teatro
        self._posti.append(posto)

    def prenota_posto(self, numero: int, fila: str):
        #trova e prenota un posto specifico
        for posto in self._posti:
            if posto.numero == numero and posto.fila == fila:
                posto.prenota()
                return
        print(f"Posto {fila}{numero} non trovato")

    def stampa_posti_occupati(self):
        #mostra tutti i posti occupati nel teatro
        posti_occupati = [f"{posto.fila}{posto.numero}" for posto in self._posti if posto.occupato]
        if posti_occupati:
            print("Posti occupati:", ", ".join(posti_occupati))
        else:
            print("Nessun posto occupato al momento")

    def teatro_pieno(self):
        #EXTRA: controllo se il teatro è full
        return all(posto.occupato for posto in self._posti)


#Test
teatro = Teatro()

#creazione e aggiunta dei posti
teatro.aggiungi_posto(PostoStandard(1,'A', 5.0))
teatro.aggiungi_posto(PostoVIP(2, 'A', "Accesso al lounge"))
teatro.aggiungi_posto(PostoStandard(3, "B"))

#prenotazione dei posti
teatro.prenota_posto(1,"A") #prenota posto standard
teatro.prenota_posto(2,"A") #prenota posto vip
teatro.prenota_posto(3, "B") #prenota posto stadard

#stampa dei posti
teatro.stampa_posti_occupati()

#liberazione posto
teatro._posti[0].libera()  # Libera il primo posto (posto 1A)
teatro.stampa_posti_occupati()


#tentativo di prenotazione quando il teatro è full
teatro.prenota_posto(1,"A") #prenota nuovamente posto 1A
teatro.prenota_posto(2,"A") #""posto 2A
teatro.prenota_posto(3,"A") #""3A


