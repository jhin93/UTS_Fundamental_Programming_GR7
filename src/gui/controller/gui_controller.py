import tkinter as tk
from gui.view.login_view import LoginView
from gui.view.enrollment_view import EnrollmentView
from gui.view.subject_view import SubjectView

class GUIController(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("GUIUniApp - UTS FEIT")
        self.geometry("350x270")
        self.logged_in_student = None
        self.show_login()

    def show_login(self):
        self.logged_in_student = None
        LoginView(self, self.show_enrolment)

    def show_enrolment(self, student):
        self.logged_in_student = student
        EnrollmentView(self, student, self.show_subjects, self.show_login)

    def show_subjects(self, student):
        SubjectView(self, student, self.show_enrolment) 