boys=1.09
girls=1
b=boys/(boys+girls)
g=girls/(boys+girls)
print(b,g)


def factorial(n):
    """
    Input number to calculate factorial
    """
    fact = 1
    if n == 0:
        return 1
    else:
        for i in range(1, n + 1):
            fact *= i
        return fact


def binominal_distribution(n, x, p):
    result = (factorial(n) / (factorial(x) * (factorial(n - x)))) * (p ** x) * ((1 - p) ** (n - x))
    return result


p = (1.09 / 2.09)

round(sum([binominal_distribution(6, i, p) for i in range(3, 7)]), 3)