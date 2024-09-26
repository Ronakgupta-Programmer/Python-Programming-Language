import tkinter as tk
from tkinter import messagebox, font as tkFont
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
from tkhtmlview import HTMLLabel

def scrape_amazon_data():
    # Retrieve the URL from the entry widget
    url = url_entry.get()

    if not url or not re.match(r'https?://(www\.)?amazon\.\w{2,3}/.*', url):
        messagebox.showwarning("Input Error", "Please enter a valid Amazon product URL.")
        return

    # Set up the Selenium WebDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    try:
        driver.get(url)

        # Wait for the main product element to load
        product_container = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#dp-container"))
        )

        # Example: Scrape product titles and prices
        title_element = product_container.find_element(By.CSS_SELECTOR, "#productTitle")
        price_element = product_container.find_element(By.CSS_SELECTOR, ".a-price-whole")

        title = title_element.text.strip() if title_element else "Title not found"
        price = price_element.text.strip() if price_element else "Price not available"

        # Display the results
        result_text.set(f"Title: {title}\nPrice: {price}")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")
    finally:
        driver.quit()

def scale_window(root):
    # Get the current screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Set the desired width and height for the main window
    desired_width = int(screen_width * 0.75)  # 75% of the screen width
    desired_height = int(screen_height * 0.75)  # 75% of the screen height

    # Set the window geometry
    root.geometry(f"{desired_width}x{desired_height}")

# Set up the Tkinter window
root = tk.Tk()
root.title("Amazon Data Scraper")

# Call the scale function to set the window size
scale_window(root)

# Main Frame with a border
main_frame = tk.Frame(root, bd=2, relief=tk.SUNKEN)
main_frame.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.95, relheight=0.95)

# Heading
heading_font = tkFont.Font(family="Helvetica", size=30, weight="bold")
heading_label = tk.Label(main_frame, text="DATA SCRAPING", font=heading_font)
heading_label.place(relx=0.5, y=20, anchor="n")

# URL Label and Entry
label_font = tkFont.Font(family="Helvetica", size=20, weight="bold")
url_label = tk.Label(main_frame, text="Amazon Link:", font=label_font)
url_label.place(relx=0.5, y=80, anchor="n")  # Center the label horizontally

url_entry = tk.Entry(main_frame, width=int(root.winfo_screenwidth() / 20), font=("Helvetica", 16))
url_entry.place(relx=0.5, y=130, anchor="n")  # Adjust x for better placement

# Scrape Button
button_font = tkFont.Font(family="Helvetica", size=18, weight="bold")
scrape_button = tk.Button(main_frame, text="Scrape Data", command=scrape_amazon_data, font=button_font)
scrape_button.place(relx=0.5, y=180, anchor="n")

# Result Display
result_text = tk.StringVar()
result_label = tk.Label(main_frame, textvariable=result_text, justify=tk.CENTER, font=("Helvetica", 18, "bold"), wraplength=int(root.winfo_screenwidth() / 2))
result_label.place(relx=0.5, y=250, anchor="n")

# Embedded browser using tkhtmlview
browser_label = HTMLLabel(main_frame, html="")
browser_label.place(relx=0.5, rely=0.5, anchor="n", relwidth=0.95, relheight=0.4)

# Run the Tkinter event loop
root.mainloop()
