import math


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


def count_mean(values: list) -> float:
    n = len(values)
    m = sum(values) / n
    return m


def count_dispersion(values: list) -> float:
    n = len(values)
    m = count_mean(values)
    d = 1/n * sum((
        (x_i - m)**2 for x_i in values
    ))
    return d


def count_standard_deviation(values: list) -> float:
    n = len(values)
    if n >= 25:
        s = math.sqrt(count_dispersion(values))
    else:
        m = count_mean(values)
        s = math.sqrt(
            (1/(n-1) * sum((x_i - m)**2 for x_i in values))
        )
    return s


def count_var_coefficient(values: list) -> float:
    sd = count_standard_deviation(values)
    m = count_mean(values)
    cv = sd / m * 100
    return cv


def task1():
    """
    Имеются данные о распределении 100 рабочих цеха по выработке в отчетном году (в
    процентах к предыдущему году). Всего n=100 значений. (см. задачу No1 лаб.р No4).
    Вычислить среднее значение, дисперсию, среднее квадратичное отклонение и
    коэффициент вариации распределения рабочих.
    """
    m = count_mean(VALUES)
    d = count_dispersion(VALUES)
    sd = count_standard_deviation(VALUES)
    cv = count_var_coefficient(VALUES)
    print(f'1. Среднее значение: {m:.5f}')
    print(f'1. Дисперсия: {d:.5f}')
    print(f'1. Среднее квадратичное отклонение: {sd:.5f}')
    print(f'1. Коэффициент вариации: {cv:.5f}')


def task2():
    """
    Имеются данные о средних и дисперсиях заработной платы двух групп рабочих.
    Найти общую дисперсию, распределение рабочих по заработной плане и его коэффициент
    вариации.
    """
    n_i_s = [40, 60]
    x_i_s = [2400, 3200]  # групповые средние
    s_i_s = [1.8*10**5, 2*10**5]

    n = sum(n_i_s)

    # общая средняя
    m = 1/n * sum((
        x_i * n_i for x_i, n_i in zip(x_i_s, n_i_s)
    ))
    # средняя групповых дисперсий
    s_2 = 1/n * sum((
        s_i * n_i for s_i, n_i in zip(s_i_s, n_i_s)
    ))
    # мeжгрупповая дисперсия
    d2 = 1/n * sum((
        (x_i - m)**2 * n_i for x_i, n_i in zip(x_i_s, n_i_s)
    ))
    # общая дисперсия
    s2 = s_2 + d2
    # коэффициент вариации
    v_ = math.sqrt(s2) / m * 100

    print(f'2. Общая дисперсия: {s2:.5f}')
    print(f'2. Коэффициент варицаии: {v_:.5f}')
