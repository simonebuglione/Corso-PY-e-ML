"""1. Carica il dataset Wine
 Esercizio Base con dataset Wine
 Carica il dataset Wine dal modulo datasets di scikit-learn.
 2. Standardizza le caratteristiche
 Standardizza le caratteristiche utilizzando StandardScaler per portare tutte
 le feature su una scala comune.
 3. Suddividi i dati in training e test set
 Suddividi i dati in due set: il 70% per il training e il 30% per il test.
 4. Applica un algoritmo di classificazione
 Applica l'algoritmo DecisionTreeClassifier per la classificazione.
 5. Valuta la performance del modello
 Valuta la performance del modello utilizzando il classification_report, con
 metriche come precisione, recall e F1-score.
 6. Visualizza la matrice di confusione
 Genera e visualizza la matrice di confusione per valutare la qualità della
 classificazione."""



from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

#carica il dataset Wine
wine= datasets.load_wine()
X=wine.data
y=wine.target

#standardizza le caratteristiche
scaler=StandardScaler()
X_scaled=scaler.fit_transform(X)

#suddividi i dati in training e test set
X_train, X_test, y_train, y_test=train_test_split(X_scaled, y, test_size=0.3, random_state=42)

#applica l'algoritmo DecisionTreeClassifier
clasf=DecisionTreeClassifier(random_state=42)
clasf.fit(X_train, y_train)

#valuta la performance del modello
y_pred=clasf.predict(X_test)
report=classification_report(y_test, y_pred)
conf_matrix=confusion_matrix(y_test, y_pred)

#verifica di eventuale overfitting
accuracy_train=clasf.score(X_train, y_train)
print(f"Accuratezza training: {accuracy_train:.4f}")

accuracy_test=clasf.score(X_test, y_test)
print(f"Accuratezza test: {accuracy_test:.4f}")

#visualizza report
print(report)

#visualizza matrice di confusione
plt.figure(figsize=(8,6))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', xticklabels=wine.target_names, yticklabels=wine.target_names)
plt.title('Matrice di Confusione')
plt.xlabel('Predizione')
plt.ylabel('Reale')
plt.show()

