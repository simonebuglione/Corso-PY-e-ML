"""Carica il dataset Wine
Utilizza il modulo datasets di scikit-learn per caricare il dataset Wine.

Esplora il dataset
Visualizza il numero di campioni per ciascuna classe e calcola le statistiche di base delle feature.
Visualizzazione: crea un grafico a barre per mostrare la distribuzione delle classi.

Riduci la dimensionalità ***
Applica la PCA (Principal Component Analysis) per ridurre le dimensioni delle feature a 2 componenti
principali.
Visualizzazione: crea un grafico scatter 2D per rappresentare i dati trasformati, con i punti colorati in
base alla classe.

Sudddividi i dati in training e test set
Dividi i dati in due set: l'80% per il training e il 20% per il test.

Applica un algoritmo di classificazione
Utilizza un modello RandomForestClassifier per la classificazione.

Valuta la performance del modello
Valuta le prestazioni utilizzando le metriche di accuratezza, precisione, recall e F1-score.

Visualizza l'importanza delle feature / caratteristiche
Visualizza le feature più importanti del dataset Wine secondo il modello Random Forest, utilizzando un
grafico a barre.

Visualizza la matrice di confusione
Genera e visualizza la matrice di confusione per valutare la qualità della classificazione.
Visualizzazione: utilizza una heatmap per rappresentare la matrice di confusione in modo più chiaro.

Ottimizza l'algoritmo
Utilizza la GridSearchCV per ottimizzare i parametri del Random Forest (ad esempio: numero di estimatori e
profondità massima dell'albero)."""


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_recall_fscore_support, confusion_matrix
from sklearn.decomposition import PCA


#1.carica dataset wine
wine=load_wine()
X=wine.data
y=wine.target

#converti in un dataframe per esplorare più facilmente
wine_df=pd.DataFrame(X, columns=wine.feature_names)
wine_df['target']=y


#2.esplorazione dataset
#numero di campioni per ciascuna classe
class_counts=wine_df['target'].value_counts()

#statistiche di base delle feature
statistiche=wine_df.describe()

#stampa info esplorative
print(f"Distribuzione delle classi: {class_counts}")
print(f"Statistiche di base delle feature:\n{statistiche}")

#visualizza la distribuzione delle classi
plt.figure(figsize=(8, 6))
class_counts.plot(kind='bar', color='skyblue')
plt.title('Distribuzione delle Classi nel Dataset Wine')
plt.xlabel('Classe')
plt.ylabel('Numero di Campioni')
plt.xticks(rotation=0)
plt.show()


#4.suddivisione dataset in training e test set
x_train, x_test, y_train, y_test=train_test_split(X, y, test_size=0.2, random_state=42)

#4.applica algoritmo randomforest
rf=RandomForestClassifier(random_state=42)
rf.fit(x_train, y_train)

#5.valuta la performance del modello
y_pred=rf.predict(x_test)

#calcolo delle metriche
accuracy=accuracy_score(y_test, y_pred)
precision, recall, f1_score, _=precision_recall_fscore_support(y_test, y_pred, average='weighted')


#stampa delle metriche
print(f"Accuracy: {accuracy}")
print(f"Precision: {precision}")
print(f"Recall: {recall}")
print(f"F1-score: {f1_score}")


#feature importance
fi=rf.feature_importances_
indici=np.argsort(fi)[::-1]

#visualizza feature importances
plt.figure(figsize=(10, 6))
plt.barh(range(len(fi)), fi[indici], align='center')
plt.yticks(range(len(fi)), np.array(wine.feature_names)[indici])
plt.title('Importanza delle Feature (Random Forest)')
plt.xlabel('Importanza')
plt.ylabel('Feature')
plt.show()

#6.visualizza matr di confusione
conf_matrix=confusion_matrix(y_test, y_pred)

#heatmap della matrice di confusione
plt.figure(figsize=(8, 6))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', xticklabels=wine.target_names, yticklabels=wine.target_names)
plt.title('Matrice di Confusione')
plt.xlabel('Predetto')
plt.ylabel('Reale')
plt.show()


#7.ottimizza algoritmo con gridsearchcv
param_grid={'n_estimators': [100, 200, 300], 'max_depth': [None, 5, 10]}

grid_search = GridSearchCV(estimator=rf, param_grid=param_grid, cv=5, n_jobs=-1, verbose=1)
grid_search.fit(x_train, y_train)

#stampa i parametri migliori
print(f"Parametri migliori: {grid_search.best_params_}")

#3.analisi delle componenti principali (PCA)
pca=PCA(n_components=2)
X_pca=pca.fit_transform(X)

#crea dataframe PCA
pca_df=pd.DataFrame(X_pca, columns=['PC1', 'PC2'])
pca_df['target']=y

#grafico scatter 2D
plt.figure(figsize=(8, 6))
sns.scatterplot(x='PC1', y='PC2', hue='target', palette='Set1', data=pca_df, s=100, alpha=0.7)
plt.title('PCA: Dati Trasformati in 2 Componenti Principali')
plt.xlabel('PC1')
plt.ylabel('PC2')
plt.legend(title='Classe', labels=wine.target_names)
plt.show()
