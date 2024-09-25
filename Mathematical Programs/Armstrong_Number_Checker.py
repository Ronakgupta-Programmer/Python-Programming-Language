import tkinter as tk
from tkinter import font 
# Function to check if a number is an Armstrong number
def check_armstrong():
    try:
        a = int(entry.get())
        b = str(a)
        c = len(b)
        sum = 0
        
        # Calculate the Armstrong sum
        for i in b:
            sum += int(i) ** c
        # Update the result label based on the calculation
        if sum == a:
            result_label.config(text=f"The number {a} is an Armstrong number!",fg="green",font=("Arial", 24, "bold"))
        else:
            result_label.config(text=f"The number {a} is not an Armstrong number.",fg="red", font=("Arial", 24, "bold"))
    except ValueError:
        result_label.config(text="Please enter a valid integer.", fg="red")

# Set up the main GUI window
root = tk.Tk()
root.title("Armstrong Number Checker")
root.geometry("500x400")
root.configure(bg="#2c3e50")  # Dark blue background

# Create a title label
title_label = tk.Label(root, text="Armstrong Number Checker", font=("Arial", 28, "bold"), bg="#2c3e50", fg="#ecf0f1")
title_label.pack(pady=20)

# Create and place the input label and entry widget
label = tk.Label(root, text="Enter a Number:", font=("Arial", 20), bg="#2c3e50", fg="#ecf0f1")
label.pack(pady=10)

entry = tk.Entry(root, font=("Arial", 20), width=20)
entry.pack(pady=10)

# Create and place the check button with styling
check_button = tk.Button(root, text="Check Armstrong Number", command=check_armstrong, 
                         font=("Arial", 20), bg="#27ae60", fg="white", relief="raised", bd=2)
check_button.pack(pady=20)

# Create a label to display the result
result_label = tk.Label(root, text="", font=("Arial", 20), bg="#2c3e50", fg="#ecf0f1")
result_label.pack(pady=20)

# Start the main loop
root.mainloop()
