import math


def count_errors(values: list, precision, x0, ta) -> dict:
    """
    Count errors of the values series
    :param values: list of obtained values
    :param precision: number of decimals after semicolon
    :param x0: x zeroes
    :param ta: student's coefficient
    :return: dict with counted parameters
    """
    print(f'x0: {x0}')
    n = len(values)
    
    # Среднее значение
    x_ = round(sum(values) / n, precision)
    print(f'Среднее значение: {x_}')

    # Дисперсия
    ds2 = round(math.sqrt(
        (sum(((x_ - xi)**2 for xi in values)))
        / (n*(n-1))
    ), precision)
    print(f'Дисперсия (среднеквадратичная ошибка): {ds2}')
    
    # Стандартное отклонение
    ds = round(math.sqrt(ds2**2), precision)
    print(f'Стандартное отклонение: {ds}')
    
    # Абсолютная погрешность (Доверительный интервал)
    dx = round(ta * ds, precision)
    print(f'Абсолютная погрешность: x={x_}±{dx}')
    
    # Относительная погрешность
    rdx = round(dx / x_ * 100, 2)
    print(f'Относительная погрешность: {rdx}%')
    result = {
        'n': n,
        'x_': x_,
        'ds2': ds2,
        'ds': ds,
        'dx': dx,
        'rdx': rdx
    }
    return result
