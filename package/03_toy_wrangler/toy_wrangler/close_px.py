##> import pandas_datareader as pdr
##> import numpy as np


##> def close_px(symbol, start, end):
##>     """
##>     grab close prices from yahoo and rounds to two places
##>     """
##>     
##>     # calling pdr function
##>     df_all = pdr.get_data_yahoo(symbol, start=start, end=end)
##>     
##>     # grabbing only the prices that we need
##>     df_close = df_all[['Close']].copy()
##>     
##>     # rounding close prices
##>     df_close['Close'] = np.round(df_close['Close'], 2)
##>     
##>     return(df_close)