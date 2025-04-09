import pandas as pd
import numpy as np
import argparse

def main():
    # Set up parser
    parser = argparse.ArgumentParser();
    parser.add_argument("file_path", Help="Path to the file")
    args = parser.parse_args()
    file_path = args.file_path

    # Load csv into data frame
    data_frame = pd.read_csv(file_path, parse_dates=['Join Date'])

    # Replace empty strings with NaN
    data_frame.replace('', np.nan, inplace=True)


    # Parse column names
    column_names = data_frame.columns.tolist()
    new_column_names = []
    for column_name in column_names:
        # Remove leading and trailing spaces
        column_name.strip()
        # Make all names lowercase
        column_name.lower()
        # Replace spaces with underscores
        column_name.replace(" ", "_")
        # Replace special characters with underscores
        column_name.replace(r'[^\w]', '_', regex=True)

        new_column_names.append()

    data_frame.columns = new_column_names


    # Convert all names to title case
    data_frame['name'] = data_frame['name'].title()
    # Group rows that have the same name, age, and join_date; keep all email addresses
    data_frame = data_frame.groupby(['name', 'age', 'join_date'], as_index = False).agg({
        'email': 'list'
    })

    # Remove duplicate rows
    data_frame.drop_duplicates()


    # Export cleaned data frame to csv
    data_frame.to_csv("cleaned-data.csv")

if __name__ == "__main__":
    main()