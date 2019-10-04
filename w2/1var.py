import math
import matplotlib.pyplot as plt


# Данные
VALUES = [
    103.4,
    115.2,
    127,
    131,
    114,
    114.1,
    119.6,
    125.5,
    116.9,
    118.1,
    123.5,
    113.5,
    112.3,
    123,
    125,
    129.9,
    99.2,
    111,
    122,
    134,
    107.1,
    117,
    117.5,
    118.5,
    124,
    127.8,
    108,
    119.5,
    123,
    126.1,
    100.1,
    120.2,
    122.2,
    124.8,
    109,
    113,
    122.5,
    135.8,
    97,
    121.1,
    123.8,
    123.2,
    105.9,
    122.6,
    123.9,
    129.5,
    107,
    123.5,
    128.5,
    117.5,
    121.5,
    127.5,
    113.2,
    120.6,
    126.5,
    116,
    122.9,
    138,
    115,
    123.1,
    140,
    94.1,
    110,
    112.9,
    132,
    102,
    109.5,
    118.3,
    135,
    112.5,
    115.5,
    120,
    126,
    130,
    105.5,
    108.2,
    119.2,
    131.4,
    106.5,
    112,
    120.8,
    121.9,
    134.2,
    115.7,
    118.9,
    124.5,
    111.5,
    121,
    133,
    116.5,
    119,
    129,
    106.1,
    119.8,
    133.6,
    114.5,
    118,
    128
]
X_max = max(VALUES)
X_min = min(VALUES)

# Количество значений
N = len(VALUES)

# Количество интервалов
K = 1 + 1.4 * math.log(N)
K = math.ceil(K)

# Длина интервала
DELTA = (X_max - X_min) / K

# Интервалы
INTERVALS = [(X_min + bias, X_min + bias + DELTA) for bias in (i*DELTA for i in range(K))]
# Распределение по интервалам
VAR_SER = {}
for val in VALUES:
    for left, right in INTERVALS:
        if left <= val <= right:
            key = f'({left}; {right})'
            if VAR_SER.get(key, None) is None:  # Not set yet
                VAR_SER[key] = 1
            else:
                VAR_SER[key] += 1


# Гистограма
xs = []
ys = []
for interval, frequency in zip(INTERVALS, VAR_SER.values()):
    xs += interval
    ys += [frequency, frequency]
plt.plot(xs, ys)

# Полигон
xs = [x + DELTA/2 for x in xs[::2]]
ys = ys[::2]
plt.plot(xs, ys)

plt.ylabel('Частоты')
plt.show()
