from cli.controllers.base import BaseController

class AdminController(BaseController):
    """Admin Controller for managing student records. This controller handles the admin functionalities such as
    listing students, grouping by grade, partitioning pass/fail, removing students, and clearing all student records."""
    def __init__(self):
        super().__init__()
        self.admins = self.db.load_admins()
        self.logged_in_admin = None

    def login(self, email, password):
        try:
            for admin in self.admins:
                if admin.email == email and admin.password == password:
                    self.logged_in_admin = admin
                    return f"Welcome Admin {admin.name}"
            return "Invalid admin credentials."
        except Exception as e:
            return f"Login failed due to unexpected error: {e}"


    def list_students(self):
        try:
            self.refresh_db()
            if not self.students:
                return "No students found."
            return "\n".join([
                f"{s.student_id} - {s.name}, Avg Mark: {s.average_mark():.2f}"
                for s in self.students
            ])
        except Exception as e:
            return f"Error listing students: {e}"

    def group_by_grade(self):
        try:
            self.refresh_db()
            grade_groups = {}

            for student in self.students:
                for subj in getattr(student, 'enrolled_subjects', []):
                    grade_groups.setdefault(subj.grade, []).append((student, subj))

            if not grade_groups:
                return "No subjects found."

            result = []
            for grade, records in grade_groups.items():
                result.append(f"\nGrade {grade}:")
                for student, subject in records:
                    result.append(
                        f"Subject ID {subject.subject_id} - Student ID {student.student_id} - {student.name}"
                    )
            return "\n".join(result)
        except Exception as e:
            return f"Error grouping by grade: {e}"

    def partition_pass_fail(self):
        try:
            self.refresh_db()
            pass_students = [s for s in self.students if s.average_mark() >= 50]
            fail_students = [s for s in self.students if s.average_mark() < 50]

            result = ["\nPASS:"]
            result += [f"{s.student_id} - {s.name}" for s in pass_students]
            result.append("\nFAIL:")
            result += [f"{s.student_id} - {s.name}" for s in fail_students]
            return "\n".join(result)
        except Exception as e:
            return f"Error partitioning pass/fail: {e}"

    def remove_student(self, student_id):
        try:
            self.refresh_db()
            initial_count = len(self.students)
            self.students = [s for s in self.students if s.student_id != student_id]
            self.db.students = self.students
            self.db.save()
            if len(self.students) < initial_count:
                return "Student removed."
            return "Student not found."
        except Exception as e:
            return f"Error removing student: {e}"

    def clear_students(self):
        try:
            self.refresh_db()
            self.students = []
            self.db.students = []
            self.db.save()
            return "All student records cleared."
        except Exception as e:
            return f"Error clearing students: {e}"

    def logout(self):
        try:
            self.logged_in_admin = None
            return "Logged out successfully."
        except Exception as e:
            return f"Logout failed: {e}"

