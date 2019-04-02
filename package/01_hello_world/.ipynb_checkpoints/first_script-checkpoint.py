# importing packages
import pandas_datareader as pdr

# reading in data
df_spy = pdr.get_data_yahoo('SPY')

# printing to screen
print("Here is the shape of df_spy:")
print(df_spy.shape)