""" Carica il dataset Iris.
 Standardizza le caratteristiche
 utilizzando StandardScaler.
 Suddividi i dati in training e test set
 (70% training, 30% test).
 Applica l'algoritmo
 DecisionTreeClassifier.
 Valuta la performance del modello
 utilizzando il classification_report
 (precisione, recall, F1-score).
 Visualizza la matrice di confusione."""

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt


#carica il dataset Iris
iris= datasets.load_iris()
x=iris.data
y=iris.target


#standardizza le caratteristiche
scaler=StandardScaler()
X_scaled=scaler.fit_transform(x)

#suddividi i dati in training e test set (70% training, 30% test)
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=42)

#applica l'algoritmo DecisionTreeClassifier
classificatore= DecisionTreeClassifier(random_state=42)
classificatore.fit(X_train, y_train)

#valuta la performance del modello
y_pred=classificatore.predict(X_test)
report=classification_report(y_test, y_pred)
confusion_matrix=confusion_matrix(y_test, y_pred)

#visualizza il classification_report
print(report)

#visualizza la matrice di confusione
plt.figure(figsize=(8,6))
sns.heatmap(confusion_matrix, annot=True, fmt='d', cmap='Blues', xticklabels=iris.target_names, yticklabels=iris.target_names)
plt.title('Matrice di Confusione')
plt.xlabel('Predizione')
plt.ylabel('Reale')
plt.show()



#dai risultati emerge che precision recall e f1score sono tutti pari a 1, quindi il modelloo ha classificato correttamente le istanze nel test set. il modello ha un'accuratezza pari al 100%. la matrice di confussione mostra che tutte le previsioni sono corrette, con ogni classe classificata correttamente nelle categorie.