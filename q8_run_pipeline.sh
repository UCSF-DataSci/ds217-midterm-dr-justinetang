#!/bin/bash
LOGFILE="reports/pipeline_log.txt"
mkdir -p reports
echo "Starting clinical trial data pipeline..." > reports/pipeline_log.txt
run_notebook() {
    local nb=$1
    echo "Running $nb..." >> $LOGFILE
    jupyter nbconvert --execute --to notebook "$nb" --output "$nb" >> $LOGFILE 2>&1 || {
        echo "ERROR: $nb failed to execute." >> $LOGFILE
        echo "Pipeline stopped due to error." >> $LOGFILE
        exit 1
    }
    echo "$nb executed successfully." >> $LOGFILE
}

run_notebook q4_exploration.ipynb
run_notebook q5_missing_data.ipynb
run_notebook q6_transformation.ipynb
run_notebook q7_aggregation.ipynb

echo "Pipeline complete!" >> reports/pipeline_log.txt
