import tkinter as tk
import sys
import os
import pickle
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
    with open(DATA_FILE, 'rb') as f:
        return pickle.load(f)

def save_students(students):
    with open(DATA_FILE, 'wb') as f:
        pickle.dump(students, f)

def find_student(email, password):
    students = load_students()
    for s in students:
        if s.email == email and s.password == password:
            return s
    return None

class LoginView:
    def __init__(self, parent, show_register_callback, show_enrolment_callback):
        self.parent = parent
        self.show_register_callback = show_register_callback
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
        tk.Button(self.parent, text="Register", width=20, command=self.show_register_callback).pack()

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

class RegisterView:
    def __init__(self, parent, show_login_callback):
        self.parent = parent
        self.show_login_callback = show_login_callback
        self.setup_ui()

    def setup_ui(self):
        self.clear()
        tk.Label(self.parent, text="Student Registration", font=("Arial", 16)).pack(pady=10)
        tk.Label(self.parent, text="Name:").pack()
        self.name_entry = tk.Entry(self.parent)
        self.name_entry.pack()
        tk.Label(self.parent, text="Email:").pack()
        self.email_entry = tk.Entry(self.parent)
        self.email_entry.pack()
        tk.Label(self.parent, text="Password:").pack()
        self.password_entry = tk.Entry(self.parent, show="*")
        self.password_entry.pack()

        tk.Button(self.parent, text="Register", width=20, command=self.register_action).pack(pady=7)
        tk.Button(self.parent, text="Back to Login", width=20, command=self.show_login_callback).pack()

    def clear(self):
        for widget in self.parent.winfo_children():
            widget.destroy()

    def register_action(self):
        name = self.name_entry.get().strip()
        email = self.email_entry.get().strip()
        password = self.password_entry.get().strip()
        if not name or not email or not password:
            messagebox.showerror("Registration Error", "All fields must be filled.")
            return
        if not validate_email(email):
            messagebox.showerror("Registration Error", "Email must end with @university.com")
            return
        if not validate_password(password):
            messagebox.showerror("Registration Error", "Password must start with an uppercase letter, followed by at least 4 letters, and end with at least 3 digits.")
            return
        students = load_students()
        if any(s.email == email for s in students):
            messagebox.showerror("Registration Error", "Student already registered.")
            return
        student = Student(name, email, password)
        students.append(student)
        save_students(students)
        messagebox.showinfo("Registered", "Registration successful! You may now log in.")
        self.show_login_callback() 