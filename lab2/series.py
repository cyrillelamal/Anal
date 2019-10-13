import math
import abc
import matplotlib.pyplot as plt


def sorted_by_keys(dict_: dict) -> dict:
    """Return copy of the passed dict sorted by its keys"""
    return {k: dict_[k] for k in sorted(dict_.keys())}


class VariationSeries:
    """Abstract"""
    PRECISION = 1  # {number},{PRECISION}

    def __init__(self, values):
        """
        :param values: all the values that make up the series
        """
        self._vs = None  # Вариационный ряд
        self._values = sorted(values)
        self._n = len(values)
        self._x_max = max(self._values)
        self._x_min = min(self._values)

        self._var_frequencies = None  # Частота варианты - m(i)
        self._rel_frequencies = None  # Относительная частота (частость) - w(i)
        self._acc_frequencies = None  # Накопленная частота - m(x)
        self._acc_rel_frequencies = None  # Накопленная частость w(x)

    def _gen_acc_frequencies(self):
        """Generator"""
        accumulated_sum = 0
        for m_i in self._vs.values():
            yield accumulated_sum
            accumulated_sum += m_i
        yield accumulated_sum

    @staticmethod
    def show():
        plt.show()

    def draw_cumulate(self, nrows, ncols, index):
        xs = self.get_cumulate_xs()
        ys = self.get_cumulate_ys()
        plt.subplot(nrows, ncols, index)
        plt.plot(xs, ys, 'bo--')
        plt.title('Кумулянта')
        plt.xlabel('Интервалы')
        plt.ylabel('Накопленные частоты')

    def draw_empiric_dist_func(
            self, nrows, ncols, index,
            title='Эмпирическая функция распределения',
            postfix=''
    ):
        xs = self.get_empiric_dist_xs()
        ys = self.get_empiric_dist_ys()
        plt.subplot(nrows, ncols, index)
        plt.plot(xs, ys, 'bo--')
        if postfix:
            title += f' {postfix}'
        plt.title(title)
        plt.xlabel('Интервалы')
        plt.ylabel('Накопленные частости')

    @abc.abstractmethod
    def get_cumulate_xs(self) -> list:
        pass

    @abc.abstractmethod
    def get_cumulate_ys(self) -> list:
        pass

    @abc.abstractmethod
    def get_empiric_dist_xs(self) -> list:
        pass

    @abc.abstractmethod
    def get_empiric_dist_ys(self) -> list:
        pass


class DiscreteVS(VariationSeries):
    """Discrete variation series"""
    def __init__(self, values):
        # User's input is a ready variable series: build the list of values
        if isinstance(values, dict):
            vs = sorted_by_keys(values)
            values = []
            for k, v in vs.items():
                values += [k] * v
        # User's input is a list of values: build the variable series
        else:
            vs = {}
            for val in sorted(values):
                vs[val] = vs.get(val, 0) + 1

        super(DiscreteVS, self).__init__(values)
        self._vs = vs

        self._variants = list(self._vs.keys())
        self._var_frequencies = list(self._vs.values())
        self._rel_frequencies = list(map(
            lambda m_i: m_i / self._n, self._var_frequencies
        ))
        self._acc_frequencies = list(self._gen_acc_frequencies())
        self._acc_rel_frequencies = list(map(
            lambda m_x: m_x / self._n, self._acc_frequencies
        ))

        self._x = self.__find_next_x()  # Следующий x

    def __find_next_x(self):
        keys = list(self._vs.keys())
        biggest = keys[-1]
        diff = biggest - keys[-2]
        return biggest + diff

    def draw_polygon(self, nrows, ncols, index):
        xs = self.get_polygon_xs()
        ys = self.get_polygon_ys()
        plt.subplot(nrows, ncols, index)
        plt.plot(xs, ys, 'bo--')
        plt.title('Полигон')
        plt.xlabel('Варианты')
        plt.ylabel('Частоты')

    def get_polygon_xs(self):
        return self._variants

    def get_polygon_ys(self):
        return self._var_frequencies

    def get_cumulate_xs(self):  # x(i)
        return self._variants + [self._x]

    def get_cumulate_ys(self):  # m(x(i))
        return self._acc_frequencies

    def get_empiric_dist_xs(self):  # x(i)
        return self.get_cumulate_xs()

    def get_empiric_dist_ys(self):  # w(x(i))
        return self._acc_rel_frequencies


class ContinuousVS(VariationSeries):
    """Continuous interval"""
    def __init__(self, values):
        # User's input is a dict with intervals
        if isinstance(values, dict):
            # Complete redefinition
            self._vs = values
            self._intervals = list(values.keys())

            values = list(values.keys())  # tuples
            self._n = sum(self._vs.values())
            self._x_max = values[-1][-1]
            self._x_min = values[0][0]

            self._k = math.ceil(1 + 1.4 * math.log(self._n))  # Количество интервалов
            self._delta = (self._x_max - self._x_min) / self._k  # Длина интервала

        # User's input is a list of values
        else:
            super(ContinuousVS, self).__init__(values)

            self._k = math.ceil(1 + 1.4 * math.log(self._n))  # Количество интервалов
            self._delta = (self._x_max - self._x_min) / self._k  # Длина интервала

            self._intervals = self.__make_intervals()
            self._vs = self.__make_vs()

        # self._variants = self._intervals  # Here intervals
        self._var_frequencies = list(self._vs.values())
        self._rel_frequencies = list(map(
            lambda m_i: m_i / self._n, self._var_frequencies
        ))
        self._acc_frequencies = list(self._gen_acc_frequencies())
        self._acc_rel_frequencies = list(map(
            lambda m_x: m_x / self._n, self._acc_frequencies
        ))

    def __make_intervals(self) -> list:
        """Return list of tuples intervals"""
        p = VariationSeries.PRECISION  # Precision
        x_start = self._x_min  # - self._delta / 2  # x(нач)
        x_end = self._x_max + self._delta / 2  # Catch the biggest value
        
        intervals = []
        for i in range(self._k):  # Number of interval
            bias = i * self._delta
            left = round(x_start + bias, p)
            right = round(x_start + self._delta + bias, p)
            intervals += [(left, right)]
        last_interval = intervals[-1]
        new_last_interval = (last_interval[0], x_end)
        intervals[-1] = new_last_interval
        return intervals

    def __make_vs(self) -> dict:
        """Return dict with variable series"""
        vs = {}  # Frequencies
        for val in sorted(self._values):
            # Choose the correct interval
            for interval in self._intervals:
                left, right = interval
                if left <= val < right or val == self._x_max:
                    vs[interval] = vs.get(interval, 0) + 1
                    break
        return vs

    def draw_hist(self):
        xs = self.get_hist_xs()
        ys = self.get_hist_ys()
        fig, ax = plt.subplots()
        ax.bar(xs, ys)
        ax.set_facecolor('seashell')
        fig.set_facecolor('floralwhite')
        fig.set_figwidth(12)
        fig.set_figheight(6)

    def get_hist_xs(self):
        bias = self._delta / 2
        xs = [interval[0] + bias for interval in self._vs.keys()]
        return xs

    def get_hist_ys(self):
        return self._var_frequencies

    def get_cumulate_xs(self):  # a(i)
        xs = [interval[0] for interval in self._vs.keys()] + [self._intervals[-1][1]]
        return xs

    def get_cumulate_ys(self):  # m(a(i))
        return self._acc_frequencies

    def get_empiric_dist_xs(self):
        return self.get_cumulate_xs()

    def get_empiric_dist_ys(self):
        return self._acc_rel_frequencies
