"""Esercizio:
 Utilizzando il dataset "Wine" disponibile in scikit-learn, sviluppa un modello di
 classificazione per prevedere la classe del vino basandoti sulle sue caratteristiche chimiche.
 Esegui una ricerca degli iperparametri utilizzando GridSearchCV e valuta le prestazioni del
 modello utilizzando la validazione incrociata.
 Istruzioni:
 Carica il dataset "Wine" utilizzando sklearn.datasets.load_wine().
 Esplora i dati per comprendere le caratteristiche e le classi presenti.
 Suddividi il dataset in set di training e test.
 Crea un modello di classificazione utilizzando RandomForestClassifier.
 Definisci una griglia di iperparametri, ad esempio variando il numero di stimatori
 (n_estimators), la profondità massima (max_depth) e il criterio di qualità dello split
 (criterion).
 Utilizza GridSearchCV per trovare la migliore combinazione di iperparametri, utilizzando una
 validazione incrociata con 5 fold.
 Dopo aver trovato i migliori iperparametri, addestra il modello ottimizzato sull'intero set
 di training.
 Valuta le prestazioni del modello sul test set utilizzando metriche come l'accuratezza, la
 precisione, il richiamo e l'F1-score.
 Visualizza la matrice di confusione per analizzare in dettaglio le prestazioni del modello.
 Discuta i risultati e l'importanza delle diverse caratteristiche nel modello finale."""

# Importiamo le librerie necessarie
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, ConfusionMatrixDisplay, accuracy_score
from sklearn.model_selection import cross_val_score

# Carichiamo il dataset Wine
data = load_wine()
X = data.data
y = data.target

# Esploriamo il dataset
print(f"Caratteristiche del dataset: {data.feature_names}")
print(f"Classi del vino: {data.target_names}")
print(f"Dimensioni di X: {X.shape}, Dimensioni di y: {y.shape}")

# Suddividiamo il dataset in set di training e test (80% training, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Creiamo un classificatore RandomForest
rf = RandomForestClassifier(random_state=42)

# Definiamo la griglia di iperparametri
param_grid = {
    'n_estimators': [50, 100, 150],
    'max_depth': [10, 20, None],
    'criterion': ['gini', 'entropy']
}

# Impostiamo GridSearchCV con validazione incrociata a 5 fold
grid_search = GridSearchCV(estimator=rf, param_grid=param_grid, cv=5, scoring='accuracy', n_jobs=-1)

# Eseguiamo la ricerca degli iperparametri
grid_search.fit(X_train, y_train)

# Visualizziamo i migliori iperparametri trovati
print(f"Migliori iperparametri: {grid_search.best_params_}")

# Otteniamo il miglior modello
best_rf = grid_search.best_estimator_

# Calcoliamo le prestazioni sui dati di allenamento
train_accuracy = best_rf.score(X_train, y_train)
print(f"Accuratezza sui dati di allenamento: {train_accuracy:.4f}")

# Calcoliamo le prestazioni sui dati di test
test_accuracy = best_rf.score(X_test, y_test)
print(f"Accuratezza sui dati di test: {test_accuracy:.4f}")

# Confrontiamo la validazione incrociata con le prestazioni sui dati di allenamento e test
cross_val_scores = cross_val_score(best_rf, X, y, cv=5, scoring='accuracy')
mean_cross_val_score = np.mean(cross_val_scores)
print(f"Accuratezza media dalla validazione incrociata: {mean_cross_val_score:.4f}")

# Verifica se c'è overfitting
if train_accuracy > test_accuracy:
    print("Il modello potrebbe soffrire di overfitting: alta accuratezza sui dati di allenamento e bassa sui dati di test.")
else:
    print("Il modello non mostra segni evidenti di overfitting.")

# Generiamo il report di classificazione
print("Report di classificazione:")
print(classification_report(y_test, best_rf.predict(X_test), target_names=data.target_names))

# Visualizziamo la matrice di confusione
cm = confusion_matrix(y_test, best_rf.predict(X_test))
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=data.target_names)
disp.plot(cmap='Blues')
plt.show()

# Analisi dell'importanza delle caratteristiche
importances = best_rf.feature_importances_
indices = np.argsort(importances)[::-1]

# Visualizziamo l'importanza delle caratteristiche
plt.figure(figsize=(10, 6))
plt.title("Importanza delle caratteristiche")
plt.barh(range(X.shape[1]), importances[indices], align="center")
plt.yticks(range(X.shape[1]), np.array(data.feature_names)[indices])
plt.xlabel("Importanza")
plt.show()

