from api_wrappers import crypto_compare_api
import numpy as np
from sklearn.linear_model import LinearRegression, RANSACRegressor
from functools import cache


class btc_model(object):
    
    def __init__(self) -> None:
        self.cc = crypto_compare_api.cc()

    def get_histo_daily(self):
        return self.cc.btc_get_histo_daily()
    
    def get_log_fitted(self):

        df = self.get_histo_daily()

        y_log_btc = np.log(df.close)
        index = [x+1000 for x in range(len(df))]
        xdata = np.log(index) #just use numbers for dates

        m, c = np.polyfit(xdata, y_log_btc, 1, w=np.sqrt(index)) # fit log(y) = m*log(x) + c
        btc_log_curve = np.exp(m*xdata + c) # calculate the fitted values of y 
        df["btc_log_curve"] = btc_log_curve

        return df

    def get_log_curves(self, n_lines_over, n_lines_under, delta):

        log_curves = []
        log_curve = self.get_log_fitted()["btc_log_curve"]
        log_curves.append(log_curve)

        under_m = 1 / (1+delta)
        over_m = 1 * (1+delta)

        for _ in range(n_lines_over):
            log_curves.append(log_curve*over_m)
            over_m *= (1+delta)

        for _ in range(n_lines_under):
            log_curves.append(log_curve*under_m)
            under_m /= (1+delta)

        
        return log_curves

    @cache
    def get_ransac_fit(self):


        df = self.get_histo_daily()

        y_log_btc = np.log(df.close)
        index = [x+1000 for x in range(len(df))]
        xdata = np.log(index) #just use numbers for dates

        xdata = xdata.reshape(-1,1)
        ydata = y_log_btc.to_numpy()

        ransac = RANSACRegressor(
            base_estimator=LinearRegression(), 
            max_trials=100, 
            residual_threshold=0.1,
            stop_n_inliers = len(ydata)/2,
            loss='squared_error',
            random_state=0
        )

        ransac.fit(xdata, ydata)

        inlier_mask = ransac.inlier_mask_
        outlier_mask = np.logical_not(inlier_mask)

        df["inlier_mask"] = inlier_mask
        df["outlier_mask"] = outlier_mask
        df["rasnac_fit"] = np.exp(ransac.predict(xdata))

        return df

        
        

