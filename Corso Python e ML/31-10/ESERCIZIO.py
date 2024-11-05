
# Richiesta dei dati all'utente
eta = int(input("Inserisci la tua età: ")) 
patente = input("Hai la patente? (si/no): ")
tasso_alcol = input("Qual è il tuo tasso alcolemico? (alto/normal): ")

# Determina il messaggio usando l'operatore ternario
messaggio = (
    "Non puoi guidare perché sei minorenne." if eta < 18 else
    "Non puoi guidare perché non hai la patente." if patente == "no" else
    "Non puoi guidare perché il tuo tasso alcolemico è alto." if tasso_alcol == "alto" else
    "Puoi guidare."
)

# Stampa il messaggio
print(messaggio)

