from matplotlib import ticker
import matplotlib.pyplot as plt
import numpy as np

class btc_view(object):
    
    def __init__(self) -> None:
        self.fig_n = 1
        plt.style.use('dark_background')

    def plt_add_line(self, y, color = 'r', linestyle='-'):
        plt.axhline(y=y, color=color, linestyle=linestyle)

    def plt_add_scatter(self, x_axis, y_data, label):
        plt.scatter(x_axis, y_data, label=label)

    def plt_normal(self, plt_name, x_axis, *data):

        plt.figure(self._get_figure_n())

        for y_value in data:
            plt.plot(x_axis, y_value)

        plt.title(plt_name)
        plt.grid()
        plt.xticks(rotation = 45)

    def plt_log(self, plt_name, x_axis, *data):

        plt.figure(self._get_figure_n())

        for y_value in data:
            plt.plot(x_axis, y_value)

        plt.title(plt_name)
        plt.grid()
        plt.xticks(rotation = 45)
        plt.yscale("log")
        plt.ylim(bottom = 0.04)
        
    def plt_loglog(self, plt_name, x_axis, *data):

        plt.figure(self._get_figure_n())
        index = [x+1000 for x in range(len(x_axis))]

        for y_value in data:
            plt.loglog(index, y_value) # ÑE ÑE con tiempo

        plt.title(plt_name)
        plt.grid()

        ticks = []
        labels = []
        
        for i in range(len(index)):
            if x_axis[i].is_year_start:
                ticks.append(index[i])
                labels.append(x_axis[i].year)

        plt.xticks(rotation = 45 ,ticks=ticks, labels=labels)
        plt.ylim(bottom = 0.04)
        #plt.xlim(left=100)
    
    def plot(self):
        plt.show()

    ################ AUX FUNCTIONS ################
    def _get_figure_n(self):
        ret = self.fig_n
        self.fig_n += 1
        return ret