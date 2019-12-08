import math


def count_errors(values: list, precision, ta) -> dict:
    """
    Count errors of the values series
    :param values: list of obtained values
    :param precision: number of decimals after semicolon
    :param ta: student's coefficient
    :return: dict with counted parameters
    """
    n = len(values)
    
    # Среднее значение
    x_ = round(sum(values) / n, precision)

    # Дисперсия
    ds2 = round(math.sqrt(
        (sum(((x_ - xi)**2 for xi in values)))
        / (n*(n-1))
    ), precision)
    
    # Стандартное отклонение
    ds = round(math.sqrt(ds2**2), precision)
    
    # Абсолютная погрешность (Доверительный интервал)
    dx = round(ta * ds, precision)
    
    # Относительная погрешность
    rdx = round(dx / x_ * 100, 2)
    result = {
        'n': n,
        'x_': x_,
        'ds2': ds2,
        'ds': ds,
        'dx': dx,
        'rdx': rdx
    }
    return result
