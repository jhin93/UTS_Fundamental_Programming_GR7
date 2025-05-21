import unittest
import os
import pickle


from student import Student


class TestStudentData(unittest.TestCase):

    def test_file_exists(self):
        self.assertEqual(os.path.exists("students.data"),
                         True, "students.data file not found")

    def test_data_has_students(self):
        with open("students.data", "rb") as f:
            students = pickle.load(f)
        self.assertGreater(len(students), 0, " No students in the file")
        self.assertIsInstance(
            students[0], Student, " Data is not of type Student")

    def test_has_admin_user(self):
        with open("students.data", "rb") as f:
            students = pickle.load(f)
        emails = [s.email for s in students]
        self.assertIn("admin@university.com", emails,
                      " admin@university.com not found")


if __name__ == "__main__":
    unittest.main()
