"""
Лабораторные работы
"""
import matplotlib.pyplot as plt
from .series import Continuous, Discrete


VALUES2 = {
    1: 2, 2: 3, 3: 6, 4: 8, 5: 22, 6: 9
}


def task1():
    values = [
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
    v1 = Continuous(values)
    # Полигон
    plt.subplot(3, 1, 1)
    plt.plot(v1.get_polygon_xs(), v1.get_polygon_ys())
    plt.title('Полигон')
    plt.xlabel('Интервалы')
    plt.ylabel('Частоты')
    # Кумулянта
    plt.subplot(3, 1, 2)
    plt.plot(v1.get_cumulate_xs(), v1.get_cumulate_ys())
    plt.title('Кумулянта')
    plt.xlabel('Интервалы')
    plt.ylabel('Накопленные частоты')
    # Эмпирическая функция распределения
    plt.subplot(3, 1, 3)
    plt.plot(v1.get_empiric_dist_xs(), v1.get_empiric_dist_ys())
    plt.title('Эмпирическая функция распределения рабочих')
    plt.xlabel('Интервалы')
    plt.ylabel('Накопленные частоты')
    xs = v1.get_hist_xs()
    ys = v1.get_hist_ys()
    fig, ax = plt.subplots()
    ax.bar(xs, ys)
    ax.set_facecolor('seashell')
    fig.set_facecolor('floralwhite')
    fig.set_figwidth(12)  # ширина Figure
    fig.set_figheight(6)  # высота Figure
    plt.show()


def task2():
    pass
    # v2 = Discrete(VALUES2)
    # v2.prepare_empiric_dist_func()
    # v2.show()
