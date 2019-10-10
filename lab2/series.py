import math
import abc
import matplotlib.pyplot as plt


def sorted_by_keys(dict_: dict) -> dict:
    """Return sorted by keys copy of the passed dict"""
    return {k: dict_[k] for k in sorted(dict_.keys())}


class Interval:
    """Abstract class representing an interval"""
    PRECISION = 1

    def __init__(self, values):
        self._values = values
        self.n = len(values)
        self.max = max(self._values)
        self.min = min(self._values)

    def prepare_polygon(self):
        """Draw polygon"""
        xs = self.get_polygon_xs()
        ys = self.get_polygon_ys()
        plt.plot(xs, ys)
        plt.title('Полигон')
        plt.ylabel('Частоты')
        plt.xlabel('Значения')
        return self

    def prepare_histogram(self):
        """Draw histogram"""
        xs = self.get_hist_xs()
        ys = self.get_hist_ys()
        fig, ax = plt.subplots()
        ax.bar(xs, ys)
        ax.set_facecolor('seashell')
        fig.set_facecolor('floralwhite')
        fig.set_figwidth(12)  # ширина Figure
        fig.set_figheight(6)  # высота Figure
        return self

    def prepare_cumulate(self):
        """Draw cumulate function"""
        xs = self.get_cumulate_xs()
        ys = self.get_cumulate_ys()
        plt.plot(xs, ys)
        plt.title('Кумулянта')
        plt.xlabel('Значения')
        return self

    def prepare_empiric_dist_func(self):
        """Draw empiric distribution function"""
        xs = self.get_empiric_dist_xs()
        ys = self.get_empiric_dist_ys()
        plt.plot(xs, ys)
        plt.title('Эмпирическая функция распределения')
        return self

    @staticmethod
    def show():
        plt.show()

    @abc.abstractmethod
    def get_polygon_xs(self) -> list:
        pass

    @abc.abstractmethod
    def get_polygon_ys(self) -> list:
        pass

    @abc.abstractmethod
    def get_hist_xs(self) -> list:
        pass

    @abc.abstractmethod
    def get_hist_ys(self) -> list:
        pass

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


class Discrete(Interval):
    """Discrete interval"""
    def __init__(self, values):
        # User's input is ready variable series
        if isinstance(values, dict):
            values = sorted_by_keys(values)
            self.variable_series = values
            vals = []
            for k, v in values.items():
                vals.extend([k]*v)
            values = vals  # self._values (all values)
        # User's input is a list of values
        else:
            vs = {}
            for val in sorted(values):
                vs[val] = vs.get(val, 0) + 1
            self.variable_series = vs
        # Else errors are thrown
        super(Discrete, self).__init__(values)

    def get_polygon_xs(self):
        return list(self.variable_series.keys())  # x(i)

    def get_polygon_ys(self):
        return list(self.variable_series.values())  # Frequencies - m(i)

    def get_hist_xs(self):
        raise ValueError(
            'Гистограмма служит только '
            'для представления интервальных '
            'вариационных рядов'
        )

    def get_hist_ys(self):
        raise ValueError(
            'Гистограмма служит только '
            'для представления интервальных '
            'вариационных рядов'
        )

    def get_cumulate_xs(self):  # x(i)
        keys = list(self.variable_series.keys())
        last_key = keys[-1]
        last_key += 1
        keys += [last_key]
        return keys

    def get_cumulate_ys(self):  # m(x(i))
        def y_gen():
            accumulated_sum = 0
            for m_i in self.variable_series.values():
                yield accumulated_sum
                accumulated_sum += m_i
            yield accumulated_sum
        return list(y_gen())

    def get_empiric_dist_xs(self):  # x(i)
        return self.get_cumulate_xs()

    def get_empiric_dist_ys(self):  # w(x)
        return [m_x / self.n for m_x in self.get_cumulate_ys()]


class Continuous(Interval):
    """Continuous interval"""
    def __init__(self, values):
        super(Continuous, self).__init__(values)
        self.k = math.ceil(1 + 1.4 * math.log(self.n))
        self.delta = (self.max - self.min) / self.k

        p = Interval.PRECISION  # Precision alias
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
                if left <= val <= right:
                    vs[interval] = vs.get(interval, 0) + 1
        self.variable_series = vs

    def get_polygon_xs(self):
        bias = self.delta / 2
        xs = [interval[0] + bias for interval in self.variable_series.keys()]
        return xs

    def get_polygon_ys(self):
        return [y for y in self.variable_series.values()]

    def get_hist_xs(self):
        x_min = self.intervals[0][0]
        center = self.delta / 2
        xs = [
            x_min + center + self.delta * i
            for i in range(self.k)
        ]
        return xs

    def get_hist_ys(self):
        return list(self.variable_series.values())

    def get_cumulate_xs(self):  # a(i)
        xs = [interval[0] for interval in self.intervals] \
             + [self.intervals[-1][1]]
        return xs

    def get_cumulate_ys(self):  # m(a(i))
        def y_gen():
            accumulated_sum = 0
            for a_i in self.variable_series.values():
                yield accumulated_sum
                accumulated_sum += a_i
            yield accumulated_sum
        return list(y_gen())

    def get_empiric_dist_xs(self):
        return self.get_cumulate_xs()

    def get_empiric_dist_ys(self):
        return [m_x / self.n for m_x in self.get_cumulate_ys()]
