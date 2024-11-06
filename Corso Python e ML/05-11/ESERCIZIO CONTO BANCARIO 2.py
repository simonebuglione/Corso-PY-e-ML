"""creare una classe base MetodoPagamento e diverse classi derivate che rappresentano diversi metodi di pagamento. Questo scenario permetterà di vedere il polimorfismo in azione, permettendo alle diverse sottoclassi di implementare i loro specifici comportamenti di pagamento, pur aderendo all'interfaccia comune definita dalla classe base.
1. Classe MetodoPagamento:
Metodi:
-effettua_pagamento(importo): un metodo che ogni sottoclasse dovrà implementare.
2. Classi Derivate:
CartaDiCredito:
-Metodi come effettua_pagamento(importo) che simula un pagamento tramite carta di credito.
PayPal:
-Metodi come effettua_pagamento(importo) che simula un pagamento tramite PayPal.
Bonifico Bancario:
Metodi come effettua_pagamento(importo) che simula un pagamento tramite bonifico bancario.
3. GestorePagamenti:
- una classe che usa un'istanza di MetodoPagamento per effettuare pagamenti, senzza preoccuparsi del dettaglio del metodo di pagamento."""


class MetodoPagamento:
    def effettua_pagamento(self, importo: float):
        raise NotImplementedError #eccezione per quando un metodo non è stato ancora implementato
    

class CartaDiCredito(MetodoPagamento):
    def effettua_pagamento(self, importo: float):
        print(f"Pagamento di {importo} euro effettuato con carta di credito")

class PayPal(MetodoPagamento):
    def effettua_pagamento(self, importo: float):
        print(f"Pagamento di {importo} euro effettuato con PayPal")

class BonificoBancario(MetodoPagamento):
    def effettua_pagamento(self, importo: float):
        print(f"Pagamento di {importo} euro effettuato tramite bonifico bancario")


class GestorePagamenti: #qui c'è polimorfismo, con gestore pagamenti è possibile usare tutti i metodi di pagamento 
    def __init__(self, metodo_pagamento: MetodoPagamento):
        self.metodo_pagamento = metodo_pagamento

def esegui_pagamento(self, importo: float):
    self.metodo_pagamento.effettua_pagamento(importo)


#test
carta= CartaDiCredito()
PayPal= PayPal()
bonifico = BonificoBancario()

#creazione del gestore di pagamento e pagamenti tramite i vari metodi
gestore_carta =GestorePagamenti(carta)
gestore_carta.esegui_pagamento(100.0)

gestore_paypal =GestorePagamenti(PayPal)
gestore_paypal.esegui_pagamento(200.0)

gestore_bonifico = GestorePagamenti(bonifico)
gestore_bonifico.esegui_pagamento(300.0)

