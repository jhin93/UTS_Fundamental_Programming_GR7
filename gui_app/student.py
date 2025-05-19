import pickle
import os

StudentData_File = "students.data"


class Student:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.enrolled_subjects = []


def load_students():
    if not os.path.exists(StudentData_File):
        return []

    with open(StudentData_File, "rb") as file:
        return pickle.load(file)


def save_students(students):
    with open(StudentData_File, "wb") as file:
        pickle.dump(students, file)
