import backtest_py

print((backtest_py.option_func.option_chain(True)).shape)

print((backtest_py.option_func.option_chain(False)).shape)

print((backtest_py.option_func.option_underlying(True)).shape)

print((backtest_py.option_func.option_underlying(False)).shape)
