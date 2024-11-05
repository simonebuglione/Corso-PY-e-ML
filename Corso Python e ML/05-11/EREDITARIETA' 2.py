class AutomobileSportiva(Veicolo, DotazioniSpeciali):
    def __init__ (self, marca, modello, dotazioni, cavalli):
        Veicolo.__init__(self, marca, modello)
        #alternativa a super per l'ereditarietà multipla
        DotazioniSpeciali.__init__(self, dotazioni)
        self.cavalli =cavalli

    def mostra_informazioni (self):
        super().mostra_informazioni()
        #chiamiamo il metodo della prima superclasse
        print(f"Potenza: {self.cavalli} CV")
        self.mostra_dotazioni()
        #possiamo chiamare metodi di entrambe le superclassi



"""Creiamo un'istanza della classe AutomobileSportiva e utilizziamo i suoi metodi per mostrare le informazioni sull'auto, inclusi i dettagli ereditati e quelli specifici della sottoclasse."""
    
    auto_sportiva= AutomobileSportiva ("Ferrari, "F8", ["ABS", "Controllo trazione", Airbag laterali"], 720)
    auto_sportiva.mostra_informazioni()