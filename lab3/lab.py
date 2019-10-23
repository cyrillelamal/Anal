import math
from functools import reduce

from lab2.series import ContinuousVS


PRECISION = 2


VALUES1 = [
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


def task1():
    v = ContinuousVS(VALUES1)

    def prod_gen():
        for interval, n_i in v.vs.items():
            left, right = interval
            x_i = (left + right) / 2
            yield x_i * n_i

    x_ = round(sum(prod_gen()) / v.n, PRECISION)
    print(f'Средняя выработка рабочих: {x_}')


def task2():
    # TODO: медиана - по кумулянте, не по гистограме
    ContinuousVS.PRECISION = 2
    v = ContinuousVS(VALUES1)
    v.draw_hist(1, 1, 1)
    ContinuousVS.show()

    idx = v.n // 2 if v.n % 2 == 0 else v.n / 2
    median = v.values[idx]
    print(f'Медиана: {median}')


def task3():
    v = ContinuousVS(VALUES1)
    idx = v.n // 2 if v.n % 2 == 0 else v.n / 2
    median = v.values[idx]
    print(f'Расчитанная медиана: {median}')

    ys = v.get_cumulate_ys()
    xs = v.get_cumulate_xs()
    y_mid = (max(ys) + min(ys)) / 2
    print(xs, ys)
    # v.draw_cumulate(1, 1, 1)
    # ContinuousVS.show()
