def simpson_integration(f, a, b, n):
    h = (b - a) / n
    x = np.linspace(a, b, n+1)
    y = f(x)

    integral_sum = y[0] + y[n]

    for i in range(1, n):
        if i % 2 == 0:
            integral_sum += 2 * y[i]
        else:
            integral_sum += 4 * y[i]

    integral = h / 3 * integral_sum

    return integral

# Exemplo de uso
import math

f = math.sin
a = 0
b = math.pi
n = 100

integral_value = simpson_integration(f, a, b, n)
print(f"Integral de sin(x) de {a} a {b}: {integral_value}")