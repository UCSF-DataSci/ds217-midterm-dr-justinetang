import os

# Q1 executable check
assert os.access('q1_setup_project.sh', os.X_OK)
with open('q1_setup_project.sh') as f:
    assert f.readline().startswith('#!/bin/bash')

# Q1 outputs
assert os.path.exists('data/')
assert os.path.exists('output/')
assert os.path.exists('reports/')
assert os.path.exists('reports/directory_structure.txt')

# Q8 outputs
assert os.path.exists('reports/pipeline_log.txt')

