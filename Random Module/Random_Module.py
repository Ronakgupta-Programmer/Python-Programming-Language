import random
import string
import datetime

def random_integer():
    a = int(input("Enter the minimum value: "))
    b = int(input("Enter the maximum value: "))
    print(f"Random Integer between {a} and {b}: {random.randint(a, b)}")

def random_float_0_to_1():
    print("Random Float between 0 and 1:", random.random())

def random_float_range():
    a = float(input("Enter the minimum value: "))
    b = float(input("Enter the maximum value: "))
    print(f"Random Float between {a} and {b}: {random.uniform(a, b)}")

def random_choice_from_list():
    sample_list = input("Enter a list of items separated by commas: ").split(',')
    print("Random choice from list:", random.choice(sample_list))

def random_sample_from_list():
    sample_list = input("Enter a list of items separated by commas: ").split(',')
    k = int(input("Enter number of samples to select: "))
    print("Random sample from list:", random.sample(sample_list, k))

def shuffle_list():
    sample_list = input("Enter a list of items separated by commas: ").split(',')
    random.shuffle(sample_list)
    print("Shuffled list:", sample_list)

def random_range_step():
    a = int(input("Enter the start value: "))
    b = int(input("Enter the stop value: "))
    step = int(input("Enter the step value: "))
    print(f"Random range (step {step}) from {a} to {b}:", random.randrange(a, b, step))

def random_character_from_string():
    print("Randomly selected character from string:", random.choice("abcdefghijklmnopqrstuvwxyz"))

def random_with_seed():
    seed = int(input("Enter a seed value: "))
    random.seed(seed)  # Setting a seed for reproducibility
    print("Random integer with seed", seed, "(1-100):", random.randint(1, 100))

def random_float_specific_range():
    a = float(input("Enter the minimum value: "))
    b = float(input("Enter the maximum value: "))
    print(f"Random float between {a} and {b}:", random.uniform(a, b))

def random_multiple_floats():
    count = int(input("Enter the number of random floats to generate: "))
    random_floats = [random.uniform(1, 10) for _ in range(count)]
    print("List of random floats between 1 and 10:", random_floats)

def random_normal_distribution():
    mu = float(input("Enter mean (mu): "))
    sigma = float(input("Enter standard deviation (sigma): "))
    print(f"Random number from normal distribution (mean={mu}, sigma={sigma}):", random.gauss(mu, sigma))

def random_int_choice():
    a = int(input("Enter the minimum value: "))
    b = int(input("Enter the maximum value: "))
    print(f"Random integer chosen from range [{a}, {b}]:", random.randint(a, b))

def random_weighted_choice():
    items = input("Enter items separated by commas: ").split(',')
    weights = list(map(int, input("Enter weights for these items separated by commas: ").split(',')))
    print("Weighted random choice:", random.choices(items, weights=weights, k=1)[0])

def random_string(length):
    letters = string.ascii_letters  # Includes both uppercase and lowercase
    return ''.join(random.choice(letters) for i in range(length))

def random_unique_sample():
    sample_list = input("Enter a list of items separated by commas: ").split(',')
    k = int(input("Enter number of unique samples to select: "))
    if k > len(sample_list):
        print("Sample size must be less than or equal to the list size.")
    else:
        print("Unique random sample from list:", random.sample(sample_list, k))

def random_date():
    start_date = datetime.date(2000, 1, 1)
    end_date = datetime.date(2024, 12, 31)
    time_between = end_date - start_date
    days_between = time_between.days
    random_number_of_days = random.randint(0, days_between)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)
    print("Random date between 2000-01-01 and 2024-12-31:", random_date)

def random_demo():
    while True:
        print("\nChoose a random function:")
        print("1. Random Integer")
        print("2. Random Float (0 to 1)")
        print("3. Random Float (in range)")
        print("4. Random Choice from List")
        print("5. Random Sample from List")
        print("6. Shuffle List")
        print("7. Random Range with Step")
        print("8. Random Character from String")
        print("9. Random with Seed")
        print("10. Random Float (specific range)")
        print("11. Random Multiple Floats")
        print("12. Random Normal Distribution")
        print("13. Random Integer Choice")
        print("14. Random Weighted Choice")
        print("15. Random String")
        print("16. Random Unique Sample")
        print("17. Random Date")
        print("18. Exit")

        choice = input("Enter your choice (1-18): ")
        
        if choice == '1':
            random_integer()
        elif choice == '2':
            random_float_0_to_1()
        elif choice == '3':
            random_float_range()
        elif choice == '4':
            random_choice_from_list()
        elif choice == '5':
            random_sample_from_list()
        elif choice == '6':
            shuffle_list()
        elif choice == '7':
            random_range_step()
        elif choice == '8':
            random_character_from_string()
        elif choice == '9':
            random_with_seed()
        elif choice == '10':
            random_float_specific_range()
        elif choice == '11':
            random_multiple_floats()
        elif choice == '12':
            random_normal_distribution()
        elif choice == '13':
            random_int_choice()
        elif choice == '14':
            random_weighted_choice()
        elif choice == '15':
            length = int(input("Enter the length of the random string: "))
            print("Random String:", random_string(length))
        elif choice == '16':
            random_unique_sample()
        elif choice == '17':
            random_date()
        elif choice == '18':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    random_demo()