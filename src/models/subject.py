import random

class Subject:
    """Subject class representing a subject in the system. This model class is used to manage the subject's
    information such as subject ID, mark, and grade. It also provides methods to convert the subject object"""
    def __init__(self, subject_id=None, mark=None):
        self.subject_id = subject_id or f"{random.randint(1, 999):03}"
        self.mark = mark if mark is not None else random.randint(25, 100)
        self.grade = self.calculate_grade()

    def calculate_grade(self):
        if self.mark >= 85:
            return 'HD'
        elif self.mark >= 75:
            return 'D'
        elif self.mark >= 65:
            return 'C'
        elif self.mark >= 50:
            return 'P'
        else:
            return 'F'

    def to_dict(self):
        return {
            "subject_id": self.subject_id,
            "mark": self.mark,
            "grade": self.grade
        }

    @staticmethod
    def from_dict(data):
        return Subject(
            subject_id=data.get("subject_id"),
            mark=data.get("mark")
        )
