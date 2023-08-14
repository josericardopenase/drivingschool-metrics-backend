#!/bin/bash
# Function to execute the Django command for a specific year and month
function run_dgt_pull_command() {
    year=$1
    month=$2

    if [ "$DJANGO_ENV" = "production" ]; then
        echo "Running Django command for year: $year, month: $month in production environment"
        python3 manage.py dgt_pull $year $month
    else
        echo "Running Django command for year: $year, month: $month in development environment"
        poetry run python3 manage.py dgt_pull $year $month
    fi
}

# Check if the year argument is provided
if [ -z "$1" ]; then
    echo "Please provide the year as an argument."
    exit 1
fi

# Extract the year from the argument
year=$1

# Loop through months from 12 to 1
for month in $(seq 12 -1 1); do
    run_dgt_pull_command $year $month
done
