from varseries import DiscreteVS
from l5_variation_series_characteristics.lab_indicators_of_variation import count_dispersion, count_standard_deviation


def task1():
    data = [
        1, 5, 2, 4, 3, 4, 6, 4, 5, 1,
        2, 2, 3, 4, 5, 3, 4, 5, 2, 1,
        4, 5, 5, 4, 3, 4, 6, 1, 2, 4,
        4, 3, 5, 6, 4, 3, 3, 1, 3, 4,
        3, 4, 3, 1, 2, 4, 4, 5, 6, 1,
        3, 4, 5, 4, 4, 3, 2, 6, 1, 2,
        4, 5, 3, 3, 2, 3, 6, 4, 3, 4,
        5, 4, 3, 3, 2, 6, 3, 3, 5, 4,
        4, 3, 3, 2, 1, 2, 1, 6, 5, 4,
        3, 2, 3, 4, 4, 3, 5, 6, 1, 5
    ]

    vs = DiscreteVS(data)

    acc_frequencies = vs.acc_frequencies
    acc_rel_frequencies = vs.acc_rel_frequencies

    mean = round(sum(x*y for x, y in vs.vs.items()) / vs.n)
    mode = vs.mode
    median = vs.median

    dispersion = count_dispersion(vs.vals)
    sd = count_standard_deviation(vs.vals)

    print(f'1.\n'
          f'Значения (Разряды): {vs.variants}\n'
          f'Накопленные частоты: {acc_frequencies}\n'
          f'Накопленные частости: {acc_rel_frequencies}\n'
          f'Средний разряд: {mean}\n'
          f'Мода: {mode}\n'
          f'Медиана: {median}\n'
          f'Дисперсия: {dispersion}\n'
          f'Стандартное отклонение {sd}')

    vs.draw_polygon('Распределение рабочих по разрядам')


def task2():
    data = [
        2, 4, 5, 3, 4, 6, 7, 4, 5, 3, 3, 4, 2, 6, 5, 4, 7, 2, 3, 4,
        4, 5, 4, 3, 4, 6, 6, 5, 2, 3, 4, 3, 5, 6, 7, 2, 4, 3, 4, 5,
        4, 6, 7, 2, 5, 3, 5, 4, 3, 7, 2, 4, 3, 4, 5, 4, 3, 2, 6, 7,
        6, 4, 3, 2, 3, 4, 5, 4, 3, 5, 4, 3, 2, 6, 4, 5, 7, 5, 4, 3,
        4, 5, 7, 4, 3, 4, 5, 6, 5, 3, 4, 2, 2, 4, 3, 7, 5, 6, 4, 5
    ]

    vs = DiscreteVS(data)

    acc_frequencies = vs.acc_frequencies
    acc_rel_frequencies = vs.acc_rel_frequencies

    mean = round(sum(x * y for x, y in vs.vs.items()) / vs.n)
    mode = vs.mode
    median = vs.median

    dispersion = count_dispersion(vs.vals)
    sd = count_standard_deviation(vs.vals)

    print(f'2.\n'
          f'Значения (Число производственных подразделений): {vs.variants}\n'
          f'Накопленные частоты: {acc_frequencies}\n'
          f'Накопленные частости: {acc_rel_frequencies}\n'
          f'Среднее число производственных подразделений: {mean}\n'
          f'Мода: {mode}\n'
          f'Медиана: {median}\n'
          f'Дисперсия: {dispersion}\n'
          f'Стандартное отклонение {sd}')

    vs.draw_polygon('Распределение сельскохозяйственных предприятий '
                    'по числу производственных подразделений '
                    '(Полигон частот)')
