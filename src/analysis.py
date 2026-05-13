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

def normalize_timestamps(news_df, stock_df, sticker, news_date_col='date', stock_date_col='Date'):
    """
    Normalize timestamps across news and stock datasets to match news items
    to corresponding stock trading days.
    """

    # Convert all timestamps to UTC first
    news_df[news_date_col] = pd.to_datetime(
        news_df[news_date_col],
        errors='coerce',
        utc=True
    )

    stock_df[stock_date_col] = pd.to_datetime(
        stock_df[stock_date_col],
        errors='coerce',
        utc=True
    )
    # Remove timezone info to make both tz-naive
    news_df[news_date_col] = news_df[news_date_col].dt.tz_localize(None)
    stock_df[stock_date_col] = stock_df[stock_date_col].dt.tz_localize(None)

    print(f"News timestamps after timezone normalization:\n{news_df[news_date_col].head()}\n")
    print(f"{sticker} Stock timestamps after timezone normalization:\n{stock_df[stock_date_col].head()}")

    # Step 5: Assign trading date from news timestamp
    # Create sorted list of available trading dates from stock data
    trading_dates = pd.to_datetime(stock_df[stock_date_col]).dt.date.dropna().unique()
    trading_dates = sorted(trading_dates)

    # Helper to find next trading date >= given date
    def next_trading_date(d):
        # if already a trading date return it
        if d in trading_dates:
            return d
        # find first trading date after d
        for td in trading_dates:
            if td >= d:
                return td
        # if no future trading date found, return last available trading date
        return trading_dates[-1] if trading_dates else d

    # Assign trading_date: map weekends/holidays to next available trading day
    news_df['trading_date'] = (
        news_df[news_date_col]
        .dt.date
        .apply(lambda d: next_trading_date(d) if pd.notnull(d) else d)
    )

    return news_df


def plot_news_by_day(normalized_news, title_suffix):
    """Plot news articles distribution by day of week."""
    normalized_news['trading_date'] = pd.to_datetime(normalized_news['trading_date'])
    news_by_day = normalized_news['trading_date'].dt.day_name().value_counts()
    
    # Reorder by day of week (Monday to Sunday)
    day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    news_by_day = news_by_day.reindex(day_order)
    
    plt.figure(figsize=(10, 5))
    news_by_day.plot(kind='bar', color='steelblue')
    plt.xlabel('Day of Week')
    plt.ylabel('Number of News Articles')
    plt.title(f'News Articles Distribution by Day of Week ({title_suffix})')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()