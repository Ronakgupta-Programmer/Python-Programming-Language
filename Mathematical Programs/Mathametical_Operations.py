import math
from collections import Counter

def fibonacci(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_fib)
    return fib_sequence[:n]

def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

def modulus(a, b):
    return a % b

def exponentiate(base, exp):
    return base ** exp

def square_root(n):
    if n < 0:
        raise ValueError("Square root is not defined for negative numbers.")
    return math.sqrt(n)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def gcd(a, b):
    while b:
        a, b = b, a % b
    return abs(a)

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

def logarithm(base, value):
    if base <= 0 or base == 1 or value <= 0:
        raise ValueError("Logarithm is undefined for this input.")
    return math.log(value, base)

def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0

def mean(numbers):
    return sum(numbers) / len(numbers)

def geometric_mean(numbers):
    product = 1
    for num in numbers:
        product *= num
    return product ** (1 / len(numbers))

def median(numbers):
    sorted_numbers = sorted(numbers)
    mid = len(sorted_numbers) // 2
    if len(sorted_numbers) % 2 == 0:
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    return sorted_numbers[mid]

def mode(numbers):
    count = Counter(numbers)
    modes = [key for key, value in count.items() if value == max(count.values())]
    return modes

def variance(numbers):
    avg = mean(numbers)
    return sum((x - avg) ** 2 for x in numbers) / len(numbers)

def standard_deviation(numbers):
    return math.sqrt(variance(numbers))

def compound_interest(principal, rate, time, frequency):
    return principal * (1 + rate / frequency) ** (frequency * time)

def area_rectangle(length, width):
    return length * width

def perimeter_rectangle(length, width):
    return 2 * (length + width)

def area_circle(radius):
    return math.pi * radius ** 2

def perimeter_circle(radius):
    return 2 * math.pi * radius

def area_triangle(base, height):
    return 0.5 * base * height

def area_trapezoid(base1, base2, height):
    return 0.5 * (base1 + base2) * height

def matrix_addition(matrix_a, matrix_b):
    return [[matrix_a[i][j] + matrix_b[i][j] for j in range(len(matrix_a[0]))] for i in range(len(matrix_a))]

def matrix_multiplication(matrix_a, matrix_b):
    return [[sum(a * b for a, b in zip(row, col)) for col in zip(*matrix_b)] for row in matrix_a]

def quadratic_solver(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        return "No real roots"
    elif discriminant == 0:
        root = -b / (2 * a)
        return (root,)
    else:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return (root1, root2)

def pendulum_period(length):
    g = 9.81
    return 2 * math.pi * math.sqrt(length / g)

def permutations(n, r):
    return factorial(n) // factorial(n - r)

def combinations(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))

def pythagorean_theorem(a, b):
    return math.sqrt(a**2 + b**2)

def surface_area_cylinder(radius, height):
    return 2 * math.pi * radius * (radius + height)

def volume_cylinder(radius, height):
    return math.pi * radius ** 2 * height

