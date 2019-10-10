import math


def count_faults(values, precision, x0, ta):
    print('x0: {}'.format(x0))
    n = len(values)
    
    # Среднее значение
    x_ = round(sum(values) / n, precision)
    print('Среднее значение: {}'.format(x_))
    
    # Дисперсия
    ds2 = round(math.sqrt(
        (sum([(x_ - xi)**2 for xi in values]))
        / (n*(n-1))
    ), precision)
    print('Дисперсия (среднеквадратичная ошибка): {}'.format(ds2))
    
    # Стандартное отклонение
    ds = round(math.sqrt(ds2**2), precision)
    print('Стандартное отклонение: {}'.format(ds))
    
    # Абсолютная погрешность (Доверительный интервал)
    dx = round(ta * ds, precision)
    print('Абсолютная погрешность: x={0}±{1}'.format(x_, dx))
    
    # Относительная погрешность
    dx = round(dx / x_ * 100, 2)
    print('Относительная погрешность: {}%'.format(dx))
