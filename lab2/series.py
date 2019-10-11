import math
import abc
import matplotlib.pyplot as plt


def sorted_by_keys(dict_: dict) -> dict:
    """Return sorted by keys copy of the passed dict"""
    return {k: dict_[k] for k in sorted(dict_.keys())}


class VariationSeries:
    """Abstract"""
    PRECISION = 1  # {number},{PRECISION}

    def __init__(self, values):
        self._values = values
        self.n = len(values)
        self.max = max(self._values)
        self.min = min(self._values)

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
        # User's input is ready variable series
        if isinstance(values, dict):
            self.vs = sorted_by_keys(values)
            selection = []
            for k, v in values.items():
                selection.extend([k]*v)
            values = selection  # self._values (all values)
        # User's input is a list of values
        else:
            self.vs = {}
            for val in sorted(values):
                self.vs[val] = self.vs.get(val, 0) + 1
        # Else errors are thrown
        # Save the list of values
        super(DiscreteVS, self).__init__(values)

    def draw_polygon(self, nrows, ncols, index):
        xs = self.get_polygon_xs()
        ys = self.get_polygon_ys()
        plt.subplot(nrows, ncols, index)
        plt.plot(xs, ys, 'bo--')
        plt.title('Полигон')
        plt.xlabel('Варианты')
        plt.ylabel('Частоты')

    def get_polygon_xs(self):
        return list(self.vs.keys())  # x(i)

    def get_polygon_ys(self):
        return list(self.vs.values())  # m(i)  (Frequencies)

    def get_cumulate_xs(self):  # x(i)
        keys = list(self.vs.keys())
        last_key = keys[-1]
        last_key += 1
        keys += [last_key]
        return keys

    def get_cumulate_ys(self):  # m(x(i))
        def y_gen():
            accumulated_sum = 0
            for m_i in self.vs.values():
                yield accumulated_sum
                accumulated_sum += m_i
            yield accumulated_sum
        return list(y_gen())

    def get_empiric_dist_xs(self):  # x(i)
        return self.get_cumulate_xs()

    def get_empiric_dist_ys(self):  # w(x)
        return [m_x / self.n for m_x in self.get_cumulate_ys()]


class ContinuousVS(VariationSeries):
    """Continuous interval"""
    def __init__(self, values):
        super(ContinuousVS, self).__init__(values)
        self.k = math.ceil(1 + 1.4 * math.log(self.n))
        self.delta = (self.max - self.min) / self.k

        p = VariationSeries.PRECISION  # Precision alias
        # INTERVALS
        self.intervals = [
            (round(self.min + bias, p), round(self.min + bias + self.delta, p))
            for bias in (i * self.delta for i in range(self.k))
        ]

        # VARIABLE SERIES
        vs = {}  # Frequencies
        for val in sorted(self._values):
            # Choose the correct interval
            for interval in self.intervals:
                left, right = interval
                if left <= val < right or val == self.max:
                    vs[interval] = vs.get(interval, 0) + 1
        self.vs = vs

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
        x_min = self.intervals[0][0]
        center = self.delta / 2
        xs = [
            x_min + center + self.delta * i
            for i in range(self.k)
        ]
        return xs

    def get_hist_ys(self):
        return list(self.vs.values())

    def get_cumulate_xs(self):  # a(i)
        xs = [interval[0] for interval in self.intervals] \
             + [self.intervals[-1][1]]
        return xs

    def get_cumulate_ys(self):  # m(a(i))
        def y_gen():
            accumulated_sum = 0
            for a_i in self.vs.values():
                yield accumulated_sum
                accumulated_sum += a_i
            yield accumulated_sum
        return list(y_gen())

    def get_empiric_dist_xs(self):
        return self.get_cumulate_xs()

    def get_empiric_dist_ys(self):
        return [m_x / self.n for m_x in self.get_cumulate_ys()]
