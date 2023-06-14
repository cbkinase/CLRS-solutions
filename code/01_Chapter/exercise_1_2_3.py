import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import root

# Define the functions
def f1(n):
    return 100 * n**2

def f2(n):
    return 2**n

# Define the equation f(n) = f1(n) - f2(n)
def equation(n):
    return f1(n) - f2(n)

# Use scipy.optimize.root to find multiple intersection points
solution = root(equation, [0.5, 20.5])  # Provide multiple initial guesses in a list

# Print the intersection points
for i, sol in enumerate(solution.x):
    print(f"Intersection point {i+1}: (n = {sol}, y = {f1(sol)})")

n = np.linspace(0, 15)
y1 = 100 * n**2
y2 = 2**n

plt.plot(n, y1, label='100n^2')
plt.plot(n, y2, label='2^n')
plt.xlabel('n')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.title('Plot of 100n^2 vs. 2^n')
plt.show()
