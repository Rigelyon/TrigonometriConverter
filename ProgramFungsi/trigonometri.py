import numpy as np

class Trigonometri:
    def __init__(self):
        pass

    def table_sin(self, left_entry, right_entry, x_range):
        y = ["f(x)"]
        for i in x_range:
            result = left_entry*np.sin(right_entry*np.radians(i))
            y.append(round(result,3))
        return y

    def graph_sin(self, left_entry, right_entry, x_range):
        x = x_range
        for i in x_range:
            y = left_entry * np.sin(right_entry * x)
        return y 

    def table_cos(self, left_entry, right_entry, x_range):
        y = ["f(x)"]
        for i in x_range:
            result = left_entry*np.cos(right_entry*np.radians(i))
            y.append(round(result,3))
        return y

    def graph_cos(self, left_entry, right_entry, x_range):
        x = x_range
        for i in x_range:
            y = left_entry * np.cos(right_entry * x)
        return y 

    def table_tan(self, left_entry, right_entry, x_range):
        y = ["f(x)"]
        for i in x_range:
            result = left_entry * np.tan(right_entry*np.radians(i))
            if result > 1000 or result < -1000:
                y.append(np.inf)
            else:
                y.append(round(result,3))
        return y

    def graph_tan(self, left_entry, right_entry, x_range):
        x = x_range
        for i in x_range:
            y = left_entry * np.tan(right_entry * x)
        return y 

    def table_cosec(self, left_entry, right_entry, x_range):
        y = ["f(x)"]
        for i in x_range:
            sin_value = np.sin(right_entry * np.radians(i))
            cosec_value = 1 / sin_value if sin_value != 0 else np.inf
            result = left_entry * cosec_value
            if result > 1000 or result < -1000:
                y.append(np.inf)
            else:
                y.append(round(result, 3))
        return y

    def graph_cosec(self, left_entry, right_entry, x_range):
        x = x_range
        for i in x_range:
            sin_value = np.sin(right_entry * x)
            y = left_entry * (1 / sin_value)
        return y 

    def table_sec(self, left_entry, right_entry, x_range):
        y = ["f(x)"]
        for i in x_range:
            cos_value = np.cos(right_entry * np.radians(i))
            sec_value = 1 / cos_value if cos_value != 0 else np.inf
            result = left_entry * sec_value
            if result > 1000 or result < -1000:
                y.append(np.inf)
            else:
                y.append(round(result, 3))
        return y

    def graph_sec(self, left_entry, right_entry, x_range):
        x = x_range
        for i in x_range:
            cos_value = np.cos(right_entry * x)
            y = left_entry * (1 / cos_value)
        return y 

    def table_cotan(self, left_entry, right_entry, x_range):
        y = ["f(x)"]
        for i in x_range:
            tan_value = np.tan(right_entry * np.radians(i))
            cotan_value = 1 / tan_value if tan_value != 0 else np.inf
            result = left_entry * cotan_value
            if result > 1000 or result < -1000:
                y.append(np.inf)
            else:
                y.append(round(result, 3))
        return y

    def graph_cotan(self, left_entry, right_entry, x_range):
        x = x_range
        for i in x_range:
            tan_value = np.cos(right_entry * x)
            y = left_entry * (1 / tan_value)
        return y 