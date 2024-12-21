import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
y = np.array([2, 4, 5, 4, 5])

model = LinearRegression()
model.fit(x, y)

x_pred = np.array([3.5]).reshape(-1, 1)
y_pred = model.predict(x_pred)
print(y_pred)

# plot the data and the regression
x_plot = np.linspace(0, 6, 100).reshape(-1, 1)
y_plot = model.predict(x_plot)
plt.scatter(x, y, label="data")
plt.plot(x_plot, y_plot, label="regression", color="red")
plt.scatter(x_pred, y_pred, label="prediction", color="green")
plt.legend()
plt.show()
