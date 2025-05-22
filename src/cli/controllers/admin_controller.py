from models.database import Database
from models.admin import Admin

class AdminController:
    def __init__(self):
        self.db = Database()
        self.admins = self.db.load_admins()
        self.students = self.db.students
        self.logged_in_admin = None

    def login(self, email, password):
        for admin in self.admins:
            if admin.email == email and admin.password == password:
                self.logged_in_admin = admin
                return f"Welcome Admin {admin.name}"
        return "Invalid admin credentials."

    def list_students(self):
        if not self.students:
            return "No students found."
        return "\n".join([
            f"{s.student_id} - {s.name}, Avg Mark: {s.average_mark():.2f}"
            for s in self.students
        ])

    def group_by_grade(self):
        grade_groups = {}
        for s in self.students:
            for subj in s.enrolled_subjects:
                grade_groups.setdefault(subj.grade, []).append(s)

        result = []
        for grade, group in grade_groups.items():
            result.append(f"\nGrade {grade}:")
            for student in group:
                result.append(f"{student.student_id} - {student.name}")
        return "\n".join(result) if result else "No subjects found."

    def partition_pass_fail(self):
        pass_students = [s for s in self.students if s.average_mark() >= 50]
        fail_students = [s for s in self.students if s.average_mark() < 50]

        result = ["\nPASS:"]
        result += [f"{s.student_id} - {s.name}" for s in pass_students]
        result.append("\nFAIL:")
        result += [f"{s.student_id} - {s.name}" for s in fail_students]
        return "\n".join(result)

    def remove_student(self, student_id):
        initial_count = len(self.students)
        self.students = [s for s in self.students if s.student_id != student_id]
        self.db.students = self.students
        self.db.save()
        if len(self.students) < initial_count:
            return "Student removed."
        return "Student not found."

    def clear_students(self):
        self.students = []
        self.db.students = []
        self.db.save()
        return "All student records cleared."

    def logout(self):
        self.logged_in_admin = None
        return "Logged out successfully."

