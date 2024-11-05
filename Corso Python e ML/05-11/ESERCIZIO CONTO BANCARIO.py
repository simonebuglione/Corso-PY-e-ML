"""creare una classe ContoBancario che incapsula le informazioni di un conto e fornisce metodi per gestire il saldo in modo sicuro. L'obiettivo è utilizzare l'incapsulamento per prevenire accessi non autorizzati o modifiche inappropriate al saldo del conto.ConnectionAbortedError
1. Classe ContoBancario:
Attributi privati:
- __titolare (stringa che rappresenta il nome del titolare del conto)
- __saldo (decimale che rappresenta il saldo del conto)
Metodi pubblici:
-deposita(importo): aggiunge un importo al saldo solo se l'importo è positivo.
-preleva(importo): sottrae un importo dal saldo solo se ci sono fondi sufficienti e l'importo è positivo.
- visualizza_saldo(): restituisce il saldo corrente senza permettere la sua modifica diretta.
2. Gestione dei Metodi e Sicurezza:
I metodi deposita e preleva devono controllare che gli importi siano validi (e.g., non negativi).
Aggiungere metodi "getter" e "setter" per gli attributi come _titolare, applicando validazioni appropriate (e.g., il titolare deve essere una stringa non vuota)."""



class ContoBancario:
    def __init__(self, titolare: str, saldo: float = 0.0):
        #attributi privati
        self.__titolare =titolare
        self.__saldo =saldo

    #metodo per depositare un importo SOLO se positivo
    def deposita(self, importo: float) -> None:
        if importo > 0:
            self.__saldo += importo
            print(f'Deposito di {importo} effettuato. Saldo attuale: {self.__saldo}')
        else:
            print('Importo non valido. Deve essere positivo')


    #metodo per prelevare un importo solo se sufficiente e positivo
    def preleva(self, importo: float) -> None:
        if importo > 0:
            if self.__saldo >= importo:
                self.__saldo -= importo
                print(f'Prelievo di {importo} effettuato. Saldo attuale: {self.__saldo}.')
            else:
                print('fondi insufficienti per effettuare il prelievo')
        else:
            print('Importo non valido. Deve essere positivo')

    #metodo per visualizzzare il saldo
    def visualizza_saldo(self) -> float:
        return self.__saldo

    #getter per il titolare
    @property #il metodo decorato con @property consente di accedere al saldo come se fosse un attributo (conto.saldo)
    def titolare(self) -> str:
        return self.__titolare

    #setter per il titolare
    @titolare.setter #Il metodo decorato con @saldo.setter consente di impostare un nuovo valore per il saldo, applicando la logica di validazione
    def titolare(self, nuovo_titolare: str) -> None:
        if isinstance(nuovo_titolare, str) and nuovo_titolare.strip():
            self.__titolare = nuovo_titolare
            print(f'Titolare cambiato in: {self.__titolare}.')
        else:
            print('Nome del titolare non valido. Deve essere una stringa non vuota.')

#esempio di utilizzo
conto = ContoBancario("Simone Rossi", 1000.0)
conto.deposita(500.0)  #deposito valido
conto.preleva(300.0)   #prelievo valido
print(f'Saldo attuale: {conto.visualizza_saldo()}')  #visualizzazione saldo
conto.preleva(1500.0)  #prelievo non valido
conto.titolare = "Giovanni Bianchi"  #cambia il titolare
print(f'Titolare attuale: {conto.titolare}')  #visualizza il titolare
