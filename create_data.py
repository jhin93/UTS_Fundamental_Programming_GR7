
import pickle
from student import Student

students = [
    Student("student1@gmail.com", "password1"),
    Student("student2@gmail.com", "password2")
]

with open("students.data", "wb") as f:
    pickle.dump(students, f)

print("student data is created")
