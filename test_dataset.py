import numpy as np
import matplotlib.pyplot as plt

# Create a simple 2D dataset for linear regression
# Generate random data points
np.random.seed(42)
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)

# Plot the dataset
plt.scatter(X, y)
plt.xlabel('X')
plt.ylabel('y')
plt.title('2D Dataset for Linear Regression')
plt.show()

print("2D dataset created with 100 points.")