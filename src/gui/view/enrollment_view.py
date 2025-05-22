import tkinter as tk
from tkinter import messagebox
from .login_view import load_students, save_students
from models.student import Student

class EnrollmentView:
    def __init__(self, parent, student, show_subjects_callback, logout_callback):
        self.parent = parent
        self.student = student
        self.show_subjects_callback = show_subjects_callback
        self.logout_callback = logout_callback
        self.setup_ui()

    def setup_ui(self):
        self.clear()
        tk.Label(self.parent, text=f"Welcome, {self.student.name}", font=("Arial", 15)).pack(pady=10)
        tk.Button(self.parent, text="Enrol in New Subject", width=23, command=self.enrol_subject_action).pack(pady=5)
        tk.Button(self.parent, text="View Subjects", width=23, command=self.view_subjects).pack(pady=5)
        tk.Button(self.parent, text="Logout", width=23, command=self.logout_callback).pack(pady=5)

    def clear(self):
        for widget in self.parent.winfo_children():
            widget.destroy()

    def enrol_subject_action(self):
        if len(self.student.enrolled_subjects) >= 4:
            messagebox.showerror("Enrolment Error", "You cannot enrol in more than 4 subjects.")
            return
        subject = self.student.enrol_subject()
        students_data = load_students()
        # Convert dictionary data to Student objects
        students = [Student.from_dict(st) for st in students_data]
        # Update the student in the list and save
        for idx, st in enumerate(students):
            if st.email == self.student.email:
                students[idx] = self.student
                break
        # Save the updated data
        save_students(students)
        messagebox.showinfo("Subject Enrolled", f"Subject {subject.subject_id} enrolled with mark {subject.mark} ({subject.grade}).")
        self.setup_ui()

    def view_subjects(self):
        self.show_subjects_callback(self.student) 