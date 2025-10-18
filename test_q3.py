import pandas as pd
import numpy as np
from q3_data_utils import load_data, clean_data, detect_missing, fill_missing, filter_data, transform_types, create_bins, summarize_by_group

# Test load_data
df = load_data('data/clinical_trial_raw.csv')
assert isinstance(df, pd.DataFrame)
assert len(df) > 0  # Has data
assert len(df.columns) > 0  # Has columns

# Test clean_data
cleaned = clean_data(df, remove_duplicates=True, sentinel_value=-999)
assert isinstance(cleaned, pd.DataFrame)

# Test detect_missing
missing = detect_missing(df)
assert isinstance(missing, pd.Series)
assert len(missing) == len(df.columns)  # One count per column

# Test fill_missing with test data
test_df = pd.DataFrame({'col': [1, np.nan, 3]})
filled = fill_missing(test_df, 'col', 'mean')
assert filled['col'].isnull().sum() == 0

# Test filter_data
filters = [{'column': 'age', 'condition': 'greater_than', 'value': 65}]
filtered = filter_data(df, filters)
assert all(filtered['age'] > 65)

# Test multiple filters
filters = [
    {'column': 'age', 'condition': 'greater_than', 'value': 18},
    {'column': 'site', 'condition': 'equals', 'value': 'Site A'}
]
filtered = filter_data(df, filters)
assert all(filtered['age'] > 18)
assert all(filtered['site'] == 'Site A')

# Test in_list condition
filters = [{'column': 'site', 'condition': 'in_list', 'value': ['Site A', 'Site B']}]
filtered = filter_data(df, filters)
assert all(filtered['site'].isin(['Site A', 'Site B']))

# Test in_range condition
filters = [{'column': 'age', 'condition': 'in_range', 'value': [18, 65]}]
filtered = filter_data(df, filters)
assert all(filtered['age'] >= 18)
assert all(filtered['age'] <= 65)

# Test transform_types
type_map = {'enrollment_date': 'datetime', 'site': 'category'}
typed = transform_types(df, type_map)
assert isinstance(typed, pd.DataFrame)

# Test create_bins
binned = create_bins(df, 'age', [0, 40, 60, 100], ['<40', '40-59', '60+'])
assert isinstance(binned, pd.DataFrame)

# Test create_bins with custom column name
binned_custom = create_bins(df, 'age', [0, 40, 60, 100], ['<40', '40-59', '60+'], 'age_groups')
assert isinstance(binned_custom, pd.DataFrame)
assert 'age_groups' in binned_custom.columns

# Test summarize_by_group with custom aggregation
summary = summarize_by_group(df, 'site', {'age': 'mean'})
assert isinstance(summary, pd.DataFrame)

# Test summarize_by_group with default aggregation (agg_dict=None)
summary_default = summarize_by_group(df, 'site')
assert isinstance(summary_default, pd.DataFrame)

print(" All Q3 tests passed successfully!")
