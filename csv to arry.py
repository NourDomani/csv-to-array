import csv

def extract_column_h(csv_file):
    # Open the CSV file
    with open(csv_file, 'r') as file:
        # Create a CSV reader
        reader = csv.reader(file)

        # Skip the header row
        next(reader)

        # Initialize an empty list to store column H data
        column_h_data = []

        # Iterate over each row in the CSV file
        for row in reader:
            try:
                # Extract the value from column H and append it to the list
                column_h_data.append(row[7])  # Assuming column H is the 8th column (0-based index)
            except IndexError:
                # Handle cases where the row doesn't have enough columns
                pass

    return column_h_data

def main():
    # Input CSV file path
    csv_file = "C:/images/sample1.csv"

    # Extract column H data
    column_h_data = extract_column_h(csv_file)

    # Print the column H data
    print("Column H data:")
    print(column_h_data)

if __name__ == "__main__":
    main()
