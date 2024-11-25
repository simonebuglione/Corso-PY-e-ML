#caricamento del dataset standard di scikit-learn già pronti, come Iris o Boston Housing

#esempio caricamento del dataset standard di scikit-learn
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler

data = load_iris()
X = data.data  # caratteristiche
y = data.target  # target


scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)


#regressione lineare

from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X, y)
predictions = model.predict(X)


#k-neighbors (KNN)

from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X, y)
predictione = knn.predict(X)