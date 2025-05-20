from models.student import load_students
from utils.validators import validate_login

def handle_login(email, password):
    if not validate_login(email, password):
        return False, "Email and password cannot be empty."

    students = load_students()
    for student in students:
        if student.email == email and student.password == password:
            return True, "Successfully logged in"
    return False, "wrong credentials"
