import tkinter as tk
from tkinter import messagebox
import pickle
import os
from models import Student, Subject, load_students, save_students

DATA_FILE = 'students.data'

# -------------------- GUI Helper --------------------
def get_student_by_email(email, password):
    students = load_students()
    for student in students:
        if student.email == email and student.password == password:
            return student, students
    return None, students

# -------------------- Windows --------------------
class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("GUIUniApp - Login")

        tk.Label(root, text="Email:").pack()
        self.email_entry = tk.Entry(root)
        self.email_entry.pack()

        tk.Label(root, text="Password:").pack()
        self.pass_entry = tk.Entry(root, show="*")
        self.pass_entry.pack()

        tk.Button(root, text="Login", command=self.login).pack(pady=5)

    def login(self):
        email = self.email_entry.get()
        password = self.pass_entry.get()
        if not email or not password:
            messagebox.showerror("Error", "Fields cannot be empty")
            return

        student, students = get_student_by_email(email, password)
        if student:
            self.root.destroy()
            root = tk.Tk()
            EnrolmentWindow(root, student, students)
            root.mainloop()
        else:
            messagebox.showerror("Error", "Invalid credentials")

class EnrolmentWindow:
    def __init__(self, root, student, all_students):
        self.root = root
        self.student = student
        self.all_students = all_students
        self.root.title("Enrolment Window")

        tk.Button(root, text="Enrol Subject", command=self.enrol_subject).pack()
        tk.Button(root, text="View Subjects", command=self.view_subjects).pack()
        tk.Button(root, text="Exit", command=self.save_and_exit).pack(pady=10)

    def enrol_subject(self):
        if len(self.student.enrolled_subjects) >= 4:
            messagebox.showerror("Error", "Cannot enrol in more than 4 subjects")
            return
        subject = Subject()
        self.student.enrolled_subjects.append(subject)
        messagebox.showinfo("Success", f"Enrolled in Subject {subject.subject_id} with Mark {subject.mark} ({subject.grade})")

    def view_subjects(self):
        self.root.destroy()
        root = tk.Tk()
        SubjectWindow(root, self.student, self.all_students)
        root.mainloop()

    def save_and_exit(self):
        for i, s in enumerate(self.all_students):
            if s.email == self.student.email:
                self.all_students[i] = self.student
        save_students(self.all_students)
        self.root.destroy()

class SubjectWindow:
    def __init__(self, root, student, all_students):
        self.root = root
        self.root.title("Subject List")

        for subj in student.enrolled_subjects:
            tk.Label(root, text=f"ID: {subj.subject_id}, Mark: {subj.mark}, Grade: {subj.grade}").pack()

        tk.Button(root, text="Back", command=self.back).pack(pady=10)
        self.student = student
        self.all_students = all_students

    def back(self):
        self.root.destroy()
        root = tk.Tk()
        EnrolmentWindow(root, self.student, self.all_students)
        root.mainloop()

# -------------------- Main Launcher --------------------
if __name__ == '__main__':
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'wb') as f:
            pickle.dump([], f)

    root = tk.Tk()
    LoginWindow(root)
    root.mainloop()
