import math


def expected_value(p_i_s: list, x2=False) -> float:
    n = len(p_i_s)
    x_i_s = [x*x for x in range(n)] if x2 else range(n)
    m_x = sum((
        p_i * x_i for p_i, x_i in zip(p_i_s, x_i_s)
    ))
    return m_x


def standart_deviation(p_i_s: list) -> float:
    m_x = expected_value(p_i_s)
    m_x2 = expected_value(p_i_s, True)
    dx = m_x2 - m_x**2
    d = math.sqrt(dx)
    return d


def task1():
    p_i_s = [0.15, 0.11, 0.04, 0.05, 0.04, 0.1, 0.1, 0.04, 0.05, 0.12, 0.2]
    q_i_s = [0.01, 0.03, 0.05, 0.09, 0.11, 0.24, 0.21, 0.1, 0.1, 0.04, 0.02]

    m_x1 = expected_value(p_i_s)
    d_x1 = standart_deviation(p_i_s)
    m_x2 = expected_value(q_i_s)
    d_x2 = standart_deviation(q_i_s)
    print(f'1. Математическое ожидание: I {m_x1}, II {m_x2}.')
    print(f'2. Стандартное отклонение: {d_x1}, II {d_x2}.')


task1()
