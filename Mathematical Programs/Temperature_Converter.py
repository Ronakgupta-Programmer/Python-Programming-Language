import tkinter as tk

# Function to convert temperature
def convert_temperature():
    try:
        # Get the input temperature and scale
        temp = float(entry.get())
        scale = scale_var.get()

        if scale == "CELSIUS":
            # Convert Celsius to Fahrenheit
            converted_temp = (temp * 9/5) + 32
            result_label.config(text=f"{temp} °C = {converted_temp:.2f} °F", fg="green", font=("Arial", 20, "bold"))
        elif scale == "FAHRENHEIT":
            # Convert Fahrenheit to Celsius
            converted_temp = (temp - 32) * 5/9
            result_label.config(text=f"{temp} °F = {converted_temp:.2f} °C", fg="green", font=("Arial", 20, "bold"))
    except ValueError:
        result_label.config(text="Please enter a valid number.", fg="red")

# Set up the main GUI window
root = tk.Tk()
root.title("Temperature Converter")
root.geometry("600x400")
root.configure(bg="#2c3e50")  # Dark blue background

# Create a title label
title_label = tk.Label(root, text="Temperature Converter", font=("Arial", 28, "bold"), bg="#2c3e50", fg="#ecf0f1")
title_label.pack(pady=20)

# Create and place the input label and entry widget
label = tk.Label(root, text="Enter Temperature:", font=("Arial", 20), bg="#2c3e50", fg="#ecf0f1")
label.pack(pady=10)

entry = tk.Entry(root, font=("Arial", 20), width=20)
entry.pack(pady=10)

# Create a dropdown menu for temperature scale selection
scale_var = tk.StringVar(value="CELSIUS")
scale_menu = tk.OptionMenu(root, scale_var, "CELSIUS", "FAHRENHEIT")
scale_menu.config(font=("Arial", 20), bg="#3498db", fg="white")
scale_menu.pack(pady=10)

# Create and place the convert button with styling
convert_button = tk.Button(root, text="Convert", command=convert_temperature, 
                           font=("Arial", 20), bg="#27ae60", fg="white", relief="raised", bd=2)
convert_button.pack(pady=20)

# Create a label to display the result
result_label = tk.Label(root, text="", font=("Arial", 20), bg="#2c3e50", fg="#ecf0f1")
result_label.pack(pady=20)

# Start the main loop
root.mainloop()
