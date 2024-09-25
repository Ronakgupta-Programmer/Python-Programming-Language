import tkinter as tk

# Function to calculate the percentage
def calculate_percentage():
    try:
        total = float(entry_total.get())
        part = float(entry_part.get())
        percentage = (part / total) * 100
        result_label.config(text=f"The percentage is: {percentage:.2f}%", fg="green")
    except ValueError:
        result_label.config(text="Please enter valid numbers.", fg="red")
    except ZeroDivisionError:
        result_label.config(text="Total cannot be zero.", fg="red")

# Set up the main GUI window
root = tk.Tk()
root.title("Percentage Calculator")
root.geometry("500x400")
root.configure(bg="#2c3e50")

# Create a title label
title_label = tk.Label(root, text="Percentage Calculator", font=("Arial", 28, "bold"), bg="#2c3e50", fg="#ecf0f1")
title_label.pack(pady=20)

# Create and place the input fields and labels
label_total = tk.Label(root, text="Enter Total:", font=("Arial", 20), bg="#2c3e50", fg="#ecf0f1")
label_total.pack(pady=10)
entry_total = tk.Entry(root, font=("Arial", 20), width=20)
entry_total.pack(pady=10)

label_part = tk.Label(root, text="Percent:", font=("Arial", 20), bg="#2c3e50", fg="#ecf0f1")
label_part.pack(pady=10)
entry_part = tk.Entry(root, font=("Arial", 20), width=20)
entry_part.pack(pady=10)

# Create and place the calculate button
calculate_button = tk.Button(root, text="Calculate Percentage", command=calculate_percentage, 
                              font=("Arial", 20), bg="#27ae60", fg="white", relief="raised", bd=2)
calculate_button.pack(pady=20)

# Create a label to display the result
result_label = tk.Label(root, text="", font=("Arial", 20), bg="#2c3e50", fg="#ecf0f1")
result_label.pack(pady=20)

# Start the main loop
root.mainloop()
