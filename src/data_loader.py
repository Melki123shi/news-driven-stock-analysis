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
    
    if numeric_columns:
        for col in numeric_columns:
            if col in df.columns:
                df[col] = pd.to_numeric(df[col], errors='coerce')
    
    return df

def handle_missing_values(df: pd.DataFrame, method: str = 'ffill') -> pd.DataFrame:
    """
    Check for and handle missing values in the DataFrame.
    
    Args:
        df: The DataFrame to process.
        method: The method to use for filling missing values. 
                Options are 'ffill' for forward fill or 'bfill' for backward fill.
                
    Returns:
        DataFrame with missing values handled.
    """
    if method == 'ffill':
        df.fillna(method='ffill', inplace=True)
    elif method == 'bfill':
        df.fillna(method='bfill', inplace=True)
    return df

def remove_nulls(df):
    """Remove rows that have any missing values. Print a summary of what was removed."""
    before = len(df)
    df = df.dropna()
    after = len(df)
    removed = before - after
    if removed > 0:
        print(f"Removed {removed} row(s) with missing values. {after} rows remaining.")
    else:
        print(f"No missing values found. All {after} rows kept.")
    return df