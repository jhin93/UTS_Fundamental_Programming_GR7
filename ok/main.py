import tkinter as tk
from tkinter import messagebox, simpledialog
import pickle
import os
import random
import re

DATA_FILE = 'students.data'

# -------------------- Models (identical to your CLI version) --------------------


class Subject:
    def __init__(self):
        self.subject_id = f"{random.randint(1, 999):03}"
        self.mark = random.randint(25, 100)
        self.grade = self.calculate_grade()

    def calculate_grade(self):
        if self.mark >= 85:
            return 'HD'
        elif self.mark >= 75:
            return 'D'
        elif self.mark >= 65:
            return 'C'
        elif self.mark >= 50:
            return 'P'
        else:
            return 'F'


class Student:
    def __init__(self, name, email, password):
        self.student_id = f"{random.randint(1, 999999):06}"
        self.name = name
        self.email = email
        self.password = password
        self.enrolled_subjects = []


# Sample student data
students = [
    Student("Admin User", "admin@university.com", "Admin123"),
    Student("Test Student", "student@university.com", "pass123")
]

# Write to file
with open("students.data", "wb") as f:
    pickle.dump(students, f)

print("✅ students.data created")


def enrol_subject(self):
    if len(self.enrolled_subjects) < 4:
        subject = Subject()
        self.enrolled_subjects.append(subject)
        return subject
    else:
        return None


def remove_subject(self, subject_id):
    before = len(self.enrolled_subjects)
    self.enrolled_subjects = [
        s for s in self.enrolled_subjects if s.subject_id != subject_id]
    return len(self.enrolled_subjects) < before

# -------------------- Data Source --------------------


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


def validate_email(email):
    return email.endswith('@university.com')


def validate_password(password):
    return re.match(r'^[A-Z][a-zA-Z]{4,}\d{3,}$', password)

# -------------------- GUI --------------------


class GUIUniApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("GUIUniApp - UTS FEIT")
        self.geometry("350x270")
        self.logged_in_student = None
        self.show_login()

    def clear(self):
        for widget in self.winfo_children():
            widget.destroy()

    # 1. Login Window
    def show_login(self):
        self.clear()
        tk.Label(self, text="University App", font=("Arial", 16)).pack(pady=10)
        tk.Label(self, text="Email:").pack()
        email_entry = tk.Entry(self)
        email_entry.pack()
        tk.Label(self, text="Password:").pack()
        password_entry = tk.Entry(self, show="*")
        password_entry.pack()

        def login_action():
            email = email_entry.get().strip()
            password = password_entry.get().strip()
            if not email or not password:
                messagebox.showerror(
                    "Login Error", "All fields must be filled.")
                return
            if not validate_email(email):
                messagebox.showerror(
                    "Login Error", "Email must end with @university.com")
                return
            student = find_student(email, password)
            if student:
                self.logged_in_student = student
                self.show_enrolment()
            else:
                messagebox.showerror(
                    "Login Error", "Incorrect credentials or student not registered.")

        tk.Button(self, text="Login", width=20,
                  command=login_action).pack(pady=7)
        tk.Button(self, text="Register", width=20,
                  command=self.show_register).pack()

    # 2. Registration Window
    def show_register(self):
        self.clear()
        tk.Label(self, text="Student Registration",
                 font=("Arial", 16)).pack(pady=10)
        tk.Label(self, text="Name:").pack()
        name_entry = tk.Entry(self)
        name_entry.pack()
        tk.Label(self, text="Email:").pack()
        email_entry = tk.Entry(self)
        email_entry.pack()
        tk.Label(self, text="Password:").pack()
        password_entry = tk.Entry(self, show="*")
        password_entry.pack()

        def register_action():
            name = name_entry.get().strip()
            email = email_entry.get().strip()
            password = password_entry.get().strip()
            if not name or not email or not password:
                messagebox.showerror("Registration Error",
                                     "All fields must be filled.")
                return
            if not validate_email(email):
                messagebox.showerror("Registration Error",
                                     "Email must end with @university.com")
                return
            if not validate_password(password):
                messagebox.showerror(
                    "Registration Error", "Password must start with an uppercase letter, followed by at least 4 letters, and end with at least 3 digits.")
                return
            students = load_students()
            if any(s.email == email for s in students):
                messagebox.showerror("Registration Error",
                                     "Student already registered.")
                return
            student = Student(name, email, password)
            students.append(student)
            save_students(students)
            messagebox.showinfo(
                "Registered", "Registration successful! You may now log in.")
            self.show_login()

        tk.Button(self, text="Register", width=20,
                  command=register_action).pack(pady=7)
        tk.Button(self, text="Back to Login", width=20,
                  command=self.show_login).pack()

    # 3. Enrolment Window
    def show_enrolment(self):
        self.clear()
        s = self.logged_in_student
        tk.Label(self, text=f"Welcome, {s.name}",
                 font=("Arial", 15)).pack(pady=10)
        tk.Button(self, text="Enrol in New Subject", width=23,
                  command=self.enrol_subject_action).pack(pady=5)
        tk.Button(self, text="View My Subjects", width=23,
                  command=self.show_subjects).pack(pady=5)
        tk.Button(self, text="Logout", width=23,
                  command=self.logout_action).pack(pady=5)

    def enrol_subject_action(self):
        s = self.logged_in_student
        if len(s.enrolled_subjects) >= 4:
            messagebox.showerror(
                "Enrolment Error", "You cannot enrol in more than 4 subjects.")
            return
        subject = s.enrol_subject()
        students = load_students()
        # Update the student in the list and save
        for idx, st in enumerate(students):
            if st.email == s.email:
                students[idx] = s
                break
        save_students(students)
        messagebox.showinfo(
            "Subject Enrolled", f"Subject {subject.subject_id} enrolled with mark {subject.mark} ({subject.grade}).")
        self.show_enrolment()

    # 4. Subjects List Window
    def show_subjects(self):
        self.clear()
        s = self.logged_in_student
        tk.Label(self, text="My Subjects", font=("Arial", 16)).pack(pady=10)
        if not s.enrolled_subjects:
            tk.Label(self, text="You have not enrolled in any subjects yet.").pack()
        else:
            for subj in s.enrolled_subjects:
                tk.Label(
                    self, text=f"Subject ID: {subj.subject_id}, Mark: {subj.mark}, Grade: {subj.grade}").pack()
        tk.Button(self, text="Back", width=20,
                  command=self.show_enrolment).pack(pady=15)

    def logout_action(self):
        self.logged_in_student = None
        self.show_login()


if __name__ == "__main__":
    GUIUniApp().mainloop()
