import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import Calendar

# Password for accessing the attendance management system
PASSWORD = "Ronaksir"  # Change this to your desired password

# Student class to store individual student information
class Student:
    def __init__(self, student_id, name, course, admission_date):
        self.id = student_id
        self.name = name
        self.course = course
        self.admission_date = admission_date
        self.attendance = {}  # Dictionary to store attendance by date

# Function to check the password and open the main application
def check_password():
    entered_password = password_entry.get()
    if entered_password == PASSWORD:
        password_window.destroy()  # Close the password window
        open_main_application()  # Open the main application
    else:
        messagebox.showwarning("Invalid Password", "The entered password is incorrect.")

# Function to open the main application
def open_main_application():
    global root
    root = tk.Tk()
    root.title("Attendance Management System")
    root.geometry("800x500")  # Set window size
    root.minsize(800, 500)  # Set minimum size for the window

    # Create a Notebook (tabs)
    notebook = ttk.Notebook(root)
    notebook.pack(pady=10, expand=True, fill='both')  # Fill both horizontally and vertically

    # Tab for Adding or Updating Students
    tab_add_student = ttk.Frame(notebook)
    notebook.add(tab_add_student, text="Add Student")

    tk.Label(tab_add_student, text="Select Course", font=("Arial", 16)).grid(row=0, column=0, columnspan=2, pady=10)

    selected_course = tk.StringVar()
    course_combobox = ttk.Combobox(tab_add_student, textvariable=selected_course, values=["Multimedia", "Programming", "Tally", "Basic", "Data Science"], font=("Arial", 12))
    course_combobox.grid(row=1, column=0, columnspan=2, sticky=tk.EW)

    tk.Label(tab_add_student, text="Student ID: ", font=("Arial", 12)).grid(row=2, column=0, sticky=tk.W)
    entry_id = tk.Entry(tab_add_student, font=("Arial", 12))
    entry_id.grid(row=2, column=1, sticky=tk.EW)

    tk.Label(tab_add_student, text="Name: ", font=("Arial", 12)).grid(row=3, column=0, sticky=tk.W)
    entry_name = tk.Entry(tab_add_student, font=("Arial", 12))
    entry_name.grid(row=3, column=1, sticky=tk.EW)

    tk.Label(tab_add_student, text="Admission Date: ", font=("Arial", 12)).grid(row=4, column=0, sticky=tk.W)
    entry_admission_date = tk.Entry(tab_add_student, font=("Arial", 12))
    entry_admission_date.grid(row=4, column=1, sticky=tk.EW)

    btn_save_student = tk.Button(tab_add_student, text="Save Student", command=lambda: save_student(entry_id, entry_name, entry_admission_date, selected_course), bg='lightgreen', font=("Arial", 12))
    btn_save_student.grid(row=5, column=0, columnspan=2, sticky=tk.EW, pady=10)

    # Tab for Marking Attendance
    tab_mark_attendance = ttk.Frame(notebook)
    notebook.add(tab_mark_attendance, text="Mark Attendance")

    tk.Label(tab_mark_attendance, text="Mark Attendance", font=("Arial", 16)).grid(row=0, column=0, columnspan=2, pady=10)

    # Dropdown for Student IDs
    tk.Label(tab_mark_attendance, text="Select Student ID: ", font=("Arial", 12)).grid(row=1, column=0, sticky=tk.W)
    selected_student_id = tk.StringVar()
    student_id_combobox = ttk.Combobox(tab_mark_attendance, textvariable=selected_student_id, font=("Arial", 12))
    student_id_combobox.grid(row=1, column=1, sticky=tk.EW)

    # Add Calendar widget to select date
    tk.Label(tab_mark_attendance, text="Select Date: ", font=("Arial", 12)).grid(row=2, column=0, sticky=tk.W)
    calendar = Calendar(tab_mark_attendance, selectmode='day', date_pattern='yyyy-mm-dd')
    calendar.grid(row=2, column=1, sticky=tk.EW)

    # Add Radio Buttons for attendance status (Present or Absent)
    attendance_status = tk.StringVar()
    attendance_status.set("Present")  # Default value

    tk.Label(tab_mark_attendance, text="Attendance Status: ", font=("Arial", 12)).grid(row=3, column=0, sticky=tk.W)
    radio_present = tk.Radiobutton(tab_mark_attendance, text="Present", variable=attendance_status, value="Present", font=("Arial", 12))
    radio_present.grid(row=3, column=1, sticky=tk.W)
    radio_absent = tk.Radiobutton(tab_mark_attendance, text="Absent", variable=attendance_status, value="Absent", font=("Arial", 12))
    radio_absent.grid(row=4, column=1, sticky=tk.W)

    btn_mark = tk.Button(tab_mark_attendance, text="Mark Attendance", command=lambda: mark_attendance(selected_student_id, calendar, attendance_status), bg='lightblue', font=("Arial", 12))
    btn_mark.grid(row=5, column=0, columnspan=2, sticky=tk.EW, pady=10)

    # Tab for Deleting Students
    tab_delete_student = ttk.Frame(notebook)
    notebook.add(tab_delete_student, text="Delete Student")

    tk.Label(tab_delete_student, text="Delete Student Record", font=("Arial", 16)).grid(row=0, column=0, columnspan=2, pady=10)

    tk.Label(tab_delete_student, text="Select Student ID to Delete: ", font=("Arial", 12)).grid(row=1, column=0, sticky=tk.W)
    student_id_delete_combobox = ttk.Combobox(tab_delete_student, values=[], font=("Arial", 12))
    student_id_delete_combobox.grid(row=1, column=1, sticky=tk.EW)

    btn_delete_student = tk.Button(tab_delete_student, text="Delete Student", command=lambda: delete_student(student_id_delete_combobox), bg='lightcoral', font=("Arial", 12))
    btn_delete_student.grid(row=2, column=0, columnspan=2, sticky=tk.EW, pady=10)

    # Tab for Viewing Attendance
    tab_view_attendance = ttk.Frame(notebook)
    notebook.add(tab_view_attendance, text="View Attendance")

    btn_view = tk.Button(tab_view_attendance, text="View Attendance Records", command=view_attendance, bg='lightblue', font=("Arial", 12))
    btn_view.pack(pady=20)

    # Configure column weight for dynamic resizing
    for i in range(2):
        tab_add_student.columnconfigure(i, weight=1)
        tab_mark_attendance.columnconfigure(i, weight=1)
        tab_delete_student.columnconfigure(i, weight=1)

    # Update the student ID comboboxes when a student is added
    update_student_id_combobox(student_id_combobox, student_id_delete_combobox)

    # Start the Tkinter main loop for the main application
    root.mainloop()

