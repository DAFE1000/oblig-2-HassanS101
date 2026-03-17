import numpy as np
import matplotlib.pyplot as plt

def g(x):
    return np.arctan(x) - 4/(1 + x**2)

def dg(x):
    return (x**2 + 8*x + 1) / (1 + x**2)**2

x = 1.7
for i in range(10):
    x_next = x - g(x)/dg(x)
    if abs(x_next - x) < 1e-12:
        break
    x = x_next

x_maks = x
y_maks = np.exp(-x_maks/4) * np.arctan(x_maks)
print(f'Toppunkt: x = {x_maks:.6f}, y = {y_maks:.6f}')
print(f'Med fire desimaler: ({x_maks:.4f}, {y_maks:.4f})')

x_vals = np.linspace(0, 5, 500)
y_vals = np.exp(-x_vals/4) * np.arctan(x_vals)

plt.plot(x_vals, y_vals, label='$f(x)=e^{-x/4}\\arctan x$')
plt.plot(x_maks, y_maks, 'ro', label='Toppunkt')
plt.xlabel('$x$')
plt.ylabel('$f(x)$')
plt.title('Funksjon med toppunkt')
plt.legend()
plt.grid(True)
plt.show()
