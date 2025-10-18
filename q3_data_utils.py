#!/usr/bin/env python3
import pandas as pd
import numpy as np

def load_data(filepath: str) -> pd.DataFrame:
    """
    Load CSV file into DataFrame.
    Args:
        filepath: Path to CSV file
    Returns:
        pd.DataFrame: Loaded data
    """
    return pd.read_csv(filepath)

def clean_data(df: pd.DataFrame, remove_duplicates=True, sentinel_value=-999) -> pd.DataFrame:
    if remove_duplicates:
        df = df.drop_duplicates()
    df = df.replace(sentinel_value, np.nan)
    return df

def detect_missing(df: pd.DataFrame) -> pd.Series:
    return df.isna().sum()

def transform_types(df, type_map: dict):
    result = df.copy()
    for col, target_type in type_map.items():
        if target_type == 'datetime':
            result[col] = pd.to_datetime(result[col], errors='coerce')
        elif target_type == 'numeric':
            result[col] = pd.to_numeric(result[col], errors='coerce')
        elif target_type == 'category':
            result[col] = result[col].astype('category')
    return result

def create_bins(df, column, bins, labels, new_column=None):
    result = df.copy()
    target_col = new_column if new_column else column + '_binned'
    result[target_col] = pd.cut(result[column], bins=bins, labels=labels, include_lowest=True)
    return result

def summarize_by_group(df, group_col, agg_dict=None):
    if agg_dict:
        result = df.groupby(group_col).agg(agg_dict)
    else:
         result = df.groupby(group_col).describe()
    return result.reset_index()

def filter_data(df, filters: list):
    result = df.copy()
    for f in filters:
        col = f['column']
        condition = f['condition']
        value = f['value']

        if condition == 'equals':
            result = result[result[col] == value]
        elif condition == 'greater_than':
            result = result[result[col] > value]
        elif condition == 'less_than':
            result = result[result[col] < value]
        elif condition == 'in_range':
            result = result[(result[col] >= value[0]) & (result[col] <= value[1])]
        elif condition == 'in_list':
            result = result[result[col].isin(value)]

    return result


def fill_missing(df: pd.DataFrame, column: str, strategy='mean') -> pd.DataFrame:
    if strategy == 'mean':
        fill_value = df[column].mean()
        df[column] = df[column].fillna(fill_value)
    elif strategy == 'median':
        fill_value = df[column].median()
        df[column] = df[column].fillna(fill_value)
    elif strategy == 'ffill':
        df[column] = df[column].fillna(method='ffill')
    else:
        raise ValueError(f"Unsupported fill strategy: {strategy}")
    return df

if __name__ == '__main__':
    # Optional: Test your utilities here
    print("Data utilities loaded successfully!")
    print("Available functions:")
    print("  - load_data()")
    print("  - clean_data()")
    print("  - detect_missing()")
    print("  - fill_missing()")
    print("  - filter_data()")
    print("  - transform_types()")
    print("  - create_bins()")
    print("  - summarize_by_group()")

    # Simple test example
    test_df = pd.DataFrame({
        'age': [25, 30, None, 22, -999],
        'bmi': [22, 25, 28, None, -999]
    })
    print("Original test DataFrame:")
    print(test_df)
    
    cleaned_df = clean_data(test_df, sentinel_value=-999)
    print("\nCleaned DataFrame (duplicates removed, sentinel replaced):")
    print(cleaned_df)

    missing_counts = detect_missing(cleaned_df)
    print("\nMissing values per column:")
    print(missing_counts)

    filled_df = fill_missing(cleaned_df, 'age', strategy='median')
    print("\nDataFrame after filling missing 'age' with median:")
    print(filled_df)
