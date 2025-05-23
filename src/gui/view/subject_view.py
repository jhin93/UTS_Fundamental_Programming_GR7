import tkinter as tk
from tkinter import messagebox
from .login_view import load_students, save_students
from models.student import Student

class SubjectView:
    def __init__(self, parent, student, back_callback):
        self.parent = parent
        self.student = student
        self.back_callback = back_callback
        self.setup_ui()

    def setup_ui(self):
        self.clear()
        tk.Label(self.parent, text="My Subjects", font=("Arial", 16)).pack(pady=10)
        if not self.student.enrolled_subjects:
            tk.Label(self.parent, text="You have not enrolled in any subjects yet.").pack()
        else:
            for subj in self.student.enrolled_subjects:
                frame = tk.Frame(self.parent)
                frame.pack(pady=5)
                tk.Label(frame, text=f"Subject ID: {subj.subject_id}, Mark: {subj.mark}, Grade: {subj.grade}").pack(side=tk.LEFT)
                tk.Button(frame, text="Remove", command=lambda s=subj: self.remove_subject(s)).pack(side=tk.LEFT, padx=5)
        tk.Button(self.parent, text="Back", width=20, command=self.go_back).pack(pady=15)

    def clear(self):
        for widget in self.parent.winfo_children():
            widget.destroy()

    def remove_subject(self, subject):
        result = self.student.remove_subject(subject.subject_id)
        if "removed" in result:
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
            messagebox.showinfo("Subject Removed", f"Subject {subject.subject_id} has been removed.")
            self.setup_ui()
        else:
            messagebox.showerror("Error", "Failed to remove subject.")

    def go_back(self):
        self.back_callback(self.student) 