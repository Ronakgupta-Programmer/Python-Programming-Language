import tkinter as tk
import math

# Function to calculate the square root
def calculate_square_root():
    try:
        num = float(entry.get())
        if num < 0:
            result_label.config(text="Please enter a non-negative number.", fg="red")
        else:
            result = math.sqrt(num)
            result_label.config(text=f"The square root of {num} is {result:.2f}.", fg="green")
    except ValueError:
        result_label.config(text="Please enter a valid number.", fg="red")

# Set up the main GUI window
root = tk.Tk()
root.title("Square Root Calculator")
root.geometry("500x400")
root.configure(bg="#2c3e50")

# Create a title label
title_label = tk.Label(root, text="Square Root Calculator", font=("Arial", 28, "bold"), bg="#2c3e50", fg="#ecf0f1")
title_label.pack(pady=20)

# Create and place the input label and entry widget
label = tk.Label(root, text="Enter a Number:", font=("Arial", 20), bg="#2c3e50", fg="#ecf0f1")
label.pack(pady=10)

entry = tk.Entry(root, font=("Arial", 20), width=20)
entry.pack(pady=10)

# Create and place the check button with styling
check_button = tk.Button(root, text="Calculate Square Root", command=calculate_square_root, 
                         font=("Arial", 20), bg="#27ae60", fg="white", relief="raised", bd=2)
check_button.pack(pady=20)

# Create a label to display the result
result_label = tk.Label(root, text="", font=("Arial", 20), bg="#2c3e50", fg="#ecf0f1")
result_label.pack(pady=20)

# Start the main loop
root.mainloop()
