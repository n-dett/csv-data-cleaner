# csv-data-cleaner

csv-data-cleaner is a simple Python script for cleaning messy CSV files. It reads a CSV file, applies a series of data cleaning steps, and writes a cleaned version to a new file.

## Features

The script performs the following cleaning operations:

- Removes leading and trailing whitespace from column names
- Converts all column names to lowercase
- Replaces spaces and special characters in column names with underscores
- Standardizes date formats
- Replaces empty values with placeholders
- Aggregates duplicate entries
- Saves the cleaned data to `cleaned_data.csv`

