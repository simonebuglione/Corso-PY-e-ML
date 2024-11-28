"""
Esercizio finale



Obiettivo: Creare un modello di Machine Learning per classificare le cifre da 0 a 9 utilizzando il
dataset MNIST Digits.

Punti dell'esercizio

Importazione dei Dati
Carica il dataset MNIST Digits utilizzando sklearn.datasets.
Visualizza alcune cifre per comprendere i dati.
Preprocessing dei Dati
Normalizza i dati dividendo i valori dei pixel per il massimo valore possibile (16).
Dividi il dataset in un training set e un test set usando train_test_split.
Scelta del Modello
Scegli un algoritmo di classificazione, come Support Vector Machine (SVM) o Random Forest.
Configura il modello con parametri di base.
Addestramento del Modello
Addestra il modello sui dati di training.
Verifica che il processo termini senza errori.
Valutazione del Modello
Utilizza il test set per valutare il modello.
Calcola l'accuratezza e stampa un report di classificazione.
Visualizzazione dei Risultati
Mostra alcune immagini del test set con le loro predizioni e i valori reali.
Identifica eventuali errori di classificazione.
Esperimenti Extra (Facoltativo)
Cambia il modello con un altro algoritmo (es. k-Nearest Neighbors o Decision Tree).
Applica la cross-validation per migliorare la stabilità delle valutazioni.
Genera una matrice di confusione per analizzare gli errori.applicare la cross validation con la pipline"""

 
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import MinMaxScaler
from sklearn.decomposition import PCA
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import classification_report, accuracy_score, ConfusionMatrixDisplay
import matplotlib.pyplot as plt
import numpy as np


#importazione dei dati
digits = load_digits()
X, y = digits.data, digits.target


#visualizza alcune cifre per comprendere i dati
fig, axes = plt.subplots(1, 10, figsize=(10, 3))
for ax, image, label in zip(axes, digits.images, y):
    ax.set_axis_off()
    ax.imshow(image, cmap=plt.cm.gray_r, interpolation='nearest')
    ax.set_title(label)
plt.show()


#normalizza i dati dividendo i valori dei pixel per il massimo valore possibile (16)
X_normalized = X / 16

#preprocessing dei dati
scaler = MinMaxScaler()
X_normalized = scaler.fit_transform(X)

# Applicazione della PCA con 95% di varianza
pca = PCA(n_components=0.95)  
X_pca = pca.fit_transform(X_normalized)

#dividi il dataset in un training set e un test set
X_train, X_test, y_train, y_test = train_test_split(X_pca, y, test_size=0.2, random_state=42)


#modello random forest
rf = RandomForestClassifier(random_state=42)

#addestramento del modello e verifica che il processo termini senza errori
rf.fit(X_train, y_train)

#predizione e valutazione del modello
y_pred = rf.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(f"Accuratezza modello:{accuracy:.2f}")
print("\nReport di classificazione:")
print(classification_report(y_test, y_pred))  

#verifica dell'overfitting: comparazione tra accurata sul training set e test set
train_accuracy = rf.score(X_train, y_train)
test_accuracy = accuracy_score(y_test, y_pred)

print(f"\nAccuratezza sul training set: {train_accuracy:.2f}")
print(f"Accuratezza sul test set: {test_accuracy:.2f}")


#visualizzazione dei risultati (senza PCA)
fig, axes = plt.subplots(1, 5, figsize=(10, 3))
for ax, image, prediction, true_label in zip(axes, X_test[:5], y_pred[:5], y_test[:5]):
    ax.set_axis_off()
    ax.imshow(digits.images[digits.target == true_label][0], cmap=plt.cm.gray_r, interpolation='nearest')
    ax.set_title(f"Pred: {prediction}\nTrue: {true_label}")
plt.show()

#matrice di confusione
disp = ConfusionMatrixDisplay.from_estimator(rf, X_test, y_test, cmap=plt.cm.Blues)
plt.show()

#esperimenti extra: cross validation con pipline
from sklearn.pipeline import Pipeline
from sklearn.neighbors import KNeighborsClassifier

#pipeline
pipeline = Pipeline([
    ('scaler', MinMaxScaler()),
    ('knn', KNeighborsClassifier())
])

#cross validation
punteggio_cv = cross_val_score(pipeline, X_pca, y, cv=5)
print(f"Accuracy media con cross-validation: {np.mean(punteggio_cv):.2f}")
