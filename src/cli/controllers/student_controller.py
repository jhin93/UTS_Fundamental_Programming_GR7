from utils.validators import validate_email, validate_password
from cli.controllers.base import BaseController

class StudentController(BaseController):
    """Student Controller for managing student records. This controller handles the student functionalities such as
    enrolling in subjects, changing password, and viewing enrolment."""
    def __init__(self):
        super().__init__()
        self.logged_in_student = None

    def register(self, name, email, password):
        try:
            self.refresh_db()
            if not validate_email(email):
                return "Invalid email format."

            if not validate_password(password):
                return "Invalid password format."

            if any(s.email == email for s in self.students):
                return "Student already registered."

            student = self.db.create_student(name, email, password)
            print(f"Registered with ID: {student.student_id}")
            return "Registration successful."
        except Exception as e:
            return f"Error during registration: {e}"

    def login(self, email, password):
        try:
            self.refresh_db()
            for student in self.students:
                if student.email == email and student.password == password:
                    self.logged_in_student = student
                    return f"Welcome {student.name}!"
            return "Invalid credentials."
        except Exception as e:
            return f"Login error: {e}"

    def change_password(self, new_password: str):
        try:
            self.refresh_db()
            if not validate_password(new_password):
                return "Invalid password format."
            status = self.logged_in_student.change_password(new_password.strip())
            self.db.save()
            return status
        except Exception as e:
            return f"Error changing password: {e}"

    def enrol_subject(self):
        try:
            self.refresh_db()
            result = self.logged_in_student.enrol_subject()
            self.db.save()
            return result
        except Exception as e:
            return f"Error enrolling subject: {e}"

    def remove_subject(self, subject_id):
        try:
            self.refresh_db()
            result = self.logged_in_student.remove_subject(subject_id)
            self.db.save()
            return result
        except Exception as e:
            return f"Error removing subject: {e}"

    def view_enrolment(self):
        try:
            self.refresh_db()
            return self.logged_in_student.view_enrolment()
        except Exception as e:
            return f"Error viewing enrolment: {e}"

    def logout(self):
        try:
            self.logged_in_student = None
            return "Logged out successfully."
        except Exception as e:
            return f"Logout failed: {e}"
        

