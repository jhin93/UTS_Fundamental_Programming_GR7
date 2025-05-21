import unittest
from main import Student


class Student:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password


def handle_login(email, password, students):
    if not email or not password or not email.endswith("@university.com"):
        return False, "All fields must be filled and Email should end with @university.com."

    if any(s.email == email and s.password == password for s in students):
        return True, "Login successful"
    return False, "Invalid credentials"


class TestLogin(unittest.TestCase):

    def setUp(self):
        self.students = [
            Student("student1", "student1@university.com", "Student123"),
            Student("student2", "student2@university.com", "Studenet123")
        ]

    def test_valid_login(self):
        result, _ = handle_login(
            "student1@university.com", "Student123", self.students)
        self.assertIs(result, True)

    def test_blank_password(self):
        result, _ = handle_login("student1@university.com", "", self.students)
        self.assertIs(result, False)

    def test_invalid_email_format(self):
        result, _ = handle_login(
            "Student1@gmail.com", "Student123", self.students)
        self.assertIs(result, False)

    def test_blank_email(self):
        result, _ = handle_login("", "Student123", self.students)
        self.assertIs(result, False)

    def test_wrong_password(self):
        result, _ = handle_login(
            "student1@university.com", "WrongPass", self.students)
        self.assertIs(result, False)


if __name__ == "__main__":
    unittest.main()

