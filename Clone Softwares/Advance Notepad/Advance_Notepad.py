import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog, colorchooser
from tkinter import ttk
from PIL import Image, ImageTk  # For loading images

class Notepad:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Notepad")
        self.root.geometry("800x600")
        self.root.iconbitmap(r"D:\Programming Files\Python Programming Language\New folder\note.ico")

        # Create menu
        self.menu = tk.Menu(self.root)
        self.root.config(menu=self.menu)

        # Text area with scrollbar
        self.text_frame = tk.Frame(self.root)
        self.text_frame.pack(fill="both", expand=True)

        self.scrollbar = tk.Scrollbar(self.text_frame)
        self.scrollbar.pack(side="right", fill="y")

        # Set wrap to 'word' for always wrapping text
        self.text_area = tk.Text(self.text_frame, font=("Arial", 12), undo=True, wrap="word", yscrollcommand=self.scrollbar.set)
        self.text_area.pack(fill="both", expand=True)
        self.scrollbar.config(command=self.text_area.yview)

        # File menu
        self.file_menu = tk.Menu(self.menu)
        self.menu.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="New", command=self.new_file)
        self.file_menu.add_command(label="Open...", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_command(label="Save As...", command=self.save_as_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.root.quit)

        # Edit menu
        self.edit_menu = tk.Menu(self.menu)
        self.menu.add_cascade(label="Edit", menu=self.edit_menu)
        self.edit_menu.add_command(label="Undo", command=self.undo)
        self.edit_menu.add_command(label="Redo", command=self.redo)
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="Cut", command=self.cut)
        self.edit_menu.add_command(label="Copy", command=self.copy)
        self.edit_menu.add_command(label="Paste", command=self.paste)
        self.edit_menu.add_command(label="Select All", command=self.select_all)
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="Find", command=self.find_text)
        self.edit_menu.add_command(label="Find & Replace", command=self.find_replace)

        # View menu
        self.view_menu = tk.Menu(self.menu)
        self.menu.add_cascade(label="View", menu=self.view_menu)
        
        # Removed the word wrap toggle
        self.dark_mode = tk.BooleanVar()
        self.dark_mode.set(False)
        self.view_menu.add_checkbutton(label="Dark Mode", onvalue=True, offvalue=False, variable=self.dark_mode, command=self.toggle_dark_mode)

        # Font Styles
        self.font_menu = tk.Menu(self.menu)
        self.menu.add_cascade(label="Font Styles", menu=self.font_menu)

        font_families = ["Arial", "Courier", "Times New Roman", "Verdana", "Helvetica", "Georgia"]

        for family in font_families:
            self.font_menu.add_command(label=family, command=lambda f=family: self.set_font_family(f))

        # Font Size
        self.font_size = tk.Menu(self.menu)
        self.menu.add_cascade(label="Font Size", menu=self.font_size)

        font_sizes = [8, 10, 12, 14, 16, 18, 20, 24, 28, 32]
        for size in font_sizes:
            self.font_size.add_command(label=str(size), command=lambda s=size: self.set_font_size(s))

        # Font Color
        self.color_menu = tk.Menu(self.menu)
        self.menu.add_cascade(label="Font Color", menu=self.color_menu)
        self.color_menu.add_command(label="Choose Font Color", command=self.change_font_color)

        # Font Styles (Bold, Italic, Underline)
        self.style_menu = tk.Menu(self.menu)
        self.menu.add_cascade(label="Text Styles", menu=self.style_menu)
        self.style_menu.add_command(label="Bold", command=self.toggle_bold)
        self.style_menu.add_command(label="Italic", command=self.toggle_italic)
        self.style_menu.add_command(label="Underline", command=self.toggle_underline)

        # Help menu
        self.help_menu = tk.Menu(self.menu)
        self.menu.add_cascade(label="Help", menu=self.help_menu)
        self.help_menu.add_command(label="About", command=self.about)

        # Status bar
        self.status_bar = tk.Label(self.root, text="Ready", anchor="w")
        self.status_bar.pack(fill="x")

    def new_file(self):
        self.text_area.delete(1.0, "end")
        self.root.title("Untitled - Advanced Notepad")

    def open_file(self):
        file_path = filedialog.askopenfilename(title="Open File", filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, "r") as file:
                self.text_area.delete(1.0, "end")
                self.text_area.insert("end", file.read())
                self.root.title(f"{file_path} - Advanced Notepad")

    def save_file(self):
        file_path = filedialog.asksaveasfilename(title="Save File", filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, "w") as file:
                file.write(self.text_area.get(1.0, "end-1c"))
                self.root.title(f"{file_path} - Advanced Notepad")

    def save_as_file(self):
        file_path = filedialog.asksaveasfilename(title="Save As", filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, "w") as file:
                file.write(self.text_area.get(1.0, "end-1c"))
                self.root.title(f"{file_path} - Advanced Notepad")

    def cut(self):
        self.text_area.clipboard_clear()
        self.text_area.clipboard_append(self.text_area.selection_get())
        self.text_area.delete("sel.first", "sel.last")

    def copy(self):
        self.text_area.clipboard_clear()
        self.text_area.clipboard_append(self.text_area.selection_get())

    def paste(self):
        self.text_area.insert("insert", self.text_area.clipboard_get())

    def select_all(self):
        self.text_area.tag_add("sel", "1.0", "end")

    def undo(self):
        self.text_area.edit_undo()

    def redo(self):
        self.text_area.edit_redo()

    def find_text(self):
        find_window = tk.Toplevel(self.root)
        find_window.title("Find")
        find_window.geometry("300x100")
        tk.Label(find_window, text="Find:").pack(side="left")
        find_entry = tk.Entry(find_window)
        find_entry.pack(side="left", padx=10)
        tk.Button(find_window, text="Find", command=lambda: self.text_area.tag_add("found", "1.0", "end")).pack(side="left")

    def find_replace(self):
        find_replace_window = tk.Toplevel(self.root)
        find_replace_window.title("Find & Replace")
        find_replace_window.geometry("400x150")
        tk.Label(find_replace_window, text="Find:").pack(side="left")
        find_entry = tk.Entry(find_replace_window)
        find_entry.pack(side="left", padx=10)
        tk.Label(find_replace_window, text="Replace:").pack(side="left")
        replace_entry = tk.Entry(find_replace_window)
        replace_entry.pack(side="left", padx=10)
        tk.Button(find_replace_window, text="Find & Replace", command=lambda: self.text_area.replace("1.0", "end", replace_entry.get())).pack(side="left")

    def about(self):
        # Show about information in a message box
        messagebox.showinfo("About Advanced Notepad", "Advanced Notepad\nVersion 2.0\nWINDOW 10")

    def set_font_family(self, family):
        self.text_area.config(font=(family, self.text_area.cget("font").split()[1]))

    def set_font_size(self, size):
        self.text_area.config(font=(self.text_area.cget("font").split()[0], size))

    def change_font_color(self):
        color = colorchooser.askcolor(title="Choose Font Color")[1]
        if color:
            self.text_area.config(fg=color)

    def toggle_dark_mode(self):
        if self.dark_mode.get():
            self.text_area.config(bg="black", fg="white", insertbackground="white")
        else:
            self.text_area.config(bg="white", fg="black", insertbackground="black")

    def toggle_bold(self):
        current_font = self.text_area.cget("font").split()
        if "bold" in current_font:
            current_font.remove("bold")
        else:
            current_font.append("bold")
        self.text_area.config(font=" ".join(current_font))

    def toggle_italic(self):
        current_font = self.text_area.cget("font").split()
        if "italic" in current_font:
            current_font.remove("italic")
        else:
            current_font.append("italic")
        self.text_area.config(font=" ".join(current_font))

    def toggle_underline(self):
        current_font = self.text_area.cget("font").split()
        if "underline" in current_font:
            current_font.remove("underline")
        else:
            current_font.append("underline")
        self.text_area.config(font=" ".join(current_font))

if __name__ == "__main__":
    root = tk.Tk()
    notepad = Notepad(root)
    root.mainloop()
