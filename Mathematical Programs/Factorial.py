import tkinter as tk

# Function to calculate the factorial
def factorial(num):
    if num == 1 or num == 0:
        return 1
    else:
        return num * factorial(num - 1)

# Function to check the factorial and update the GUI
def check_factorial():
    try:
        num = int(entry.get())
        if num < 0:
            result_label.config(text="Please enter a non-negative integer.", fg="red", font=("Arial", 25, "bold"))
        else:
            result = factorial(num)
            # Convert result to string to handle large numbers
            result_str = f"The factorial of {num} is:\n{result}"
            result_label.config(text=result_str, fg="white", font=("Arial", 20, "bold"))
    except ValueError:
        result_label.config(text="Please enter a valid integer.", fg="red", font=("Arial", 20, "bold"))

# Set up the main GUI window
root = tk.Tk()
root.title("Factorial Calculator")
root.geometry("600x400")  # Increased width for larger numbers
root.configure(bg="#2c3e50")  # Dark blue background

# Create a title label
title_label = tk.Label(root, text="Factorial Calculator", font=("Arial", 28, "bold"), bg="#2c3e50", fg="#ecf0f1")
title_label.pack(pady=20)

# Create and place the input label and entry widget
label = tk.Label(root, text="Enter a Number:", font=("Arial", 20), bg="#2c3e50", fg="#ecf0f1")
label.pack(pady=10)

entry = tk.Entry(root, font=("Arial", 20), width=25)  # Increased width
entry.pack(pady=10)

# Create and place the check button with styling
check_button = tk.Button(root, text="Calculate Factorial", command=check_factorial, 
                         font=("Arial", 20), bg="#27ae60", fg="white", relief="raised", bd=2)
check_button.pack(pady=20)

# Create a label to display the result
result_label = tk.Label(root, text="", font=("Arial", 16), bg="#2c3e50", fg="#ecf0f1", wraplength=500)  # Adjusted font size and added wrap length
result_label.pack(pady=20)

# Start the main loop
root.mainloop()
