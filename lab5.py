import math

# Определение функции f(x)
def f(x):
    return 1/3 + math.cos(10 + 2.3**abs(x))

# Определение производной f'(x)
def f_derivative(x):
    return -math.sin(10 + 2.3**abs(x)) * 2.3**abs(x) * math.log(2.3) * (1 if x >= 0 else -1)

# Метод бисекции
def bisection_method(a, b, tol=1e-6, max_iter=100):
    if f(a) * f(b) >= 0:
        raise ValueError("Функция должна иметь разные знаки на концах интервала [a, b].")
    
    iter_count = 0
    while (b - a) / 2 > tol and iter_count < max_iter:
        c = (a + b) / 2
        if f(c) == 0:
            break
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
        iter_count += 1
    
    return (a + b) / 2

# Метод Ньютона
def newton_method(x0, tol=1e-6, max_iter=100):
    x = x0
    iter_count = 0
    while abs(f(x)) > tol and iter_count < max_iter:
        x = x - f(x) / f_derivative(x)
        iter_count += 1
    return x

# Локализация корня
a = 0
b = 1
while f(a) * f(b) >= 0:
    b += 1
print(a, b)
# Решение методом бисекции
root_bisection = bisection_method(a, b)
print(f"Корень, найденный методом бисекции: {root_bisection}")

# Решение методом Ньютона
initial_guess = (a + b) / 2  # Начальное приближение
root_newton = newton_method(initial_guess)
print(f"Корень, найденный методом Ньютона: {root_newton}")