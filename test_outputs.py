import os
import pandas as pd

# Q4 outputs
assert os.path.exists('output/q4_site_counts.csv')
df = pd.read_csv('output/q4_site_counts.csv')
assert len(df) >= 1  # Has at least one site
assert len(df.columns) >= 2  # Has site and count columns
assert df.iloc[:, 1].sum() > 0  # Counts sum to positive number

# Q2 outputs
assert os.path.exists('data/sample_data.csv')
assert os.path.exists('output/statistics.txt')

# Q5 outputs
assert os.path.exists('output/q5_cleaned_data.csv')
assert os.path.exists('output/q5_missing_report.txt')

# Q6 outputs
assert os.path.exists('output/q6_transformed_data.csv')
original = pd.read_csv('data/clinical_trial_raw.csv')
transformed = pd.read_csv('output/q6_transformed_data.csv')
assert len(transformed.columns) > len(original.columns)

# Q7 outputs
assert os.path.exists('output/q7_site_summary.csv')
summary = pd.read_csv('output/q7_site_summary.csv')
assert len(summary) >= 1  # Has at least one site
