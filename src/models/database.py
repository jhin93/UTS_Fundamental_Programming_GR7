import os
import json
from models.student import Student
from models.admin import Admin

class Database:
    """Database class for managing student records and admin accounts. This class handles the loading and saving of
    student data to a JSON file, as well as the creation of new student records and admin accounts."""
    def __init__(self, file_path='data/students.data'):
        self.file_path = file_path
        self.students = []
        self.admins = [Admin("admin1", "admin1@university.com", "admin1pass"),
                    Admin("admin2", "admin2@university.com", "admin2pass")]
        self.load()

    def load(self):
        if os.path.exists(self.file_path):
            try:
                with open(self.file_path, 'r') as f:
                    data = json.load(f)
                    self.students = [Student.from_dict(d) for d in data.get("students", [])]
            except (json.JSONDecodeError, IOError) as e:
                print(f"Error loading student data: {e}")
                self.students = []  # Reset to empty if file is corrupted
            except Exception as e:
                print(f"Unexpected error while loading data: {e}")
        else:
            print(f"Warning: {self.file_path} does not exist. Starting with empty student list.")

    def save(self):
        try:
            os.makedirs(os.path.dirname(self.file_path), exist_ok=True)
            with open(self.file_path, 'w+') as f:
                data = {
                    "students": [s.to_dict() for s in self.students]
                }
                json.dump(data, f, indent=4)
        except IOError as e:
            print(f"Error saving student data: {e}")
        except Exception as e:
            print(f"Unexpected error while saving data: {e}")

    def create_student(self, name, email, password):
        try:
            student = Student(name, email, password)
            self.students.append(student)
            self.save()
            return student
        except Exception as e:
            print(f"Failed to create student: {e}")
            return None

    def load_admins(self):
        return self.admins
