import tkinter as tk

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
                tk.Label(self.parent, text=f"Subject ID: {subj.subject_id}, Mark: {subj.mark}, Grade: {subj.grade}").pack()
        tk.Button(self.parent, text="Back", width=20, command=self.go_back).pack(pady=15)

    def clear(self):
        for widget in self.parent.winfo_children():
            widget.destroy()

    def go_back(self):
        self.back_callback(self.student) 