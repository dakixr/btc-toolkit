from btc import btc_model, btc_view
import numpy as np

class btc_controller(object):

    
    def __init__(self) -> None:
        self.model = btc_model.btc_model()
        self.view = btc_view.btc_view()

        self.func_view = {
        "log": self.view.plt_log,
        "loglog": self.view.plt_loglog,
        "normal": self.view.plt_normal
        }

    def model_rasnac(self, view = "log", name = "BTC - Regresión robusta RASNAC"):

        df = self.model.get_ransac_fit()

        self.func_view[view](
            name,
            df.timestamp,
            df.close,
            df.rasnac_fit
        )
        
        if view == "loglog":
            x_axis = np.array([x+1000 for x in range(len(df))])[df.inlier_mask]
        else:
            x_axis = df.timestamp[df.inlier_mask]

        self.view.plt_add_scatter(
            x_axis=x_axis,
            y_data=df.close[df.inlier_mask],
            label="Inliners")

    def oscilator_rasnac(self, view = "normal", name = "BTC - Oscilador RASNAC"):

        df = self.model.get_ransac_fit()

        self.func_view[view](
            name,
            df.timestamp,
            np.log(df.close/df.rasnac_fit)
        )

        self.view.plt_add_line(y=0)


    def oscilator_log_model(self, view = "normal", name = "BTC - Oscilador Modelo Logaritmico"):

        df = self.model.get_log_fitted()

        self.func_view[view](
            name,
            df.timestamp,
            np.log(df.close/df.btc_log_curve)

        )
        
        self.view.plt_add_line(y=0)

    def model_log(self, view = "log", name = "BTC - Regresión Logarítmica"):
        """Plots all BTC historical price fitted with a logarithmic curve -> y = e^(a * date + b).
           Log scale."""

        df = self.model.get_log_fitted()

        self.func_view[view](
            name,
            df.timestamp,             # x axis
            df.close,                 # BTC histotical data
            df.btc_log_curve)         # Logarithmic curve fitted to BTC price
    
    def price(self, view = "log", name = "BTC - Precio histórico"):
        """Plots all BTC historical price. """

        df = self.model.get_histo_daily()

        self.func_view[view](
            name,
            df.timestamp,             # x axis
            df.close)                 # BTC histotical data

    def model_log_curves(self, n_lines_over = 7, n_lines_under = 2, delta = 0.7, view = "log", name = "BTC - Modelo de Curvas Logarítmicas"):

        df = self.model.get_histo_daily()
        curves = self.model.get_log_curves(n_lines_over, n_lines_under, delta)

        self.func_view[view](
            name,
            df.timestamp,
            df.close,
            *curves)

    def plot(self):
        self.view.plot()
