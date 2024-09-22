import csv
import pandas as pd
import shutil
import os

def read_csv(file_path):
    """Read and display CSV file content."""
    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

def write_csv(file_path, data):
    """Write data to a new CSV file."""
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

def update_csv(file_path, old_value, new_value):
    """Update records in a CSV file."""
    with open(file_path, mode='r') as file:
        rows = list(csv.reader(file))
    
    for row in rows:
        if old_value in row:
            row[row.index(old_value)] = new_value

    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)

def delete_record(file_path, value):
    """Delete a record from the CSV file."""
    with open(file_path, mode='r') as file:
        rows = list(csv.reader(file))
    
    rows = [row for row in rows if value not in row]

    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)

def search_record(file_path, search_value):
    """Search for records containing a specific value."""
    with open(file_path, mode='r') as file:
        rows = list(csv.reader(file))
    
    results = [row for row in rows if search_value in row]
    
    if results:
        print("Search Results:")
        for row in results:
            print(row)
    else:
        print("No records found.")

def count_records(file_path):
    """Count the number of records in the CSV file."""
    with open(file_path, mode='r') as file:
        rows = list(csv.reader(file))
    
    print(f"Total records: {len(rows) - 1} (excluding header)")

def sort_records(file_path, column_index):
    """Sort records based on a specific column."""
    with open(file_path, mode='r') as file:
        rows = list(csv.reader(file))

    header = rows[0]
    sorted_rows = sorted(rows[1:], key=lambda x: x[column_index])
    sorted_rows.insert(0, header)

    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(sorted_rows)
    
    print("Records sorted successfully.")

def add_column(file_path, column_name, default_value):
    """Add a new column to the CSV file with default values."""
    with open(file_path, mode='r') as file:
        rows = list(csv.reader(file))
    
    rows[0].append(column_name)  # Add new column header
    for row in rows[1:]:
        row.append(default_value)  # Append default value

    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)
    
    print(f"Column '{column_name}' added successfully.")

def delete_column(file_path, column_index):
    """Delete a specified column from the CSV file."""
    with open(file_path, mode='r') as file:
        rows = list(csv.reader(file))

    for row in rows:
        del row[column_index]

    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)

    print("Column deleted successfully.")

def unique_values(file_path, column_index):
    """Find unique values in a specified column."""
    with open(file_path, mode='r') as file:
        rows = list(csv.reader(file))

    values = set(row[column_index] for row in rows[1:])
    print(f"Unique values in column {column_index}: {values}")

def group_by(file_path, column_index):
    """Group records by a specified column and count occurrences."""
    df = pd.read_csv(file_path)
    grouped = df.groupby(df.columns[column_index]).size()
    print(grouped)

def backup_csv(file_path):
    """Create a backup of the CSV file."""
    backup_path = f"{file_path}.bak"
    shutil.copyfile(file_path, backup_path)
    print(f"Backup created at {backup_path}")

def analyze_csv(file_path):
    """Perform data analysis using pandas."""
    df = pd.read_csv(file_path)
    print(df.describe())

def main():
    while True:
        print("\nCSV File Management Menu:")
        print("1.  Read CSV - Display the contents of a CSV file.")
        print("2.  Write CSV - Create a new CSV file with sample data.")
        print("3.  Update CSV - Update records in a CSV file.")
        print("4.  Delete Record - Remove a specific record from a CSV file.")
        print("5.  Search Record - Search for records containing a specific value.")
        print("6.  Count Records - Count the total number of records in a CSV file.")
        print("7.  Sort Records - Sort records based on a specific column.")
        print("8.  Add Column - Add a new column with default values.")
        print("9.  Delete Column - Remove a specified column from a CSV file.")
        print("10. Unique Values - Find unique values in a specified column.")
        print("11. Group By - Group records by a specified column and count occurrences.")
        print("12. Backup CSV - Create a backup of the CSV file.")
        print("13. Analyze CSV - Perform data analysis on the CSV file.")
        print("14. Exit - Exit the program.")
        
        choice = input("Select an option: ")
        
        if choice == '1':
            file_path = input("Enter CSV file path: ")
            read_csv(file_path)
        elif choice == '2':
            file_path = input("Enter CSV file path: ")
            data = [["Name", "Age"], ["Alice", 30], ["Bob", 25]]
            write_csv(file_path, data)
        elif choice == '3':
            file_path = input("Enter CSV file path: ")
            old_value = input("Enter the old value to update: ")
            new_value = input("Enter the new value: ")
            update_csv(file_path, old_value, new_value)
        elif choice == '4':
            file_path = input("Enter CSV file path: ")
            value = input("Enter the value to delete: ")
            delete_record(file_path, value)
        elif choice == '5':
            file_path = input("Enter CSV file path: ")
            search_value = input("Enter the value to search: ")
            search_record(file_path, search_value)
        elif choice == '6':
            file_path = input("Enter CSV file path: ")
            count_records(file_path)
        elif choice == '7':
            file_path = input("Enter CSV file path: ")
            column_index = int(input("Enter the column index to sort (0 for first column): "))
            sort_records(file_path, column_index)
        elif choice == '8':
            file_path = input("Enter CSV file path: ")
            column_name = input("Enter the new column name: ")
            default_value = input("Enter the default value: ")
            add_column(file_path, column_name, default_value)
        elif choice == '9':
            file_path = input("Enter CSV file path: ")
            column_index = int(input("Enter the column index to delete (0 for first column): "))
            delete_column(file_path, column_index)
        elif choice == '10':
            file_path = input("Enter CSV file path: ")
            column_index = int(input("Enter the column index to find unique values (0 for first column): "))
            unique_values(file_path, column_index)
        elif choice == '11':
            file_path = input("Enter CSV file path: ")
            column_index = int(input("Enter the column index to group by (0 for first column): "))
            group_by(file_path, column_index)
        elif choice == '12':
            file_path = input("Enter CSV file path: ")
            backup_csv(file_path)
        elif choice == '13':
            file_path = input("Enter CSV file path: ")
            analyze_csv(file_path)
        elif choice == '14':
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()