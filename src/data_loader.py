import pandas as pd
from typing import List, Optional

def load_data(
    filepath: str,
    numeric_columns: Optional[List[str]] = None
) -> pd.DataFrame:
    """
    Load dataset into a pandas DataFrame and convert specified columns to numeric types.
    
    Args:
        filepath: Path to the CSV file
        numeric_columns: List of column names to convert to float.
                        Defaults to None (no conversion)
        
    Returns:
        DataFrame with specified columns converted to float type
    """
    df = pd.read_csv(filepath)

    # Convert Date column to datetime
    df['Date'] = pd.to_datetime(df['Date'])

    # Set as index
    df.set_index('Date', inplace=True)

    # Remove timezone (only if it exists)
    if df.index.tz is not None:
        df.index = df.index.tz_localize(None)

    # Convert numeric columns
    df = df.astype({
        'Open': 'float64',
        'High': 'float64',
        'Low': 'float64',
        'Close': 'float64',
        'Volume': 'float64'
    })

    return df

def handle_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    """
    Check for and handle missing values in the DataFrame.
    
    Args:
        df: The DataFrame to process.
        method: The method to use for filling missing values. 
                Options are 'ffill' for forward fill or 'bfill' for backward fill.
                
    Returns:
        DataFrame with missing values handled.
    """
    print("Checking for missing values...")
    print(f"Found {df.isnull().sum().sum()} missing values. Filling with ffill.")
    if df.isnull().values.any():
        df.ffill(inplace=True)
    return df