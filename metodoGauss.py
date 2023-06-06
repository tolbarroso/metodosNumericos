import numpy as np

def gauss_integration(f, a, b, n):
    x, w = np.polynomial.legendre.leggauss(n)
    xi = 0.5 * (b - a) * x + 0.5 * (b + a)
    wi = 0.5 * (b - a) * w

    integral_sum = np.sum(wi * f(xi))

    return integral_sum

# Exemplo de uso
import math

f = math.sin
a = 0
b = math.pi
n = 5

integral_value = gauss_integration(f, a, b, n)
print(f"Integral de sin(x) de {a} a {b}: {integral_value}")