def main():
    print("Choose an operation:")
    print("1.  Fibonacci")
    print("2.  Factorial")
    print("3.  Addition")
    print("4.  Subtraction")
    print("5.  Multiplication")
    print("6.  Division")
    print("7.  Modulus")
    print("8.  Exponentiation")
    print("9.  Square Root")
    print("10. Check Prime")
    print("11. GCD")
    print("12. LCM")
    print("13. Logarithm")
    print("14. Check Power of Two")
    print("15. Mean")
    print("16. Geometric Mean")
    print("17. Median")
    print("18. Mode")
    print("19. Variance")
    print("20. Standard Deviation")
    print("21. Compound Interest")
    print("22. Area and Perimeter of Rectangle")
    print("23. Area and Circumference of Circle")
    print("24. Area of Triangle")
    print("25. Area of Trapezoid")
    print("26. Matrix Addition")
    print("27. Matrix Multiplication")
    print("28. Quadratic Equation Solver")
    print("29. Pendulum Period")
    print("30. Permutations")
    print("31. Combinations")
    print("32. Pythagorean Theorem")
    print("33. Surface Area and Volume of Cylinder")

    choice = input("Enter choice (1-33): ")
    
    if choice == '1':
        n = int(input("Enter the number of Fibonacci terms: "))
        print(f"Fibonacci sequence: {fibonacci(n)}")
    
    elif choice == '2':
        n = int(input("Enter a number to compute factorial: "))
        print(f"Factorial of {n}: {factorial(n)}")
    
    elif choice == '3':
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print(f"Sum: {add(a, b)}")
    
    elif choice == '4':
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print(f"Difference: {subtract(a, b)}")
    
    elif choice == '5':
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print(f"Product: {multiply(a, b)}")
    
    elif choice == '6':
        a = float(input("Enter numerator: "))
        b = float(input("Enter denominator: "))
        try:
            print(f"Quotient: {divide(a, b)}")
        except ValueError as e:
            print(e)

    elif choice == '7':
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print(f"{a} % {b} = {modulus(a, b)}")
    
    elif choice == '8':
        base = float(input("Enter base: "))
        exp = float(input("Enter exponent: "))
        print(f"{base} raised to the power of {exp} is: {exponentiate(base, exp)}")
    
    elif choice == '9':
        n = float(input("Enter a number to compute square root: "))
        try:
            print(f"Square root of {n} is: {square_root(n)}")
        except ValueError as e:
            print(e)

    elif choice == '10':
        n = int(input("Enter a number to check if it is prime: "))
        if is_prime(n):
            print(f"{n} is a prime number.")
        else:
            print(f"{n} is not a prime number.")
    
    elif choice == '11':
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print(f"GCD of {a} and {b} is: {gcd(a, b)}")
    
    elif choice == '12':
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print(f"LCM of {a} and {b} is: {lcm(a, b)}")
    
    elif choice == '13':
        base = float(input("Enter base: "))
        value = float(input("Enter value: "))
        try:
            print(f"Logarithm of {value} with base {base} is: {logarithm(base, value)}")
        except ValueError as e:
            print(e)

    elif choice == '14':
        n = int(input("Enter a number to check if it is a power of two: "))
        if is_power_of_two(n):
            print(f"{n} is a power of two.")
        else:
            print(f"{n} is not a power of two.")
    
    elif choice == '15':
        numbers = list(map(float, input("Enter numbers separated by spaces: ").split()))
        print(f"Mean: {mean(numbers)}")
    
    elif choice == '16':
        numbers = list(map(float, input("Enter numbers separated by spaces: ").split()))
        print(f"Geometric Mean: {geometric_mean(numbers)}")
    
    elif choice == '17':
        numbers = list(map(float, input("Enter numbers separated by spaces: ").split()))
        print(f"Median: {median(numbers)}")
    
    elif choice == '18':
        numbers = list(map(float, input("Enter numbers separated by spaces: ").split()))
        print(f"Mode: {mode(numbers)}")
    
    elif choice == '19':
        numbers = list(map(float, input("Enter numbers separated by spaces: ").split()))
        print(f"Variance: {variance(numbers)}")
    
    elif choice == '20':
        numbers = list(map(float, input("Enter numbers separated by spaces: ").split()))
        print(f"Standard Deviation: {standard_deviation(numbers)}")
    
    elif choice == '21':
        principal = float(input("Enter principal amount: "))
        rate = float(input("Enter interest rate (in decimal): "))
        time = float(input("Enter time (in years): "))
        frequency = int(input("Enter the number of times interest is compounded per year: "))
        interest = compound_interest(principal, rate, time, frequency)
        print(f"Compound interest is: {interest}")

    elif choice == '22':
        length = float(input("Enter length of the rectangle: "))
        width = float(input("Enter width of the rectangle: "))
        print(f"Area: {area_rectangle(length, width)}")
        print(f"Perimeter: {perimeter_rectangle(length, width)}")

    elif choice == '23':
        radius = float(input("Enter radius of the circle: "))
        print(f"Area: {area_circle(radius)}")
        print(f"Circumference: {perimeter_circle(radius)}")

    elif choice == '24':
        base = float(input("Enter base of the triangle: "))
        height = float(input("Enter height of the triangle: "))
        print(f"Area: {area_triangle(base, height)}")

    elif choice == '25':
        base1 = float(input("Enter base1 of the trapezoid: "))
        base2 = float(input("Enter base2 of the trapezoid: "))
        height = float(input("Enter height of the trapezoid: "))
        print(f"Area: {area_trapezoid(base1, base2, height)}")

    elif choice == '26':
        rows = int(input("Enter number of rows for the matrices: "))
        print("Enter the first matrix:")
        matrix_a = [list(map(float, input().split())) for _ in range(rows)]
        print("Enter the second matrix:")
        matrix_b = [list(map(float, input().split())) for _ in range(rows)]
        print(f"Result of addition: {matrix_addition(matrix_a, matrix_b)}")

    elif choice == '27':
        rows_a = int(input("Enter number of rows for first matrix: "))
        cols_a = int(input("Enter number of columns for first matrix: "))
        matrix_a = [list(map(float, input().split())) for _ in range(rows_a)]
        
        rows_b = int(input("Enter number of rows for second matrix: "))
        cols_b = int(input("Enter number of columns for second matrix: "))
        matrix_b = [list(map(float, input().split())) for _ in range(rows_b)]
        
        if cols_a != rows_b:
            print("Matrix multiplication is not possible.")
        else:
            print(f"Result of multiplication: {matrix_multiplication(matrix_a, matrix_b)}")

    elif choice == '28':
        a = float(input("Enter coefficient a: "))
        b = float(input("Enter coefficient b: "))
        c = float(input("Enter coefficient c: "))
        roots = quadratic_solver(a, b, c)
        print(f"Roots: {roots}")

    elif choice == '29':
        length = float(input("Enter length of the pendulum (in meters): "))
        print(f"Period of the pendulum: {pendulum_period(length)} seconds")

    elif choice == '30':
        n = int(input("Enter total items (n): "))
        r = int(input("Enter selected items (r): "))
        print(f"Permutations: {permutations(n, r)}")

    elif choice == '31':
        n = int(input("Enter total items (n): "))
        r = int(input("Enter selected items (r): "))
        print(f"Combinations: {combinations(n, r)}")

    elif choice == '32':
        a = float(input("Enter length of side a: "))
        b = float(input("Enter length of side b: "))
        hypotenuse = pythagorean_theorem(a, b)
        print(f"Hypotenuse: {hypotenuse}")

    elif choice == '33':
        radius = float(input("Enter radius of the cylinder: "))
        height = float(input("Enter height of the cylinder: "))
        surface_area = surface_area_cylinder(radius, height)
        volume = volume_cylinder(radius, height)
        print(f"Surface Area: {surface_area}")
        print(f"Volume: {volume}")

    else:
        print("Invalid choice. Please select a number between 1 and 33.")

if __name__ == "__main__":
    main()