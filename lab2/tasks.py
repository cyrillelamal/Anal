"""
Задания к лабораторной работе 4
"""
from .series import ContinuousVS, DiscreteVS, VariationSeries


def task1():
    values = [
        4, 2, 4, 6, 5, 6, 4, 1, 3, 1, 2, 5, 2, 6, 3, 1, 2, 3, 4, 5, 4, 6, 2, 3, 4
    ]
    VariationSeries.PRECISION = 2

    v = DiscreteVS(values)
    v.draw_polygon(3, 1, 1)
    v.draw_cumulate(3, 1, 2)
    v.draw_empiric_dist_func(3, 1, 3)

    DiscreteVS.show()


def task2():
    values = [
        60, 25, 12, 10, 68, 35, 2, 17, 51, 9, 3, 130, 24, 85, 100, 152, 6, 18, 7, 42
    ]
    VariationSeries.PRECISION = 2

    v = ContinuousVS(values)

    print(v)


def task3():
    values = {
        (0, 5*10**3): 4, (5*10**3, 7*10**3): 12,
        (7*10**3, 10**4): 8, (10**4, 1.5*10**4): 6
    }
    VariationSeries.PRECISION = 2

    v = ContinuousVS(values)
    v.draw_cumulate(2, 1, 1)
    v.draw_hist(2, 1, 2)

    ContinuousVS.show()


def task4():
    values = [
        14.51, 14.42, 14.56, 14.47, 14.46, 14.35, 14.48, 14.53,
        14.21, 14.31, 14.35, 14.68, 14.56, 14.28, 14.36, 14.21,
        14.52, 14.23, 14.41, 14.46, 14.69, 14.54, 14.36, 14.15,
        14.37, 14.51, 14.25, 14.55, 14.51, 14.36, 14.62, 14.55,
        14.38, 14.33, 14.40, 14.52, 14.48, 14.51, 14.55, 14.39,
        14.54, 14.58, 14.48, 14.37, 14.38, 14.51, 14.36, 14.15,
        14.24, 14.32
    ]
    VariationSeries.PRECISION = 2

    v = ContinuousVS(values)
    v.draw_cumulate(3, 1, 1)
    v.draw_empiric_dist_func(3, 1, 2)
    v.draw_hist(3, 1, 3)

    ContinuousVS.show()