# Function to add or update a student
def save_student(entry_id, entry_name, entry_admission_date, selected_course):
    student_id = entry_id.get()
    name = entry_name.get()
    admission_date = entry_admission_date.get()

    if student_id.isdigit() and name != "" and admission_date:
        student_id = int(student_id)

        # Check if student already exists for updating
        for student in students:
            if student.id == student_id:
                student.name = name
                student.course = selected_course.get()
                student.admission_date = admission_date
                messagebox.showinfo("Success", f"Student {name} updated successfully!")
                clear_student_inputs(entry_id, entry_name, entry_admission_date)
                update_student_id_combobox(student_id_combobox, student_id_delete_combobox)  # Update the comboboxes
                return

        # If student does not exist, add as new
        new_student = Student(student_id, name, selected_course.get(), admission_date)
        students.append(new_student)
        messagebox.showinfo("Success", f"Student {name} added successfully!")
        clear_student_inputs(entry_id, entry_name, entry_admission_date)
        update_student_id_combobox(student_id_combobox, student_id_delete_combobox)  # Update the comboboxes
    else:
        messagebox.showwarning("Input Error", "Please enter valid Student ID, Name, and Admission Date.")

# Function to clear student input fields
def clear_student_inputs(entry_id, entry_name, entry_admission_date):
    entry_id.delete(0, tk.END)
    entry_name.delete(0, tk.END)
    entry_admission_date.delete(0, tk.END)

# Function to mark attendance for a student on a specific date
def mark_attendance(selected_student_id, calendar, attendance_status):
    student_id = selected_student_id.get()
    attendance_date = calendar.get_date()
    status = attendance_status.get()

    if student_id.isdigit():
        student_id = int(student_id)
        for student in students:
            if student.id == student_id:
                student.attendance[attendance_date] = status
                messagebox.showinfo("Success", f"Attendance marked for {student.name} on {attendance_date} as {status}.")
                return
        messagebox.showwarning("Not Found", f"Student with ID {student_id} not found.")
    else:
        messagebox.showwarning("Input Error", "Please select a valid Student ID.")

# Function to delete a student
def delete_student(student_id_combobox):
    student_id = student_id_combobox.get()
    if student_id.isdigit():
        student_id = int(student_id)
        for student in students:
            if student.id == student_id:
                students.remove(student)
                messagebox.showinfo("Success", f"Student with ID {student_id} deleted successfully.")
                update_student_id_combobox(student_id_combobox, student_id_combobox)  # Update the delete combobox
                return
        messagebox.showwarning("Not Found", f"Student with ID {student_id} not found.")
    else:
        messagebox.showwarning("Input Error", "Please select a valid Student ID.")

# Function to view the attendance of all students
def view_attendance():
    if not students:
        messagebox.showinfo("No Students", "No students added yet.")
        return

    attendance_window = tk.Toplevel(root)
    attendance_window.title("Attendance Records")
    attendance_window.geometry("800x400")  # Set window size

    tk.Label(attendance_window, text="ID\tName\t\t\tCourse\t\tAdmission Date\tAttendance", font=("Arial", 12)).grid(row=0, column=0, sticky='w')
    tk.Label(attendance_window, text="---------------------------------------------------------------------------------------------------").grid(row=1, column=0, sticky='w')

    for index, student in enumerate(students):
        attendance_str = ', '.join([f"{date}: {status}" for date, status in student.attendance.items()])
        tk.Label(attendance_window, text=f"{student.id}\t{student.name:20}\t{student.course:20}\t{student.admission_date}\t{attendance_str}", font=("Arial", 12)).grid(row=index + 2, column=0, sticky='w')

# Function to update the student ID combobox
def update_student_id_combobox(*comboboxes):
    for student_id_combobox in comboboxes:
        student_id_combobox['values'] = [student.id for student in students]
        student_id_combobox.set("")  # Clear selection

# Global variables
students = []  # List to store all students

# Password window
password_window = tk.Tk()  # Create password window
password_window.title("Enter Password")
password_window.geometry("300x150")  # Set window size

tk.Label(password_window, text="Enter Password:", font=("Arial", 12)).pack(pady=20)
password_entry = tk.Entry(password_window, show="*", font=("Arial", 12))
password_entry.pack(pady=5)

btn_submit = tk.Button(password_window, text="Submit", command=check_password, bg='lightgreen', font=("Arial", 12))
btn_submit.pack(pady=10)

# Start the Tkinter main loop for the password window
password_window.mainloop()