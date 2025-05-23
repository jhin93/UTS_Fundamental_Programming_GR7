import tkinter as tk
import sys
import os
import json
# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from models.student import Student
from tkinter import messagebox
from .exception_view import validate_email, validate_password

# Create data directory if it doesn't exist
DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), 'data')
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

DATA_FILE = os.path.join(DATA_DIR, 'students.data')

def load_students():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r') as f:
        data = json.load(f)
        return data.get('students', [])

def save_students(students):
    # Convert to dictionary format if needed
    students_data = [s.to_dict() if hasattr(s, 'to_dict') else s for s in students]
    with open(DATA_FILE, 'w') as f:
        json.dump({"students": students_data}, f, indent=4)

def find_student(email, password):
    students = load_students()
    for s in students:
        student = Student.from_dict(s)
        if student.email == email and student.password == password:
            return student
    return None

class LoginView:
    def __init__(self, parent, show_enrolment_callback):
        self.parent = parent
        self.show_enrolment_callback = show_enrolment_callback
        self.setup_ui()

    def setup_ui(self):
        self.clear()
        # Set window size to 720x360
        self.parent.geometry("720x360")
        # Center the window on the screen
        self.parent.update_idletasks()
        width = self.parent.winfo_width()
        height = self.parent.winfo_height()
        x = (self.parent.winfo_screenwidth() // 2) - (width // 2)
        y = (self.parent.winfo_screenheight() // 2) - (height // 2)
        self.parent.geometry(f'{width}x{height}+{x}+{y}')
        
        tk.Label(self.parent, text="University App", font=("Arial", 16)).pack(pady=10)
        tk.Label(self.parent, text="Email:").pack()
        self.email_entry = tk.Entry(self.parent)
        self.email_entry.pack()
        tk.Label(self.parent, text="Password:").pack()
        self.password_entry = tk.Entry(self.parent, show="*")
        self.password_entry.pack()

        tk.Button(self.parent, text="Login", width=20, command=self.login_action).pack(pady=7)

    def clear(self):
        for widget in self.parent.winfo_children():
            widget.destroy()

    def login_action(self):
        email = self.email_entry.get().strip()
        password = self.password_entry.get().strip()
        if not email or not password:
            messagebox.showerror("Login Error", "All fields must be filled.")
            return
        if not validate_email(email):
            messagebox.showerror("Login Error", "Email must end with @university.com")
            return
        student = find_student(email, password)
        if student:
            self.show_enrolment_callback(student)
        else:
            messagebox.showerror("Login Error", "Incorrect credentials or student not registered.") 