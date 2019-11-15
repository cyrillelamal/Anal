import math


def task1():
    def f_int(x):
        if x <= 1:
            return 0
        elif x > 3:
            return 1
        else:
            return x * x / 8 - 1 / 8

    a = 1
    b = 2

    # Вероятность попадания в интервал (1; 2)
    # P(1 < x < 2)
    p = f_int(b) - f_int(a)

    # Дифференциальная функция распределения
    def f_dif(x):
        if x <= 3 or x > 3:
            return 0
        else:
            return x / 4

    # Математическое ожидание
    func = lambda x: x ** 2 / 4
    mx = func(b) - func(a)

    # Дисперсия
    func = lambda x: x ** 3 / 4
    dx = func(b) - func(a) - mx ** 2

    # Среднее квадратичное отклонение
    delta_x = math.sqrt(dx)

    print(f'1.\n'
          f'Математическое ожидание: {mx}\n'
          f'Дисперсия: {dx}\n'
          f'Среднее квадратичное отклонение {delta_x}\n'
          f'Вероятность попадания в интервал ({a}; {b}) = {p}')


def task2():
    def f(x):
        if x <= 0:
            return 0
        elif x > 2 ** (1 / 3):
            return 1
        else:
            return x ** 6 / 4

    a = 0
    b = 1
    k = 2  # Кол-во наступлений события
    n = 6  # Кол-во испытаний

    #  Вероятность для одного
    p = f(b) - f(a)
    q = 1 - p

    # Бернулли
    c_k_n = math.factorial(n) / (math.factorial(k) * math.factorial(n - k))
    p_k_n = c_k_n * p**k * q**(n - k)

    print(f'2.\n'
          f'Вероятность: {p_k_n}')


def task3():
    def f(x):
        if x < -1 or x > 1:
            return 0
        elif -1 <= x <= 0:
            return 1 + x
        else:
            return 1 - x

    def f_int(x):
        if x < -1 or x > 1:
            return 0
        elif -1 <= x <= 0:
            return x**2 / 2 + x
        else:
            return x - x**2 / 2

    a = -0.5
    b = 1

    p = f_int(b) - f_int(a)
    print(f'3.\n'
          f'Вероятность: {p}')
