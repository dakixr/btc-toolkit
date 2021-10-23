import matplotlib.pyplot as plt
import numpy as np

class btc_view(object):
    
    def __init__(self) -> None:
        self.fig_n = 1
        plt.style.use('dark_background')

    def plt_log(self, plt_name, x_axis, *data):

        plt.figure(self._get_figure_n())

        for y_value in data:
            plt.plot(x_axis, y_value)

        plt.title(plt_name)
        plt.xticks(rotation = 45)
        plt.yscale("log")
        plt.ylim(bottom = 0.04)
    
    def plot(self):
        plt.show()

    ################ AUX FUNCTIONS ################
    def _get_figure_n(self):
        ret = self.fig_n
        self.fig_n += 1
        return ret