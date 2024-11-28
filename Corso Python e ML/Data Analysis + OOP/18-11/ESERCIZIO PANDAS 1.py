"""Esercizio 1: Analisi Esplorativa dei Dati
 Obiettivo: Familiarizzare con le operazioni di base per l'esplorazione dei dati
 usando pandas.
 Dataset: Utilizzare un dataset di esempio che include le seguenti informazioni su
 un gruppo di persone: Nome, Età, Città e Salario. 

 Caricare i dati in un DataFrame autogenerandoli casualmente .
 Visualizzare le prime e le ultime cinque righe del DataFrame.
 Visualizzare il tipo di dati di ciascuna colonna.
 Calcolare statistiche descrittive di base per le colonne numeriche (media,
 mediana, deviazione standard).
 Identificare e rimuovere eventuali duplicati.
 Gestire i valori mancanti sostituendoli con la mediana della rispettiva
 colonna.
 Aggiungere una nuova colonna chiamata "Categoria Età" che classifica le
 persone come "Giovane", "Adulto" o "Senior" basandosi sull'età (es., 0-18
 anni: Giovane, 19-65 anni: Adulto, oltre 65 anni: Senior).
 Salvare il DataFrame pulito in un nuovo file CSV."""


import pandas as pd
import numpy as np


#Utilizzare un dataset di esempio che include le seguenti informazioni su
#un gruppo di persone: Nome, Età, Città e Salario. 
# Caricare i dati in un DataFrame autogenerandoli casualmente.
np.random.seed(50) #seed per generare sempre gli stessi numeri
data = {
    "Nome": [f"Persona_{i}" for i in range(1, 101)],
    "Età": np.random.randint(15, 85, size=100),
    "Città": np.random.choice(["Roma", "Milano", "Napoli", "Torino", "Firenze"], size=100),
    "Salario": np.random.randint(20000, 80000, size=100)
}

#creazione DataFrame
df =pd.DataFrame(data)


# Visualizzare le prime e le ultime cinque righe del DataFrame.
print("Prime cinque righe del DataFrame:")
print(df.head())

print("\nUltime cinque righe del DataFrame:")
print(df.tail())

# Visualizzare il tipo di dati di ciascuna colonna.
print("\nTipi di dati di ciascuna colonna:")
print(df.dtypes)

#Calcolare statistiche descrittive di base per le colonne numeriche (media,
# mediana, deviazione standard).
print("\nStatistiche descrittive di base:")
print(df.describe())

# Identificare e rimuovere eventuali duplicati.
print("\nNumero di duplicati prima della rimozione:", df.duplicated().sum())
df = df.drop_duplicates()
print("Numero di duplicati dopo la rimozione:", df.duplicated().sum())

#Gestire i valori mancanti sostituendoli con la mediana della rispettiva
 #colonna.
df["Salario"].fillna(df["Salario"].median(), inplace=True)

#che classifica le
 #persone come "Giovane", "Adulto" o "Senior" basandosi sull'età (es., 0-18
 #anni: Giovane, 19-65 anni: Adulto, oltre 65 anni: Senior).
def classify_age(age):
    if age <= 18:
        return "Giovane"
    elif age <= 65:
        return "Adulto"
    else:
        return "Senior"

df["Categoria Età"] = df["Età"].apply(classify_age)

#Salvare il DataFrame pulito in un nuovo file CSV.
output_path = r"C:\Users\bugli\Desktop\GitHub\Corso-PY-e-ML\Corso Python e ML\Dataset\cleaned_dataset.csv"
df.to_csv(output_path, index=False)
output_path
