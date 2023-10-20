import datetime
import numpy as np
import matplotlib.pyplot as plt

# Given dataset
X = np.array([2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
Y = np.array([30, 25, 95, 115, 265, 325, 570, 700, 1085, 1300])

# Normalize the dataset
X_normalized = X - np.mean(X)
Y_normalized = Y - np.mean(Y)

# Calculate 𝑏1, 𝑏0, and r
n = len(X_normalized)
sum_x = np.sum(X_normalized)
sum_y = np.sum(Y_normalized)
sum_xy = np.sum(X_normalized * Y_normalized)
sum_x_squared = np.sum(X_normalized**2)
sum_y_squared = np.sum(Y_normalized**2)

b1 = sum_xy / sum_x_squared
b0 = np.mean(Y) - b1 * np.mean(X)
r = sum_xy / np.sqrt(sum_x_squared * sum_y_squared)

# Print 𝑏1, 𝑏0, and r
print("𝑏1:", b1)
print("𝑏0:", b0)
print("Coefficient of linear correlation (r):", r)

# Plot the curve of X vs Y and the fitting line
plt.scatter(X, Y, label="Data points")
plt.plot(X, b0 + b1 * X, color='red', label="Fitting line")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.show()

# Based on the value of r, you can draw conclusions about the goodness of fit
if np.abs(r) > 0.9:
    print("The linear model is a good fit for the dataset.")
else:
    print("Other models might provide a better fit based on data visualization.")

current_datetime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print(f"Current date and time: {current_datetime}")