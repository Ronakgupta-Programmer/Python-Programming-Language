import qrcode as qr
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk

# Function to generate QR code and display it in the GUI
def generate_qr():
    user_link = url_entry.get()  # Get the URL from the entry field
    if user_link:
        qr1 = qr.QRCode(version=1,
                        error_correction=qr.constants.ERROR_CORRECT_H,
                        box_size=10, border=2)
        
        qr1.add_data(user_link)
        qr1.make(fit=True)
        
        img = qr1.make_image(fill_color="black", back_color="white")
        img.save("QR_Code.png")  # Save QR code image

        # Display the QR code in the GUI
        img = Image.open("QR_Code.png")
        img = img.resize((300, 300))  # Resize image for display
        img_tk = ImageTk.PhotoImage(img)
        
        qr_label.config(image=img_tk)
        qr_label.image = img_tk  # Keep a reference to avoid garbage collection

# Set up the GUI window
root = tk.Tk()
root.title("QR Code Generator")

# Get the screen size and adjust the window size accordingly
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = int(screen_width * 0.5)  # 50% of screen width
window_height = int(screen_height * 0.6)  # 60% of screen height
root.geometry(f"{window_width}x{window_height}")  # Set window size

# Lock the window size
root.resizable(False, False)

# Create a frame for the URL input with attractive styling
frame = ttk.Frame(root, padding="20")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E))

# Label and Entry for URL input with increased font size
url_label = ttk.Label(frame, text="Enter URL:", font=("Helvetica", 14))
url_label.grid(row=0, column=0, sticky=tk.W)

url_entry = ttk.Entry(frame, width=30, font=("Helvetica", 14))
url_entry.grid(row=0, column=1)

# Button to generate QR code with increased font size
generate_button = ttk.Button(frame, text="Generate QR Code", command=generate_qr, style="TButton")
generate_button.grid(row=0, column=2, padx=10)

# Label to display the QR code, centered
qr_label = ttk.Label(root)
qr_label.grid(row=1, column=0, pady=20)

# Configure style for the button to make it more attractive
style = ttk.Style()
style.configure("TButton", font=("Helvetica", 12), padding=10)

# Run the application
root.mainloop()
