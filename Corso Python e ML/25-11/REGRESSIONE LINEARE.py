#regressione lineare

from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X, y)
PREDICTIONS = model.predict(X)