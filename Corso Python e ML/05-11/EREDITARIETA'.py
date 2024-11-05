class Veicolo:
    def __init__(self, marca, modello):
        self.marca = marca
        self.modello = modello

    def mostra_informazioni(self):
        print(f"Veicolo marca {self.marca}, modello {self.modello}")

class Quad(Veicolo):
    pass  # Utilizziamo "pass" in minuscolo


#creovun'istanza di Quad
mio_quad = Quad("Yamaha", "1000")

#mostrare le informazioni del quad
mio_quad.mostra_informazioni()



