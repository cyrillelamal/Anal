import math
import plotly.graph_objects as go


def expected_value(x: list, p: list) -> float:
    m_x = sum((x_i * p_i for x_i, p_i in zip(x, p)))
    return m_x


def dispersion(x: list, p: list) -> float:
    x2 = [x_i * x_i for x_i in x]  # x^2
    m_x = expected_value(x, p)
    m_x2 = expected_value(x2, p)
    d_x = m_x2 - m_x*m_x
    return d_x


def standart_deviation(x: list, p: list) -> float:
    d_x = dispersion(x, p)
    d = math.sqrt(d_x)
    return d


def task1():
    """
    Известны законы распределения вероятности попадания в мишень для двух стрелков Х
    и Y (см. таблицу). Из таблицы видно, что вероятность попадания в 10 (центр мишени) для
    первого стрелка выше, чем для второго, но и вероятность того, что первый стрелок
    промажет так же выше.
    Определите какой из двух стрелков стреляет лучше. Для этого постойте многоугольник
    распределения вероятностей, найдите математическое ожидание и среднее квадратичное
    отклонение.
    """
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
    """
    В лотерее разыгрывается: автомобиль стоимостью 5000 ден. ед., 4 телевизора
    стоимостью 250 ден. ед., 5 видеомагнитофонов стоимостью 200 ден. ед. Всего продается
    1000 билетов.
    Вычислить математическое ожидание случайной величины X – средний выигрыш на
    билет. Определите, какова должна быть стоимость билетов, чтобы устроители лотерее не
    остались в проигрыше.
    """
    prizes = [(1, 5000), (4, 250), (5, 200)]
    n = 1000  # Всего билетов

    t = sum((n for n, _ in prizes))  # Всего призов

    p = [p_i / t for p_i, _ in prizes]  # Вероятности
    x = [x_i for _, x_i in prizes]  # Возможные значения

    m_x = expected_value(x, p)
    d = standart_deviation(x, p)

    price = (m_x + d) / n
    print(f'2.\n'
          f'Математическое ожидание: {m_x}\n'
          f'Стоимость билета: {price}')


def task3():
    """
    Случайная величина задана следующим рядом распределения:
    Найти математическое ожидание и дисперсию этой величины.
    """
    x = [2, 4, 7, 10, 12]
    p = [0.1, 0.2, 0.4, 0.2, 0.1]

    m_x = expected_value(x, p)
    d_x = dispersion(x, p)
    print(f'3.\n'
          f'Математическое ожидание: {m_x}\n'
          f'Дисперсия: {d_x}')


def task4():
    """
    Дан закон распределения дискретной случайной величины X.
    Найти математическое ожидание, дисперсию этой величины и среднее квадратичное
    отклонение.
    """
    x = [2, 4, 5, 6, 8, 9]
    p = [0.2, 0.25, 0.3, 0.1, 0.1, 0.05]

    m_x = expected_value(x, p)
    d_x = dispersion(x, p)
    d = standart_deviation(x, p)
    print(f'4.\n'
          f'Математическое ожидание: {m_x}\n'
          f'Дисперсия: {d_x}\n'
          f'СКО: {d}')
