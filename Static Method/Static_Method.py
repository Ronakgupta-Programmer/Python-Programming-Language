class StaticExamples:
    # Static variables (class variables)
    counter = 0
    settings = {}

    @staticmethod
    def increment_counter():
        """Increment the static counter variable."""
        StaticExamples.counter += 1
        print(f"Counter incremented: {StaticExamples.counter}")

    @staticmethod
    def reset_counter():
        """Reset the static counter variable to zero."""
        StaticExamples.counter = 0
        print("Counter reset to 0.")

    @staticmethod
    def display_counter():
        """Display the current value of the static counter."""
        print(f"Current Counter Value: {StaticExamples.counter}")

    @staticmethod
    def add(a, b):
        """Static method to add two numbers."""
        return a + b

    @staticmethod
    def multiply(a, b):
        """Static method to multiply two numbers."""
        return a * b

    @staticmethod
    def create_file(filename):
        """Create a simple text file."""
        with open(filename, 'w') as f:
            f.write("This is a static file.")
        print(f"File '{filename}' created.")

    @staticmethod
    def read_file(filename):
        """Read and display the content of a file."""
        try:
            with open(filename, 'r') as f:
                print(f"Contents of '{filename}':\n{f.read()}")
        except FileNotFoundError:
            print(f"File '{filename}' does not exist.")

    @staticmethod
    def get_setting(key):
        """Get a setting from the static settings dictionary."""
        return StaticExamples.settings.get(key, None)

    @staticmethod
    def set_setting(key, value):
        """Set a setting in the static settings dictionary."""
        StaticExamples.settings[key] = value
        print(f"Setting '{key}' updated to '{value}'.")

    @staticmethod
    def list_settings():
        """List all settings in the static settings dictionary."""
        print("Current Settings:")
        for key, value in StaticExamples.settings.items():
            print(f"{key}: {value}")

    @staticmethod
    def clear_settings():
        """Clear all settings in the static settings dictionary."""
        StaticExamples.settings.clear()
        print("All settings cleared.")

    @staticmethod
    def static_greeting(name):
        """Static method that returns a greeting message."""
        return f"Hello, {name}! Welcome to Static Examples."

    @staticmethod
    def reverse_string(s):
        """Return the reverse of a given string."""
        return s[::-1]

    @staticmethod
    def calculate_factorial(n):
        """Calculate the factorial of a number."""
        if n < 0:
            return "Factorial not defined for negative numbers."
        factorial = 1
        for i in range(1, n + 1):
            factorial *= i
        return factorial

    @staticmethod
    def is_palindrome(s):
        """Check if a given string is a palindrome."""
        return s == s[::-1]

    @staticmethod
    def power(base, exponent):
        """Calculate the power of a number."""
        return base ** exponent

    @staticmethod
    def generate_primes(n):
        """Generate a list of prime numbers up to n."""
        primes = []
        for num in range(2, n + 1):
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    break
            else:
                primes.append(num)
        return primes

    @staticmethod
    def find_max(numbers):
        """Find the maximum number in a list."""
        return max(numbers)

def main():
    while True:
        print("\nChoose an option:")
        print("1. Increment Counter")
        print("2. Reset Counter")
        print("3. Display Counter")
        print("4. Add Two Numbers")
        print("5. Multiply Two Numbers")
        print("6. Create a File")
        print("7. Read a File")
        print("8. Get a Setting")
        print("9. Set a Setting")
        print("10. List All Settings")
        print("11. Clear All Settings")
        print("12. Greet User")
        print("13. Reverse a String")
        print("14. Calculate Factorial")
        print("15. Check Palindrome")
        print("16. Calculate Power")
        print("17. Generate Prime Numbers")
        print("18. Find Maximum in List")
        print("19. Exit")

        choice = input("Enter your choice (1-19): ")

        if choice == '1':
            StaticExamples.increment_counter()
        elif choice == '2':
            StaticExamples.reset_counter()
        elif choice == '3':
            StaticExamples.display_counter()
        elif choice == '4':
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            result = StaticExamples.add(a, b)
            print(f"Result of addition: {result}")
        elif choice == '5':
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            result = StaticExamples.multiply(a, b)
            print(f"Result of multiplication: {result}")
        elif choice == '6':
            filename = input("Enter filename to create: ")
            StaticExamples.create_file(filename)
        elif choice == '7':
            filename = input("Enter filename to read: ")
            StaticExamples.read_file(filename)
        elif choice == '8':
            key = input("Enter setting key to get: ")
            value = StaticExamples.get_setting(key)
            print(f"Setting '{key}': {value}")
        elif choice == '9':
            key = input("Enter setting key to set: ")
            value = input("Enter value: ")
            StaticExamples.set_setting(key, value)
        elif choice == '10':
            StaticExamples.list_settings()
        elif choice == '11':
            StaticExamples.clear_settings()
        elif choice == '12':
            name = input("Enter your name: ")
            greeting = StaticExamples.static_greeting(name)
            print(greeting)
        elif choice == '13':
            string_input = input("Enter a string to reverse: ")
            reversed_string = StaticExamples.reverse_string(string_input)
            print(f"Reversed String: {reversed_string}")
        elif choice == '14':
            n = int(input("Enter a number to calculate factorial: "))
            factorial = StaticExamples.calculate_factorial(n)
            print(f"Factorial of {n}: {factorial}")
        elif choice == '15':
            string_input = input("Enter a string to check for palindrome: ")
            if StaticExamples.is_palindrome(string_input):
                print(f"{string_input} is a palindrome.")
            else:
                print(f"{string_input} is not a palindrome.")
        elif choice == '16':
            base = int(input("Enter base: "))
            exponent = int(input("Enter exponent: "))
            result = StaticExamples.power(base, exponent)
            print(f"{base} to the power of {exponent} is {result}.")
        elif choice == '17':
            n = int(input("Generate prime numbers up to: "))
            primes = StaticExamples.generate_primes(n)
            print(f"Prime numbers up to {n}: {primes}")
        elif choice == '18':
            numbers = list(map(int, input("Enter a list of numbers separated by space: ").split()))
            max_number = StaticExamples.find_max(numbers)
            print(f"The maximum number in the list is: {max_number}")
        elif choice == '19':
            print("Exiting program..")
            break
        else:
            print("Invalid choice! Please choose a number between 1 and 19.")

if __name__ == "__main__":
    main()