import numpy as np
import matplotlib.pyplot as plt

def trapezoidal_interpolation(x, y, xi):
    n = len(x)
    h = x[1] - x[0]
    s = 0

    for i in range(1, n-1):
        s += y[i]

    result = y[0] + 2*s + y[n-1]
    result *= h/2

    return np.interp(xi, x, y)  # Interpolação para o ponto desejado xi

# Exemplo de uso
x = [0, 1, 2, 3, 4]
y = [0, 1, 4, 9, 16]
xi = 2.5

interp_value = trapezoidal_interpolation(x, y, xi)
print(f"Interpolação no ponto {xi}: {interp_value}")

# Plot do gráfico
plt.plot(x, y, 'o', label='Pontos')
plt.plot(xi, interp_value, 'ro', label='Interpolação')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interpolação Trapezoidal')
plt.legend()
plt.show()