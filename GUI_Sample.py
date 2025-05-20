import tkinter as tk
from tkinter import simpledialog, messagebox
import csv
import random
import os
import re

DATA_FILE = 'students.csv'

# ---------- CSV Functions ----------
def load_students():
    students = []
    if not os.path.exists(DATA_FILE):
        return students
    with open(DATA_FILE, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            student = dict(row)
            # Decode enrolled_subjects
            enrolled = []
            if student['enrolled_subjects']:
                for subj in student['enrolled_subjects'].split('|'):
                    sid, mark, grade = subj.split(',')
                    enrolled.append({'subject_id': sid, 'mark': int(mark), 'grade': grade})
            student['enrolled_subjects'] = enrolled
            students.append(student)
    return students

def save_students(students):
    with open(DATA_FILE, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['student_id', 'name', 'email', 'password', 'enrolled_subjects']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for s in students:
            # Encode enrolled_subjects
            enrolled = '|'.join(f"{sub['subject_id']},{sub['mark']},{sub['grade']}" for sub in s['enrolled_subjects'])
            data = s.copy()
            data['enrolled_subjects'] = enrolled
            writer.writerow(data)

def find_student(email, password=None):
    students = load_students()
    for s in students:
        if s['email'] == email and (password is None or s['password'] == password):
            return s
    return None

def validate_email(email):
    return email.endswith('@university.com')

def validate_password(password):
    return re.match(r'^[A-Z][a-zA-Z]{4,}\d{3,}$', password)

def calc_grade(mark):
    mark = int(mark)
    if mark >= 85:
        return 'HD'
    elif mark >= 75:
        return 'D'
    elif mark >= 65:
        return 'C'
    elif mark >= 50:
        return 'P'
    else:
        return 'F'

def average_mark(student):
    enrolled = student['enrolled_subjects']
    if not enrolled:
        return 0
    return sum(sub['mark'] for sub in enrolled) / len(enrolled)

# ---------- Main GUI ----------
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("University Student App")
        self.geometry("400x300")
        self.show_main_menu()

    def show_main_menu(self):
        self.clear()
        tk.Label(self, text="University App", font=("Arial", 16)).pack(pady=10)
        tk.Button(self, text="Student", width=20, command=self.student_menu).pack(pady=10)
        tk.Button(self, text="Exit", width=20, command=self.quit).pack(pady=10)

    def clear(self):
        for widget in self.winfo_children():
            widget.destroy()

    def student_menu(self):
        self.clear()
        tk.Label(self, text="Student Menu", font=("Arial", 14)).pack(pady=10)
        tk.Button(self, text="Register", width=20, command=self.register_window).pack(pady=5)
        tk.Button(self, text="Login", width=20, command=self.login_window).pack(pady=5)
        tk.Button(self, text="Back", width=20, command=self.show_main_menu).pack(pady=5)

    def register_window(self):
        def submit():
            name = name_entry.get()
            email = email_entry.get()
            password = password_entry.get()
            if not validate_email(email):
                messagebox.showerror("Error", "Email must end with @university.com")
                return
            if not validate_password(password):
                messagebox.showerror("Error", "Invalid password format.\nMust start with an uppercase letter, followed by at least 4 letters, and end with at least 3 digits.")
                return
            students = load_students()
            if any(s['email'] == email for s in students):
                messagebox.showerror("Error", "Student already registered.")
                return
            student_id = f"{random.randint(1, 999999):06}"
            students.append({
                'student_id': student_id,
                'name': name,
                'email': email,
                'password': password,
                'enrolled_subjects': []
            })
            save_students(students)
            messagebox.showinfo("Success", f"Registered with ID: {student_id}")
            win.destroy()

        win = tk.Toplevel(self)
        win.title("Register")
        tk.Label(win, text="Name").pack()
        name_entry = tk.Entry(win)
        name_entry.pack()
        tk.Label(win, text="Email").pack()
        email_entry = tk.Entry(win)
        email_entry.pack()
        tk.Label(win, text="Password").pack()
        password_entry = tk.Entry(win, show="*")
        password_entry.pack()
        tk.Button(win, text="Register", command=submit).pack(pady=5)

    def login_window(self):
        def submit():
            email = email_entry.get()
            password = password_entry.get()
            student = find_student(email, password)
            if student:
                win.destroy()
                self.student_dashboard(student)
            else:
                messagebox.showerror("Error", "Invalid credentials.")

        win = tk.Toplevel(self)
        win.title("Login")
        tk.Label(win, text="Email").pack()
        email_entry = tk.Entry(win)
        email_entry.pack()
        tk.Label(win, text="Password").pack()
        password_entry = tk.Entry(win, show="*")
        password_entry.pack()
        tk.Button(win, text="Login", command=submit).pack(pady=5)

    def student_dashboard(self, student):
        self.clear()
        tk.Label(self, text=f"Welcome {student['name']}", font=("Arial", 14)).pack(pady=10)

        def change_password():
            new_pass = simpledialog.askstring("Change Password", "Enter new password:", show="*")
            if not new_pass:
                return
            if new_pass == student['password']:
                messagebox.showerror("Error", "New password cannot be the same as the old password.")
            elif not validate_password(new_pass):
                messagebox.showerror("Error", "Invalid password format.")
            else:
                student['password'] = new_pass
                students = load_students()
                for s in students:
                    if s['student_id'] == student['student_id']:
                        s['password'] = new_pass
                        break
                save_students(students)
                messagebox.showinfo("Success", "Password changed successfully.")

        def enrol_subject():
            if len(student['enrolled_subjects']) >= 4:
                messagebox.showwarning("Limit", "Cannot enrol more than 4 subjects.")
                return
            subj_id = f"{random.randint(1, 999):03}"
            mark = random.randint(25, 100)
            grade = calc_grade(mark)
            student['enrolled_subjects'].append({'subject_id': subj_id, 'mark': mark, 'grade': grade})
            students = load_students()
            for s in students:
                if s['student_id'] == student['student_id']:
                    s['enrolled_subjects'] = student['enrolled_subjects']
                    break
            save_students(students)
            messagebox.showinfo("Success", f"Subject {subj_id} enrolled with mark {mark} ({grade})")
            show_subjects()

        def remove_subject():
            sid = simpledialog.askstring("Remove Subject", "Enter Subject ID to remove:")
            if not sid:
                return
            before = len(student['enrolled_subjects'])
            student['enrolled_subjects'] = [sub for sub in student['enrolled_subjects'] if sub['subject_id'] != sid]
            after = len(student['enrolled_subjects'])
            if after < before:
                students = load_students()
                for s in students:
                    if s['student_id'] == student['student_id']:
                        s['enrolled_subjects'] = student['enrolled_subjects']
                        break
                save_students(students)
                messagebox.showinfo("Removed", f"Subject {sid} removed.")
                show_subjects()
            else:
                messagebox.showwarning("Not Found", "Subject not found.")

        def show_subjects():
            subjects_text.delete('1.0', tk.END)
            enrolled = student['enrolled_subjects']
            if not enrolled:
                subjects_text.insert(tk.END, "No subjects enrolled yet.\n")
            else:
                for subj in enrolled:
                    subjects_text.insert(tk.END, f"Subject ID: {subj['subject_id']}, Mark: {subj['mark']}, Grade: {subj['grade']}\n")
                subjects_text.insert(tk.END, f"\nAverage Mark: {average_mark(student):.2f}")

        tk.Button(self, text="Change Password", width=20, command=change_password).pack(pady=3)
        tk.Button(self, text="Enrol Subject", width=20, command=enrol_subject).pack(pady=3)
        tk.Button(self, text="Remove Subject", width=20, command=remove_subject).pack(pady=3)
        tk.Button(self, text="Show Subjects", width=20, command=show_subjects).pack(pady=3)
        tk.Button(self, text="Logout", width=20, command=self.show_main_menu).pack(pady=10)

        subjects_text = tk.Text(self, width=40, height=8)
        subjects_text.pack(pady=10)
        show_subjects()

if __name__ == "__main__":
    App().mainloop()
