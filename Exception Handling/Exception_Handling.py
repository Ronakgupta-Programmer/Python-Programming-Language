import logging

# Configure logging
logging.basicConfig(filename='error_log.txt', level=logging.ERROR)

class CustomError(Exception):
    """Custom exception for specific validation errors."""
    pass

def handle_zero_division():
    """Demonstrate ZeroDivisionError."""
    try:
        numerator = float(input("Enter numerator: "))
        denominator = float(input("Enter denominator: "))
        result = numerator / denominator
        print(f"Result: {result}")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        logging.error("Attempted to divide by zero.")

def handle_value_error():
    """Demonstrate ValueError."""
    try:
        age = int(input("Enter your age: "))
        if age < 0:
            raise CustomError("Age cannot be negative.")
        print(f"Your age is {age}.")
    except ValueError:
        print("Error: Please enter a valid integer for age.")
        logging.error("Invalid age input.")
    except CustomError as ce:
        print(f"Error: {ce}")
        logging.error(f"Custom error: {ce}")

def handle_file_not_found():
    """Demonstrate FileNotFoundError."""
    try:
        with open("sample.txt", "r") as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("Error: File not found.")
        logging.error("Attempted to read a non-existent file.")

def handle_type_error():
    """Demonstrate TypeError."""
    try:
        result = '1' + 2  # This will raise a TypeError
    except TypeError:
        print("Error: Cannot add string and integer.")
        logging.error("TypeError: Attempted to add string and integer.")

def main():
    while True:
        print("\nSelect an error to demonstrate handling:")
        print("1. ZeroDivisionError")
        print("2. ValueError")
        print("3. FileNotFoundError")
        print("4. TypeError")
        print("0. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '0':
            print("Exiting the program.")
            break
        elif choice == '1':
            handle_zero_division()
        elif choice == '2':
            handle_value_error()
        elif choice == '3':
            handle_file_not_found()
        elif choice == '4':
            handle_type_error()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()