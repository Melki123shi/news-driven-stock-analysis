import talib
import pandas as pd
import matplotlib.pyplot as plt

def calculate_indicators(df, ma_periods=[20, 50, 200], bb_period=20):
    """
    Calculates BBANDS, SMA, and EMA for multiple windows.
    """
    # 1. Calculate Bollinger Bands
    # matype=0 is SMA, matype=1 is EMA
    df['upper_band'], df['middle_band'], df['lower_band'] = talib.BBANDS(
        df['Close'], 
        timeperiod=bb_period, 
        nbdevup=2, 
        nbdevdn=2, 
        matype=0
    )

    # 2. Calculate Multiple SMAs and EMAs
    for period in ma_periods:
        df[f'SMA_{period}'] = talib.SMA(df['Close'], timeperiod=period)
        df[f'EMA_{period}'] = talib.EMA(df['Close'], timeperiod=period)
    
    return df
 
def add_and_plot_moving_averages(df, windows, plot_rows=200):
    price_col = 'Close' if 'Close' in df.columns else ('close' if 'close' in df.columns else df.columns[-1])

    for w in windows:
        df[f'SMA_{w}'] = df[price_col].rolling(window=w, min_periods=1).mean()
        df[f'EMA_{w}'] = df[price_col].ewm(span=w, adjust=False).mean()

    cols = [price_col] + [f'SMA_{w}' for w in windows] + [f'EMA_{w}' for w in windows]

    df[cols].tail()

    df[cols].tail(plot_rows).plot(figsize=(12, 6))
    plt.title('Price with SMA and EMA')
    plt.show()

    return df