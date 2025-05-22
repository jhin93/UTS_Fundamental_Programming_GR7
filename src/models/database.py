import os
import json
from models.student import Student
from models.admin import Admin

class Database:
    def __init__(self, file_path='data/students.data'):
        self.file_path = file_path
        self.students = []
        self.admins = [Admin("admin1", "admin1@university.com", "admin1pass"),
                       Admin("admin2", "admin2@university.com", "admin2pass")]
        self.load()

    def load(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as f:
                data = json.load(f)
                self.students = [Student.from_dict(d) for d in data.get("students", [])]

    def save(self):
        with open(self.file_path, 'w+') as f:
            data = {
                "students": [s.to_dict() for s in self.students],
                # "admins": [a.to_dict() for a in self.admins]
            }
            json.dump(data, f, indent=4)

    def create_student(self, name, email, password):
        student = Student(name, email, password)
        self.students.append(student)
        self.save()
        return student

    def load_admins(self):
        return self.admins
