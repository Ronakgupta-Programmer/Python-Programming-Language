def divide(a, b):
    assert isinstance(a, (int, float)), "Numerator must be a number."
    assert isinstance(b, (int, float)), "Denominator must be a number."
    assert b != 0, "Denominator must not be zero."
    return a / b

def calculate_average(numbers):
    assert isinstance(numbers, list), "Input must be a list."
    assert len(numbers) > 0, "The list must not be empty."
    assert all(isinstance(n, (int, float)) for n in numbers), "All elements must be numbers."
    return sum(numbers) / len(numbers)

def check_coordinates(x, y):
    assert isinstance(x, (int, float)), "x must be a number."
    assert isinstance(y, (int, float)), "y must be a number."
    assert -100 <= x <= 100, "x must be between -100 and 100."
    assert -100 <= y <= 100, "y must be between -100 and 100."
    return (x, y)

def check_palindrome(s):
    assert isinstance(s, str), "Input must be a string."
    assert len(s) > 0, "String must not be empty."
    return s == s[::-1]

def factorial(n):
    assert isinstance(n, int), "Input must be an integer."
    assert n >= 0, "Number must be non-negative."
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

class BankAccount:
    MAX_DEPOSIT = 10000  # Maximum deposit amount
    MAX_WITHDRAWAL = 5000  # Maximum withdrawal amount

    def __init__(self, balance):
        assert isinstance(balance, (int, float)), "Initial balance must be a number."
        assert balance >= 0, "Initial balance must be non-negative."
        self.balance = balance

    def withdraw(self, amount):
        assert isinstance(amount, (int, float)), "Withdrawal amount must be a number."
        assert amount > 0, "Withdrawal amount must be positive."
        assert amount <= self.balance, "Insufficient funds."
        assert amount <= self.MAX_WITHDRAWAL, f"Withdrawal amount must not exceed {self.MAX_WITHDRAWAL}."
        self.balance -= amount

    def deposit(self, amount):
        assert isinstance(amount, (int, float)), "Deposit amount must be a number."
        assert amount > 0, "Deposit amount must be positive."
        assert amount <= self.MAX_DEPOSIT, f"Deposit amount must not exceed {self.MAX_DEPOSIT}."
        self.balance += amount

    def get_balance(self):
        assert self.balance >= 0, "Balance must be non-negative."
        return self.balance

def check_iterable(obj):
    assert hasattr(obj, '__iter__'), "Object must be iterable."
    assert len(obj) > 0, "Iterable must not be empty."
    return True

def check_positive_integer(n):
    assert isinstance(n, int), "Input must be an integer."
    assert n > 0, "Number must be a positive integer."
    return True

def check_even(n):
    assert isinstance(n, int), "Input must be an integer."
    assert n % 2 == 0, "Number must be even."
    return True

def check_odd(n):
    assert isinstance(n, int), "Input must be an integer."
    assert n % 2 != 0, "Number must be odd."
    return True

def validate_email(email):
    assert isinstance(email, str), "Email must be a string."
    assert "@" in email and "." in email, "Invalid email format."
    return True

def validate_string_length(s, min_length):
    assert isinstance(s, str), "Input must be a string."
    assert len(s) >= min_length, f"String must be at least {min_length} characters long."
    return True

def validate_dict_keys(d, required_keys):
    assert isinstance(d, dict), "Input must be a dictionary."
    assert all(isinstance(key, str) for key in required_keys), "Required keys must be strings."
    assert all(key in d for key in required_keys), f"Missing keys: {set(required_keys) - set(d.keys())}."
    return True

def main():
    while True:
        print("\nSelect an option:")
        print("1.  Calculate the average of a list")
        print("2.  Check if a number is even")
        print("3.  Check if a number is odd")
        print("4.  Divide two numbers")
        print("5.  Check coordinates")
        print("6.  Bank account operations")
        print("7.  Validate email")
        print("8.  Validate string length")
        print("9.  Validate dictionary keys")
        print("10. Check if a string is a palindrome")
        print("11. Calculate factorial of a number")
        print("12. Exit")

        choice = input("Enter your choice (1-12): ")

        if choice == '1':
            numbers = input("Enter numbers separated by commas: ")
            number_list = [float(num) for num in numbers.split(',')]
            try:
                avg = calculate_average(number_list)
                print(f"The average is: {avg}")
            except AssertionError as e:
                print("Error:", e)

        elif choice == '2':
            number = int(input("Enter a number: "))
            try:
                check_even(number)
                print(f"{number} is even.")
            except AssertionError as e:
                print("Error:", e)

        elif choice == '3':
            number = int(input("Enter a number: "))
            try:
                check_odd(number)
                print(f"{number} is odd.")
            except AssertionError as e:
                print("Error:", e)

        elif choice == '4':
            try:
                a = float(input("Enter the numerator: "))
                b = float(input("Enter the denominator: "))
                result = divide(a, b)
                print(f"The result of {a} divided by {b} is: {result}")
            except AssertionError as e:
                print("Error:", e)

        elif choice == '5':
            try:
                x = float(input("Enter x-coordinate: "))
                y = float(input("Enter y-coordinate: "))
                coords = check_coordinates(x, y)
                print(f"Coordinates are valid: {coords}")
            except AssertionError as e:
                print("Error:", e)

        elif choice == '6':
            account = BankAccount(100)  # Example balance
            while True:
                print("\nBank Account Operations:")
                print("1. Deposit")
                print("2. Withdraw")
                print("3. Check Balance")
                print("4. Exit to main menu")
                
                account_choice = input("Enter your choice (1-4): ")
                
                if account_choice == '1':
                    amount = float(input("Enter deposit amount: "))
                    try:
                        account.deposit(amount)
                        print(f"Deposited: {amount}, New Balance: {account.get_balance()}")
                    except AssertionError as e:
                        print("Error:", e)

                elif account_choice == '2':
                    amount = float(input("Enter withdrawal amount: "))
                    try:
                        account.withdraw(amount)
                        print(f"Withdrew: {amount}, New Balance: {account.get_balance()}")
                    except AssertionError as e:
                        print("Error:", e)

                elif account_choice == '3':
                    print(f"Current Balance: {account.get_balance()}")

                elif account_choice == '4':
                    break

                else:
                    print("Invalid choice. Please select 1-4.")

        elif choice == '7':
            email = input("Enter email to validate: ")
            try:
                validate_email(email)
                print("Email is valid.")
            except AssertionError as e:
                print("Error:", e)

        elif choice == '8':
            string = input("Enter a string: ")
            min_length = int(input("Enter minimum length: "))
            try:
                validate_string_length(string, min_length)
                print("String length is valid.")
            except AssertionError as e:
                print("Error:", e)

        elif choice == '9':
            dictionary = input("Enter a dictionary (e.g., {'key': 'value'}): ")
            required_keys = input("Enter required keys separated by commas: ").split(',')
            try:
                validate_dict_keys(eval(dictionary), [key.strip() for key in required_keys])
                print("Dictionary keys are valid.")
            except AssertionError as e:
                print("Error:", e)

        elif choice == '10':
            string = input("Enter a string to check for palindrome: ")
            try:
                if check_palindrome(string):
                    print(f"{string} is a palindrome.")
                else:
                    print(f"{string} is not a palindrome.")
            except AssertionError as e:
                print("Error:", e)

        elif choice == '11':
            n = int(input("Enter a non-negative integer: "))
            try:
                result = factorial(n)
                print(f"The factorial of {n} is: {result}")
            except AssertionError as e:
                print("Error:", e)

        elif choice == '12':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()