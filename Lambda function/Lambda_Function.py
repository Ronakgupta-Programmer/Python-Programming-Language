from functools import reduce

def main():
    print("=== Lambda Functions Demo ===\n")

    while True:
        print("Choose an operation to perform using lambda functions:")
        print("1. Add numbers")
        print("2. Filter even numbers")
        print("3. Square numbers")
        print("4. Sum of numbers")
        print("5. Sort names by length")
        print("6. Concatenate two strings")
        print("7. Check if positive")
        print("8. List cubes of numbers")
        print("9. Increment a number")
        print("0. Exit")
        
        choice = input("Enter your choice (0-9): ")

        if choice == '0':
            print("Exiting the program.")
            break
        
        if choice == '1':
            # Add numbers
            numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
            add = lambda x, y: x + y
            result = reduce(add, numbers)
            print(f"Sum of numbers: {result}\n")

        elif choice == '2':
            # Filter even numbers
            numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
            even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
            print(f"Even Numbers: {even_numbers}\n")

        elif choice == '3':
            # Square numbers
            numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
            squared_numbers = list(map(lambda x: x ** 2, numbers))
            print(f"Squared Numbers: {squared_numbers}\n")

        elif choice == '4':
            # Sum of numbers
            numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
            sum_of_numbers = reduce(lambda x, y: x + y, numbers)
            print(f"Sum: {sum_of_numbers}\n")

        elif choice == '5':
            # Sort names by length
            names = input("Enter names separated by spaces: ").split()
            sorted_names = sorted(names, key=lambda x: len(x))
            print(f"Sorted Names: {sorted_names}\n")

        elif choice == '6':
            # Concatenate two strings
            str1 = input("Enter the first string: ")
            str2 = input("Enter the second string: ")
            concat = lambda x, y: x + " " + y
            result = concat(str1, str2)
            print(f"Concatenated: {result}\n")

        elif choice == '7':
            # Check if positive
            numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
            check_positive = lambda x: "Positive" if x > 0 else "Non-Positive"
            for num in numbers:
                print(f"Check {num}: {check_positive(num)}")
            print()

        elif choice == '8':
            # List cubes of numbers
            numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
            cubes = [(lambda x: x ** 3)(x) for x in numbers]
            print(f"Cubes: {cubes}\n")

        elif choice == '9':
            # Increment a number
            n = int(input("Enter the number to increment: "))
            increment_by = int(input("Enter how much to increment by: "))
            increment = lambda x: x + increment_by
            print(f"Incremented number: {increment(n)}\n")

        else:
            print("Invalid choice, please try again.\n")

if __name__ == "__main__":
    main()