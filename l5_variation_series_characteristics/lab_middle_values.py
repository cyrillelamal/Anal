from variation_series import ContinuousVS, DiscreteVS


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
VALUES2 = {
        1: 2, 2: 3, 3: 6, 4: 8, 5: 22, 6: 9
}


def task1():
    ContinuousVS.PRECISION = 2
    v = ContinuousVS(VALUES1)

    def prod_gen():
        for interval, n_i in v.vs.items():
            left, right = interval
            x_i = (left + right) / 2
            yield x_i * n_i

    x_ = round(sum(prod_gen()) / v.n, PRECISION)
    print(f'1. Средняя выработка рабочих: {x_}')


def task2():
    DiscreteVS.PRECISION = 2
    v = DiscreteVS(VALUES2)
    print(f'2. Медиана (перпендикуляр): {v.count_median()}')


def task3():
    v = ContinuousVS(VALUES1)
    print(f'3. Медиана (перпендикуляр): {v.count_median()}')


def task4():
    v = DiscreteVS(VALUES2)
    print(f'4. Мода (пик): {v.count_mode()}')
    print(f'4. Медиана (перпендикуляр): {v.count_median()}')


def task5():
    v = ContinuousVS(VALUES1)
    print(f'5. Мода (пик): {v.count_mode()}')
