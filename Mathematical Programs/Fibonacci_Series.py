import tkinter as tk

# Function to generate the Fibonacci series
def fibonacci(n):
    fib_series = []
    a, b = 0, 1
    for _ in range(n):
        fib_series.append(a)
        a, b = b, a + b
    return fib_series

# Function to check the Fibonacci series and update the GUI
def display_fibonacci():
    try:
        num = int(entry.get())
        if num < 0:
            result_label.config(text="Please enter a non-negative integer.", fg="red", font=("Arial", 20, "bold"))
        else:
            series = fibonacci(num)
            result_str = f"The Fibonacci series up to {num} terms is:\n{series}"
            result_label.config(text=result_str, fg="white", font=("Arial", 16))
    except ValueError:
        result_label.config(text="Please enter a valid integer.", fg="red")

# Set up the main GUI window
root = tk.Tk()
root.title("Fibonacci Series Generator")
root.geometry("600x400")  # Width for larger numbers
root.configure(bg="#2c3e50")  # Dark blue background

# Create a title label
title_label = tk.Label(root, text="Fibonacci Series Generator", font=("Arial", 28, "bold"), bg="#2c3e50", fg="#ecf0f1")
title_label.pack(pady=20)

# Create and place the input label and entry widget
label = tk.Label(root, text="Enter Number of Terms:", font=("Arial", 20), bg="#2c3e50", fg="#ecf0f1")
label.pack(pady=10)

entry = tk.Entry(root, font=("Arial", 20), width=25)  # Increased width
entry.pack(pady=10)

# Create and place the generate button with styling
generate_button = tk.Button(root, text="Generate Fibonacci Series", command=display_fibonacci, 
                             font=("Arial", 20), bg="#27ae60", fg="white", relief="raised", bd=2)
generate_button.pack(pady=20)

# Create a label to display the result
result_label = tk.Label(root, text="", font=("Arial", 16), bg="#2c3e50", fg="#ecf0f1", wraplength=500)  # Adjusted font size and added wrap length
result_label.pack(pady=20)

# Start the main loop
root.mainloop()
