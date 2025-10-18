from q2_process_metadata import parse_config, validate_config, generate_sample_data, calculate_statistics
# Test parse_config
config = parse_config('q2_config.txt')
assert isinstance(config, dict)
assert isinstance(config, dict)
assert config['sample_data_min'] == '18'

# Test validate_config
test_config = {'sample_data_rows': '100', 'sample_data_min': '18', 'sample_data_max': '75'}
validation = validate_config(test_config)
assert isinstance(validation, dict)
assert validation['sample_data_rows'] == True  # 100 > 0
assert validation['sample_data_min'] == True  # 18 >= 1

# Test generate_sample_data
config = {'sample_data_rows': '10', 'sample_data_min': '18', 'sample_data_max': '75'}
generate_sample_data('test_sample.csv', config)
# Verify file was created and has correct number of lines
with open('test_sample.csv') as f:
    lines = f.readlines()
    assert len(lines) == 10  # 10 rows as specified
# Test calculate_statistics
stats = calculate_statistics([10, 20, 30, 40, 50])
assert stats['mean'] == 30.0
assert stats['median'] == 30.0

print("All tests passed successfully!")
