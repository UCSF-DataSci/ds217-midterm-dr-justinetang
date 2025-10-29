#!/usr/bin/env python3
import random
import statistics
import os
def parse_config(filepath: str) -> dict:
    config = {}
    with open(filepath, 'r') as file:
        for line in file:
            line = line.strip()
            if '=' in line:
                key, value = line.split('=', 1)
                config[key.strip()] = value.strip()
    return config

def validate_config(config: dict) -> dict:
    results = {}
    try:
        rows = int(config.get('sample_data_rows', ''))
        results['sample_data_rows'] = rows > 0
    except (ValueError, TypeError):
        results['sample_data_rows'] = False
# sample_data_min
    try:
        min_val = int(config.get('sample_data_min', ''))
        results['sample_data_min'] = min_val >= 1
    except (ValueError, TypeError):
        results['sample_data_min'] = False
# sample_data_max
    try:
        max_val = int(config.get('sample_data_max', ''))
        if results.get('sample_data_min', False):
            results['sample_data_max'] = max_val > min_val
        else:
            results['sample_data_max'] = False
    except (ValueError, TypeError):
        results['sample_data_max'] = False

    return results

def generate_sample_data(filename: str, config: dict) -> None:
    rows = int(config['sample_data_rows'])
    min_val = int(config['sample_data_min'])
    max_val = int(config['sample_data_max'])
    dir_name = os.path.dirname(filename)
    if dir_name:  # only create directory if it exists
        os.makedirs(dir_name, exist_ok=True)
    with open(filename, 'w') as f:
        for _ in range(rows):
            num = random.randint(min_val, max_val)
            f.write(f"{num}\n")

def calculate_statistics(data: list) -> dict:
    count = len(data)
    total = sum(data) if count else 0
    mean = statistics.mean(data) if count else 0
    median = statistics.median(data) if count else 0
    return {
        'mean': mean,
        'median': median,
        'sum': total,
        'count': count
    }

def main():
    config_file = 'q2_config.txt'
    config = parse_config(config_file)
    validation = validate_config(config)
    if not all(validation.values()):
        print("Config validation failed:")
        for key, valid in validation.items():
            print(f"  {key}: {'PASS' if valid else 'FAIL'}")
        return

    data_file = 'data/sample_data.csv'
    generate_sample_data(data_file, config)

    with open(data_file, 'r') as f:
        data = [int(line.strip()) for line in f if line.strip().isdigit()]

    stats = calculate_statistics(data)
    os.makedirs('output', exist_ok=True)

    with open('output/statistics.txt', 'w') as f:
        for key, value in stats.items():
            f.write(f"{key}: {value}\n")
if __name__ == '__main__':
    main()
