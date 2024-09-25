import tkinter as tk

# Function to check if a string is a palindrome
def is_palindrome(s):
    return s == s[::-1]  # Check if the string is equal to its reverse

# Function to check the palindrome and update the GUI
def check_palindrome():
    input_text = entry.get()
    if input_text.strip() == "":  # Check for empty input
        result_label.config(text="Please enter a valid string.", fg="red", font=("Arial", 22, "bold"))
    else:
        if is_palindrome(input_text):
            result_label.config(text=f'{input_text} is a palindrome!', fg="green", font=("Arial", 22, "bold"))
        else:
            result_label.config(text=f'{input_text} is not a palindrome.', fg="red", font=("Arial", 22, "bold"))

# Set up the main GUI window
root = tk.Tk()
root.title("Palindrome Checker")
root.geometry("600x400")  # Width for larger input
root.configure(bg="#2c3e50")  # Dark blue background

# Create a title label
title_label = tk.Label(root, text="Palindrome Checker", font=("Arial", 28, "bold"), bg="#2c3e50", fg="#ecf0f1")
title_label.pack(pady=20)

# Create and place the input label and entry widget
label = tk.Label(root, text="Enter a String:", font=("Arial", 20), bg="#2c3e50", fg="#ecf0f1")
label.pack(pady=10)

entry = tk.Entry(root, font=("Arial", 20), width=30)  # Increased width for better user experience
entry.pack(pady=10)

# Create and place the check button with styling
check_button = tk.Button(root, text="Check Palindrome", command=check_palindrome, 
                         font=("Arial", 20), bg="#27ae60", fg="white", relief="raised", bd=2)
check_button.pack(pady=20)

# Create a label to display the result
result_label = tk.Label(root, text="", font=("Arial", 20), bg="#2c3e50", fg="#ecf0f1")
result_label.pack(pady=20)

# Start the main loop
root.mainloop()
