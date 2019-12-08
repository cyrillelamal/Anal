"""
Классификация погрешностей измерения
"""
from l1_measurement_errors.errors import count_errors


VALUES = [14.85, 14.80, 14.79, 14.84, 14.81]
PRECISION = 2
X0 = 14.80
TA = 2.570


# All is done here
r = count_errors(VALUES, PRECISION, TA)


print(f'Среднее значение: {r["x_"]}')
print(f'Дисперсия (среднеквадратичная ошибка): {r["ds2"]}')
print(f'Стандартное отклонение: {r["ds"]}')
print(f'Абсолютная погрешность: x={r["x_"]}±{r["dx"]}')
print(f'Относительная погрешность: {r["rdx"]}%')
