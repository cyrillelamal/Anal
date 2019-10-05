"""
Задание 1
"""
import math
import collections
import matplotlib.pyplot as plt
import numpy as np


PRECISION = 1

# Данные
VALUES = [
    103.4, 115.2, 127, 131, 114, 114.1, 119.6, 125.5, 116.9, 118.1, 123.5,
    113.5, 112.3, 123, 125, 129.9, 99.2, 111, 122, 134, 107.1, 117, 117.5,
    118.5, 124, 127.8, 108, 119.5, 123, 126.1, 100.1, 120.2, 122.2, 124.8,
    109, 113, 122.5, 135.8, 97, 121.1, 123.8, 123.2, 105.9, 122.6, 123.9,
    129.5, 107, 123.5, 128.5, 117.5, 121.5, 127.5, 113.2, 120.6, 126.5,
    116, 122.9, 138, 115, 123.1, 140, 94.1, 110, 112.9, 132, 102, 109.5,
    118.3, 135, 112.5, 115.5, 120, 126, 130, 105.5, 108.2, 119.2, 131.4,
    106.5, 112, 120.8, 121.9, 134.2, 115.7, 118.9, 124.5, 111.5, 121, 133,
    116.5, 119, 129, 106.1, 119.8, 133.6, 114.5, 118, 128
]
X_max = max(VALUES)
X_min = min(VALUES)

# Количество значений
N = len(VALUES)

# Количество интервалов
K = math.ceil(1 + 1.4 * math.log(N))

# Длина интервала
DELTA = (X_max - X_min) / K

# Интервалы
INTERVALS = [
    (round(X_min + bias, PRECISION), round(X_min + bias + DELTA, PRECISION))
    for bias in (i*DELTA for i in range(K))
]

# Распределение по интервалам
VAR_SER = {}  # Py 3.6+
for val in sorted(VALUES):
    # Choose the correct interval
    for interval in INTERVALS:
        left, right = interval
        if left <= val <= right:
            VAR_SER[interval] = VAR_SER.get(interval, 0) + 1

# Гистограма
his_xs = []
his_ys = []
for interval, frequency in VAR_SER.items():
    his_xs += interval
    his_ys += [frequency, frequency]
plt.plot(his_xs, his_ys)

# Полигон
pol_xs = []
pol_ys = []
bias = DELTA / 2
for interval, frequency in VAR_SER.items():
    x = interval[0] + bias
    pol_xs.append(x)
    pol_ys.append(frequency)
plt.plot(pol_xs, pol_ys)

plt.show()
# xs = []
# ys = []
# for interval, frequency in VAR_SER.items():
#     left, right = interval
#     xs += [left]*2 + [right]*2
#     ys += [frequency] * 4
#
#
# print(xs[::2], len(xs), xs)
# plt.hist(xs[::2], bins=60)
# plt.show()
# print(xs)
# print(ys)
# # Полигон
# xs = [x + DELTA/2 for x in xs[::2]]
# ys = ys[::2]
# plt.plot(xs, ys)
#
# plt.ylabel('Частоты')
# plt.show()
