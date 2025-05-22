from models.database import Database
from utils.validators import validate_email, validate_password

class StudentController:
    def __init__(self):
        self.db = Database()
        self.students = self.db.students
        self.logged_in_student = None

    def register(self, name, email, password):
        if not validate_email(email):
            return "Invalid email format."

        if not validate_password(password):
            # print("Invalid password format.")
            return "Invalid password format."

        if any(s.email == email for s in self.students):
            return "Student already registered."

        student = self.db.create_student(name, email, password)
        print(f"Registered with ID: {student.student_id}")
        return True

    def login(self, email, password):
        for student in self.students:
            if student.email == email and student.password == password:
                self.logged_in_student = student
                return f"Welcome {student.name}!"
        return "Invalid credentials."

    def change_password(self, new_password: str):
        if not validate_password(new_password):
            return "Invalid password format."
        status = self.logged_in_student.change_password(new_password.strip())
        self.db.save()
        return status

    def enrol_subject(self):
        result = self.logged_in_student.enrol_subject()
        self.db.save()
        return result

    def remove_subject(self, subject_id):
        self.logged_in_student.remove_subject(subject_id)
        self.db.save()
        return f"Subject {subject_id} removed."

    def view_enrolment(self):
        return self.logged_in_student.view_enrolment()

    def logout(self):
        self.logged_in_student = None

