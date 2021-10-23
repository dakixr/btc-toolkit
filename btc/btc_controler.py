from matplotlib.pyplot import close
from btc import btc_model, btc_view

class btc_controller(object):
    
    def __init__(self) -> None:
        self.model = btc_model.btc_model()
        self.view = btc_view.btc_view()

    def log_fit(self):
        """Plots all BTC historical price fitted with a logarithmic curve -> y = e^(a * date + b).
           Log scale."""

        df = self.model.log_fitted()

        self.view.plt_log("BTC Logarithmic fit",
                          df.timestamp,             # x axis
                          df.close,                 # BTC histotical data
                          df.btc_log_curve)         # Logarithmic curve fitted to BTC price
    
    def log(self):
        """Plots all BTC historical price. 
           Log scale."""

        df = self.model.get_histo_daily()

        self.view.plt_log("BTC",
                          df.timestamp,             # x axis
                          df.close)                 # BTC histotical data
    
    def plot(self):
        self.view.plot()