import random
from models.subject import Subject

class Student:
    def __init__(self, name, email, password):
        self.student_id = f"{random.randint(1, 999999):06}"
        self.name = name
        self.email = email
        self.password = password
        self.enrolled_subjects = []

    def enrol_subject(self):
        if len(self.enrolled_subjects) < 4:
            subject = Subject()
            self.enrolled_subjects.append(subject)
            return subject
        else:
            return None

    def remove_subject(self, subject_id):
        before = len(self.enrolled_subjects)
        self.enrolled_subjects = [s for s in self.enrolled_subjects if s.subject_id != subject_id]
        return len(self.enrolled_subjects) < before 