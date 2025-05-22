import random
from models.subject import Subject

class Student:
    """Student class representing a student in the system. This class handles the student's personal information,
    enrolled subjects"""
    def __init__(self, name, email, password, student_id=None, enrolled_subjects=None):
        self.student_id = student_id or f"{random.randint(1, 999999):06}"
        self.name = name
        self.email = email
        self.password = password
        self.enrolled_subjects = [
            Subject.from_dict(s) for s in enrolled_subjects
        ] if enrolled_subjects else []

    def enrol_subject(self):
        if len(self.enrolled_subjects) >= 4:
            return "Cannot enrol in more than 4 subjects."
        subject = Subject()
        self.enrolled_subjects.append(subject)
        return f"Subject {subject.subject_id} enrolled with mark {subject.mark} ({subject.grade})"

    def remove_subject(self, subject_id):
        before = len(self.enrolled_subjects)
        self.enrolled_subjects = [
            s for s in self.enrolled_subjects if s.subject_id != subject_id
        ]
        if len(self.enrolled_subjects) < before:
            return f"Subject {subject_id} removed."
        return "Subject not found."

    def change_password(self, new_password):
        if self.password == new_password:
            return "New password cannot be the same as the old one."
        self.password = new_password
        return "Password changed successfully."

    def view_enrolment(self):
        if not self.enrolled_subjects:
            return "No subjects enrolled."
        return "\n".join([
            f"Subject ID: {s.subject_id}, Mark: {s.mark}, Grade: {s.grade}"
            for s in self.enrolled_subjects
        ])

    def average_mark(self):
        if not self.enrolled_subjects:
            return 0
        return sum(s.mark for s in self.enrolled_subjects) / len(self.enrolled_subjects)

    def to_dict(self):
        return {
            "student_id": self.student_id,
            "name": self.name,
            "email": self.email,
            "password": self.password,
            "enrolled_subjects": [s.to_dict() for s in self.enrolled_subjects]
        }

    @staticmethod
    def from_dict(data):
        return Student(
            name=data["name"],
            email=data["email"],
            password=data["password"],
            student_id=data["student_id"],
            enrolled_subjects=data.get("enrolled_subjects", [])
        )
