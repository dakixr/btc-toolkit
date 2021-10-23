from api_wrappers import crypto_compare_api
import numpy as np

class btc_model(object):
    
    def __init__(self) -> None:
        self.cc = crypto_compare_api.cc()

    def get_histo_daily(self):
        return self.cc.btc_get_histo_daily()
    
    def log_fitted(self):

        df = self.get_histo_daily()
        log_btc = np.log(df.close)
        index = [x+1 for x in range(len(df))]
        xdata = np.log(index) #just use numbers for dates

        m, c = np.polyfit(xdata, log_btc, 1, w=np.sqrt(index)) # fit log(y) = m*log(x) + c
        btc_log_curve = np.exp(m*xdata + c) # calculate the fitted values of y 
        df["btc_log_curve"] = btc_log_curve

        return df