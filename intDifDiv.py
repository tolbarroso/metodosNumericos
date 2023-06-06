def divided_difference(x, y):
    n = len(x)
    coeffs = y.copy()

    for j in range(1, n):
        for i in range(n-1, j-1, -1):
            coeffs[i] = (coeffs[i] - coeffs[i-1]) / (x[i] - x[i-j])

    return coeffs

def interpolation_polynomial(x, y, xi):
    coeffs = divided_difference(x, y)
    n = len(x)
    p = coeffs[n-1]

    for i in range(n-2, -1, -1):
        p = p * (xi - x[i]) + coeffs[i]

    return p

# Exemplo de uso
x = [0, 1, 2, 3, 4]
y = [0, 1, 4, 9, 16]
xi = 2.5

interp_value = interpolation_polynomial(x, y, xi)
print(f"Interpolação no ponto {xi}: {interp_value}")