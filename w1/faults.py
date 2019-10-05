import math


PRECISION = 5

VALUES = [14.85, 14.80, 14.79, 14.84, 14.81]
x0 = 14.80
ta = 2.570
n = len(VALUES)


# Среднее значение
x_ = round(sum(VALUES) / n, PRECISION)
print('Среднее значение: ', x_)

# Дисперсия
Ds2 = round(math.sqrt(
    (sum([(x_ - xi)**2 for xi in VALUES]))
    / (n*(n-1))
), PRECISION)
print('Дисперсия (среднеквадратичная ошибка): ', Ds2)

# Стандартное отклонение
DS = round(math.sqrt(Ds2**2), PRECISION)
print('Стандартное отклонение: ', DS)

# Абсолютная погрешность (Доверительный интервал)
Dx = round(ta * DS, PRECISION)
print('Абсолютная погрешность: x={0}±{1}'.format(x_, Dx))

# Относительная погрешность
dx = round(Dx / x_ * 100, 2)
print('Относительная погрешность: {}%'.format(dx))
