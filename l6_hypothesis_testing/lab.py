import math
import plotly.graph_objects as go


from variation_series import DiscreteVS
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

    x = list(vs.vs.keys())
    y = list(vs.vs.values())
    acc_frequencies = vs.acc_frequencies
    acc_rel_frequencies = vs.acc_rel_frequencies

    mean = round(sum(x*y for x, y in vs.vs.items()) / vs.n)
    mode = vs.count_mode()
    median = vs.count_median()

    dispersion = count_dispersion(vs.values)
    sd = count_standard_deviation(vs.values)

    print(f'1.\n'
          f'Значения (Разряды): {x}\n'
          f'Накопленные частоты: {acc_frequencies}\n'
          f'Накопленные частости: {acc_rel_frequencies}\n'
          f'Средний разряд: {mean}\n'
          f'Мода: {mode}\n'
          f'Медиана: {median}\n'
          f'Дисперсия: {dispersion}\n'
          f'Стандартное отклонение {sd}')

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=x, y=y,
        mode='lines',
        name='Распределение рабочих по разрядам',
    ))
    fig.update_layout(
        title='Распределение рабочих по разрядам (Полигон частот)',
        xaxis_title='Разряды',
        yaxis_title='Частоты'
    )
    fig.show()


def task2():
    pass
