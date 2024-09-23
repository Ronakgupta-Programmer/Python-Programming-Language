import array as arr
import random

def display_array(array):
    print("Array elements:", array)

def save_array_to_file(array):
    filename = input("Enter the filename (e.g., array.txt): ")
    with open(filename, 'w') as file:
        for item in array:
            file.write(f"{item}\n")
    print(f"Array saved to '{filename}'.")

def load_array_from_file():
    filename = input("Enter the filename (e.g., array.txt): ")
    try:
        with open(filename, 'r') as file:
            loaded_array = arr.array('i', [int(line.strip()) for line in file])
        print(f"Array loaded from '{filename}':")
        display_array(loaded_array)
        return loaded_array
    except FileNotFoundError:
        print("File not found! Please enter a valid filename.")
        return arr.array('i', [])

def main():
    my_array = arr.array('i', [])
    
    while True:
        print("\nMenu:")
        print("1.  Add elements to the array")
        print("2.  Display the array")
        print("3.  Modify an element")
        print("4.  Remove an element")
        print("5.  Slice the array")
        print("6.  Find an element")
        print("7.  Count occurrences of an element")
        print("8.  Sort the array")
        print("9.  Reverse the array")
        print("10. Clear the array")
        print("11. Copy the array")
        print("12. Find max and min values")
        print("13. Calculate sum and average")
        print("14. Remove duplicates")
        print("15. Shuffle the array")
        print("16. Save to file")
        print("17. Load from file")
        print("18. Exit")
        
        choice = int(input("Please enter your choice (1-18): "))
        
        if choice == 1:
            n = int(input("How many elements do you want to add? "))
            for i in range(n):
                element = int(input(f"Enter element {i + 1}: "))
                my_array.append(element)
        
        elif choice == 2:
            display_array(my_array)
        
        elif choice == 3:
            index_to_modify = int(input("Which index do you want to modify? "))
            new_value = int(input("Enter new value: "))
            if 0 <= index_to_modify < len(my_array):
                my_array[index_to_modify] = new_value
                print("Modified Array:")
                display_array(my_array)
            else:
                print("Invalid index!")
        
        elif choice == 4:
            value_to_remove = int(input("Which value do you want to remove? "))
            if value_to_remove in my_array:
                my_array.remove(value_to_remove)
                print("Array after removing:")
                display_array(my_array)
            else:
                print("Value not found in the array!")

        elif choice == 5:
            start_index = int(input("Enter start index for slicing: "))
            end_index = int(input("Enter end index for slicing: "))
            print("Sliced Array:", my_array[start_index:end_index])

        elif choice == 6:
            value_to_find = int(input("Which value do you want to find? "))
            if value_to_find in my_array:
                print(f"{value_to_find} is present in the array.")
            else:
                print(f"{value_to_find} is not found in the array.")

        elif choice == 7:
            value_to_count = int(input("Which value do you want to count? "))
            count = my_array.count(value_to_count)
            print(f"Count of {value_to_count}: {count}")

        elif choice == 8:
            my_array = arr.array('i', sorted(my_array))
            print("Sorted Array:")
            display_array(my_array)

        elif choice == 9:
            my_array.reverse()
            print("Reversed Array:")
            display_array(my_array)

        elif choice == 10:
            my_array = arr.array('i', [])
            print("Array has been cleared.")

        elif choice == 11:
            copied_array = arr.array('i', my_array)
            print("Copy of the array:")
            display_array(copied_array)

        elif choice == 12:
            if my_array:
                max_value = max(my_array)
                min_value = min(my_array)
                print(f"Maximum Value: {max_value}")
                print(f"Minimum Value: {min_value}")
            else:
                print("Array is empty!")

        elif choice == 13:
            if my_array:
                total = sum(my_array)
                average = total / len(my_array)
                print(f"Total of array: {total}, Average: {average}")
            else:
                print("Array is empty!")

        elif choice == 14:
            unique_array = arr.array('i', set(my_array))
            my_array = unique_array
            print("Duplicates removed. Updated Array:")
            display_array(my_array)

        elif choice == 15:
            random.shuffle(my_array)
            print("Shuffled Array:")
            display_array(my_array)

        elif choice == 16:
            save_array_to_file(my_array)

        elif choice == 17:
            my_array = load_array_from_file()

        elif choice == 18:
            print("Exiting the program.")
            break

        else:
            print("Invalid choice! Please enter a valid number.")

if __name__ == "__main__":
    main()
