import matplotlib.pyplot as plt
import numpy as np

def log_fitted(df):

    log_btc = np.log(df.close)
    index = [x+1 for x in range(len(df))]
    xdata = np.log(index) #just use numbers for dates

    m, c = np.polyfit(xdata, log_btc, 1, w=np.sqrt(index)) # fit log(y) = m*log(x) + c
    btc_log_curve = np.exp(m*xdata + c) # calculate the fitted values of y 

    plt.style.use('dark_background')
    plt.plot(df.timestamp, df.close, df.timestamp, btc_log_curve)
    plt.xticks(rotation=45)
    plt.yscale("log")
    plt.ylim(bottom=0.04)
    plt.show()