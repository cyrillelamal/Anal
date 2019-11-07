import math
import plotly.graph_objects as go


def expected_value(x: list, p: list, x2=False) -> float:
    if x2:  # Square
        x = [x_i*x_i for x_i in x]
    m_x = sum((x_i * p_i for x_i, p_i in zip(x, p)))
    return m_x


def dispersion(x: list, p: list) -> float:
    m_x = expected_value(x, p)
    m_x2 = expected_value(x, p, True)
    d_x = m_x2 - m_x*m_x
    return d_x


def standart_deviation(x: list, p: list) -> float:
    d_x = dispersion(x, p)
    d = math.sqrt(d_x)
    return d


def task1():
    p = [0.15, 0.11, 0.04, 0.05, 0.04, 0.1, 0.1, 0.04, 0.05, 0.12, 0.2]
    q = [0.01, 0.03, 0.05, 0.09, 0.11, 0.24, 0.21, 0.1, 0.1, 0.04, 0.02]
    x = list(range(len(p)))  # 0..10

    m_x1 = expected_value(x, p)
    d_x1 = standart_deviation(x, p)
    m_x2 = expected_value(x, q)
    d_x2 = standart_deviation(x, q)
    print(f'1.\n'
          f'Первый стрелок: M(x)={m_x1}, d={d_x1}\n'
          f'Второй стрелок: M(x)={m_x2}, d={d_x2}')

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=p,
                             mode='lines+markers',
                             name='Первый стрелок'))
    fig.add_trace(go.Scatter(x=x, y=q,
                             mode='lines+markers',
                             name='Второй стрелок'))
    fig.show()


def task2():
    prizes = [(1, 5000), (4, 250), (5, 200)]
    n = 1000  # Всего билетов

    t = sum((n for n, _ in prizes))  # Всего призов

    x = [x_i for _, x_i in prizes]  # Возможные значения
    p = [p_i / t for p_i, _ in prizes]  # Вероятности
    m_x = expected_value(x, p)
    d = standart_deviation(x, p)

    price = (m_x + d) / n
    print(f'2.\n'
          f'Стоимость билета: {price}')
