import pandas as pd
import argparse

def main():
    # Set up parser
    parser = argparse.ArgumentParser();
    parser.add_argument("file_path", Help="Path to the file")
    args = parser.parse_args()
    file_path = args.file_path

    # Load csv into data frame
    data_frame = pd.read_csv(file_path)


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

    # Export cleaned data frame to csv
    data_frame.to_csv("cleaned-data.csv")

if __name__ == "__main__":
    main()