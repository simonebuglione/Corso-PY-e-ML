"""Carica il dataset Iris.
 Suddividi i dati in training e test.
 Applica l'algoritmo K-Nearest Neighbors
 con n_neighbors=5.
 Valuta la performance del modello
 usando l'accuratezza."""


from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score


#carica dataset Iris
iris = load_iris()
X=iris.data #per vedere caratteristiche
y= iris.target  #per le etichette(classi)

#Suddividi i dati in training e test.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

#Applica l'algoritmo K-Nearest Neighbors
KNN= KNeighborsClassifier(n_neighbors=5)
KNN.fit(X_train, y_train)

#previsioni sul set di test
y_pred = KNN.predict(X_test)

#calcolo accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuratezza moedello: {accuracy}")


#EXTRA: controllo eventuale overfitting
train_accuracy = KNN.score(X_test, y_test)
test_accuracy=accuracy_score(y_test, y_pred)

print(f"Accuratezza sui dati di addestramento: {train_accuracy}")
print(f"Accuratezza sui dati di test: {test_accuracy}")

#non c'è overfitting quindi il risultato così elevato è molto probabilmente dovuto alla semplicità del dataset