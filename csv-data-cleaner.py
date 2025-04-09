import pandas as pd
import numpy as np
import argparse
import re

def main():
    # Set up parser
    parser = argparse.ArgumentParser();
    parser.add_argument("file_path", help="Path to the file")
    args = parser.parse_args()
    file_path = args.file_path

    # Load csv into data frame
    data_frame = pd.read_csv(file_path)

    print(f'Imported data: \n {data_frame} \n\n')

    # Parse column names
    column_names = data_frame.columns.tolist()
    new_column_names = []
    for column_name in column_names:
        # Remove leading and trailing spaces
        column_name = column_name.strip()
        # Make all names lowercase
        column_name = column_name.lower()
        # Replace spaces with underscores
        column_name = column_name.replace(" ", "_")
        # Replace special characters with underscores
        column_name = re.sub(r'\W', '_', column_name)

        new_column_names.append(column_name)

    data_frame.columns = new_column_names

    # Convert date strings to datetime
    data_frame['join_date'] = pd.to_datetime(data_frame['join_date'], format="mixed")


    # Convert all names to title case
    data_frame['name'] = data_frame['name'].apply(lambda x: x.title() if isinstance(x, str) else x)


    # Fill empty values
    data_frame.fillna({'name': 'N/A', 'age': 0}, inplace=True)
    placeholder_date = pd.to_datetime('1901-01-01')
    data_frame.fillna({'join_date': placeholder_date}, inplace=True)

    # Group rows that have the same name, age, and join_date; keep all email addresses
    data_frame = data_frame.groupby(['name', 'age', 'join_date'], as_index = False).agg({
        'email': 'first'
    })

    print(f'Cleaned data: \n {data_frame}\n')

    # Export cleaned data frame to csv
    data_frame.to_csv("cleaned-data.csv", index=False)

if __name__ == "__main__":
    main()