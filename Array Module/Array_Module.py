import array as arr
import random

def display_array(array):
    print("Array ke elements:", array)

def save_array_to_file(array):
    filename = input("File ka naam daaliye (e.g., array.txt): ")
    with open(filename, 'w') as file:
        for item in array:
            file.write(f"{item}\n")
    print(f"Array ko '{filename}' mein save kiya gaya.")

def load_array_from_file():
    filename = input("File ka naam daaliye (e.g., array.txt): ")
    try:
        with open(filename, 'r') as file:
            loaded_array = arr.array('i', [int(line.strip()) for line in file])
        print(f"Array '{filename}' se load kiya gaya:")
        display_array(loaded_array)
        return loaded_array
    except FileNotFoundError:
        print("File nahi mili! Kripya sahi filename daaliye.")
        return arr.array('i', [])

def main():
    my_array = arr.array('i', [])
    
    while True:
        print("\nMenu:")
        print("1. Add elements to the array")
        print("2. Display the array")
        print("3. Modify an element")
        print("4. Remove an element")
        print("5. Slice the array")
        print("6. Find an element")
        print("7. Count occurrences of an element")
        print("8. Sort the array")
        print("9. Reverse the array")
        print("10. Clear the array")
        print("11. Copy the array")
        print("12. Find max and min values")
        print("13. Calculate sum and average")
        print("14. Remove duplicates")
        print("15. Shuffle the array")
        print("16. Save to file")
        print("17. Load from file")
        print("18. Exit")
        
        choice = int(input("Apna chunav daaliye (1-18): "))
        
        if choice == 1:
            n = int(input("Kitne elements add karna chahte hain? "))
            for i in range(n):
                element = int(input(f"Element {i + 1} daaliye: "))
                my_array.append(element)
        
        elif choice == 2:
            display_array(my_array)
        
        elif choice == 3:
            index_to_modify = int(input("Kaunse index ka element modify karna chahte hain? "))
            new_value = int(input("Naya value daaliye: "))
            if 0 <= index_to_modify < len(my_array):
                my_array[index_to_modify] = new_value
                print("Modified Array:")
                display_array(my_array)
            else:
                print("Invalid index!")
        
        elif choice == 4:
            value_to_remove = int(input("Kaunse value ko remove karna chahte hain? "))
            if value_to_remove in my_array:
                my_array.remove(value_to_remove)
                print("Array after removing:")
                display_array(my_array)
            else:
                print("Value array mein nahi hai!")

        elif choice == 5:
            start_index = int(input("Slicing ke liye start index daaliye: "))
            end_index = int(input("Slicing ke liye end index daaliye: "))
            print("Sliced Array:", my_array[start_index:end_index])

        elif choice == 6:
            value_to_find = int(input("Kaunse value ko dhoondhna chahte hain? "))
            if value_to_find in my_array:
                print(f"{value_to_find} array mein maujood hai.")
            else:
                print(f"{value_to_find} array mein nahi hai.")

        elif choice == 7:
            value_to_count = int(input("Kaunse value ki ginti karni hai? "))
            count = my_array.count(value_to_count)
            print(f"{value_to_count} ki ginti: {count}")

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
            print("Array clear kar diya gaya.")

        elif choice == 11:
            copied_array = arr.array('i', my_array)
            print("Array ki copy:")
            display_array(copied_array)

        elif choice == 12:
            if my_array:
                max_value = max(my_array)
                min_value = min(my_array)
                print(f"Maximum Value: {max_value}")
                print(f"Minimum Value: {min_value}")
            else:
                print("Array khali hai!")

        elif choice == 13:
            if my_array:
                total = sum(my_array)
                average = total / len(my_array)
                print(f"Array ka total: {total}, Average: {average}")
            else:
                print("Array khali hai!")

        elif choice == 14:
            unique_array = arr.array('i', set(my_array))
            my_array = unique_array
            print("Duplicates remove kar diye gaye. Updated Array:")
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
            print("Program band ho raha hai.")
            break

        else:
            print("Invalid choice! Kripya sahi number daaliye.")

if __name__ == "__main__":
    main()
