#!/bin/bash
set -e
echo "setting up project directories"
mkdir -p data
mkdir -p output
mkdir -p reports
echo "Directories created: data/, output/, reports/"
echo "Generating dataset"
python3 generate_data.py
echo "Dataset generated: data/clinical_trial_raw.csv"
echo "Saving directory structure to reports/directory_structure.txt"
if command -v tree &> /dev/null
then
	tree . > reports/directory_structure.txt
else
	ls -laR . > reports/directory_structure.txt
fi

echo "Directory structure saved in reports/directory_structure.txt"
echo "Q1 setup complete."
