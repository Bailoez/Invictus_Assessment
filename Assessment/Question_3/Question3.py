import pandas as pd
import requests
import numpy as np
import plotly.graph_objects as go
import matplotlib.pyplot as plot

# get BTC/USD and ETH/USD spot and PERP markets
historical_BTC = requests.get('https://ftx.com/api/markets/BTC/USD/candles?resolution=86400'
                              '&start_time=1595457814&end_time=1626993814').json()
historical_ETH = requests.get('https://ftx.com/api/markets/ETH/USD/candles?resolution=86400'
                              '&start_time=1595457814&end_time=1626993814').json()
historical_BTC_PERP = requests.get('https://ftx.com/api/markets/BTC-PERP/candles?resolution=86400'
                              '&start_time=1595457814&end_time=1626993814').json()
historical_ETH_PERP = requests.get('https://ftx.com/api/markets/ETH-PERP/candles?resolution=86400'
                              '&start_time=1595457814&end_time=1626993814').json()

historical_BTC = pd.DataFrame(historical_BTC['result'])
historical_ETH = pd.DataFrame(historical_ETH['result'])
historical_BTC_PERP = pd.DataFrame(historical_BTC_PERP['result'])
historical_ETH_PERP = pd.DataFrame(historical_ETH_PERP['result'])
historical_BTC.drop(['startTime'], axis=1, inplace=True)  # start time known - indicated in url in UNIX time
historical_ETH.drop(['startTime'], axis=1, inplace=True)  # start time known - indicated in url in UNIX time
historical_BTC_PERP.drop(['startTime'], axis=1, inplace=True)
historical_ETH_PERP.drop(['startTime'], axis=1, inplace=True)
historical_ETH.head()
historical_BTC.head()
historical_BTC_PERP.head()
historical_ETH_PERP.head()

# printing historical closing prices for BTC/USD and ETH/USH in 5 minute OHLC csv format
print("Historical 5 min OHLC of BTC/USD in csv format:\n ", historical_BTC)
print("Historical 5 min OHLC of ETH/USD in csv format:\n ", historical_ETH)
print("Historical 5 min OHLC of BTC-PERP in csv format:\n ", historical_BTC_PERP)
print("Historical 5 min OHLC of ETH-PERP in csv format:\n ", historical_ETH_PERP)

historical_BTC['time'] = pd.to_datetime(historical_BTC['time'], unit='ms')
historical_BTC.set_index('time', inplace=True)
historical_BTC['20 SMA'] = historical_BTC.close.rolling(20).mean()
historical_BTC.tail()

fig = go.Figure(data=[go.Candlestick(x=historical_BTC.index,
                                     open=historical_BTC['open'],
                                     high=historical_BTC['high'],
                                     low=historical_BTC['low'],
                                     close=historical_BTC['close'],
                                     ),
                      go.Scatter(x=historical_BTC.index, y=historical_BTC['20 SMA'],
                                 line=dict(color='purple', width=1))])

fig.show()
# end of pulling historical data from FTX API code
#################################################

# sharpe a sortino ratios
r_p = (32295 / 9610.5) * 100  # closing price 1 year ago/closing price today as percentage (market return)


def sharpe(returns, rf=0, days=365):
    volatility = returns.std() * np.sqrt(days)
    sharpe_ratio = (returns.mean() - rf) / volatility
    return sharpe_ratio


def information_ratio(returns, benchmark_returns, days=252):
    return_difference = returns - benchmark_returns
    volatility = return_difference.std() * np.sqrt(days)
    information_ratio_btc_eth = return_difference.mean() / volatility
    return information_ratio_btc_eth


def downside_risk(returns, risk_free=0):        # taking risk free % as 0
    adj_returns = returns - risk_free
    sqr_downside = np.square(np.clip(adj_returns, np.NINF, 0))
    return np.sqrt(np.nanmean(sqr_downside) * 252)


def sortino(returns, risk_free=0):              # taking risk free % as 0
    adj_returns = returns - risk_free
    d_risk = downside_risk(adj_returns)

    if d_risk == 0:
        return np.nan

    return (np.nanmean(adj_returns) * np.sqrt(252)) \
           / d_risk


def error_track(arg1):
    tracking_err = np.std((historical_BTC['close'] - arg1)
                          / arg1)
    return tracking_err


print("Sharpe ratio BTC: ", sharpe(historical_BTC['close']))
print("Sortino ratio: ", sortino(historical_BTC['close']))
print("Sharpe ratio ETH: ", sharpe(historical_ETH['close']))
print("Sortino ratio: ", sortino(historical_ETH['close']))
#print("Information ratio of BTC with respect to ETH: ", information_ratio(historical_BTC['close'],
                                                                          #historical_ETH['close']))
print("Tracking error spot BTC vs perpetual: ", error_track(historical_BTC_PERP['close']))
