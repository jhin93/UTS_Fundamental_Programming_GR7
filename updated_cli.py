import os
import pickle
import random
import re
from typing import List

DATA_FILE = 'students.data'

# -------------------- Models --------------------
class Subject:
    def __init__(self):
        self.subject_id = f"{random.randint(1, 999):03}"
        self.mark = random.randint(25, 100)
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

class Student:
    def __init__(self, name, email, password):
        self.student_id = f"{random.randint(1, 999999):06}"
        self.name = name
        self.email = email
        self.password = password
        self.enrolled_subjects: List[Subject] = []

    def enrol_subject(self):
        if len(self.enrolled_subjects) < 4:
            subject = Subject()
            self.enrolled_subjects.append(subject)
            print(f"Subject {subject.subject_id} enrolled with mark {subject.mark} ({subject.grade})")
        else:
            print("Cannot enrol more than 4 subjects.")

    def remove_subject(self, subject_id):
        self.enrolled_subjects = [s for s in self.enrolled_subjects if s.subject_id != subject_id]

    def change_password(self, new_password):
        self.password = new_password

    def view_enrolment(self):
        for subj in self.enrolled_subjects:
            print(f"Subject ID: {subj.subject_id}, Mark: {subj.mark}, Grade: {subj.grade}")

    def average_mark(self):
        if not self.enrolled_subjects:
            return 0
        return sum(s.mark for s in self.enrolled_subjects) / len(self.enrolled_subjects)

# -------------------- Database --------------------
def load_students():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'rb') as f:
        return pickle.load(f)

def save_students(students):
    with open(DATA_FILE, 'wb') as f:
        pickle.dump(students, f)

# -------------------- Validators --------------------
def validate_email(email):
    return email.endswith('@university.com')

def validate_password(password):
    return re.match(r'^[A-Z][a-zA-Z]{4,}\d{3,}$', password)

# -------------------- CLI Controller --------------------
def register():
    name = input("Enter name: ")
    email = input("Enter email: ")
    password = input("Enter password: ")

    if not validate_email(email):
        print("Invalid email format.")
        return
    if not validate_password(password):
        print("Invalid password format.")
        return

    students = load_students()
    if any(s.email == email for s in students):
        print("Student already registered.")
        return

    new_student = Student(name, email, password)
    students.append(new_student)
    save_students(students)
    print(f"Registered with ID: {new_student.student_id}")

def login():
    email = input("Email: ")
    password = input("Password: ")

    students = load_students()
    for s in students:
        if s.email == email and s.password == password:
            print(f"Welcome {s.name}!\n")
            student_menu(s, students)
            return
    print("Invalid credentials.")

def student_menu(student, all_students):
    while True:
        print("\n(c) Change password\n(e) Enrol\n(r) Remove\n(s) Show subjects\n(x) Exit")
        choice = input("Choose: ").lower()
        if choice == 'c':
            new_pass = input("New password: ")
            if validate_password(new_pass):
                student.change_password(new_pass)
                print("Password changed.")
            else:
                print("Invalid format.")
        elif choice == 'e':
            student.enrol_subject()
        elif choice == 'r':
            sid = input("Enter subject ID to remove: ")
            student.remove_subject(sid)
        elif choice == 's':
            student.view_enrolment()
        elif choice == 'x':
            save_students(all_students)
            break
        else:
            print("Invalid option.")

def admin_menu():
    while True:
        print("\nAdmin Menu:\n(s) Show all students\n(g) Group by grade\n(p) Partition Pass/Fail\n(r) Remove student\n(c) Clear all students\n(x) Exit")
        choice = input("Choose: ").lower()
        students = load_students()
        if choice == 's':
            for s in students:
                print(f"{s.student_id} - {s.name}, Avg Mark: {s.average_mark():.2f}")
        elif choice == 'g':
            grade_groups = {}
            for s in students:
                for subj in s.enrolled_subjects:
                    grade_groups.setdefault(subj.grade, []).append(s)
            for grade, group in grade_groups.items():
                print(f"\nGrade {grade}:")
                for student in group:
                    print(f"{student.student_id} - {student.name}")
        elif choice == 'p':
            pass_students = [s for s in students if s.average_mark() >= 50]
            fail_students = [s for s in students if s.average_mark() < 50]
            print("\nPASS:")
            for s in pass_students:
                print(f"{s.student_id} - {s.name}")
            print("\nFAIL:")
            for s in fail_students:
                print(f"{s.student_id} - {s.name}")
        elif choice == 'r':
            sid = input("Enter student ID to remove: ")
            students = [s for s in students if s.student_id != sid]
            save_students(students)
            print("Student removed.")
        elif choice == 'c':
            save_students([])
            print("All student records cleared.")
        elif choice == 'x':
            break
        else:
            print("Invalid option.")

# -------------------- Main CLI --------------------
def main():
    while True:
        print("\nUniversity Menu:\n(A) Admin\n(S) Student\n(X) Exit")
        user_type = input("Select option: ").lower()
        if user_type == 's':
            print("\nStudent Menu:\n(r) Register\n(l) Login\n(x) Exit")
            choice = input("Choose: ").lower()
            if choice == 'r':
                register()
            elif choice == 'l':
                login()
            elif choice == 'x':
                continue
        elif user_type == 'a':
            admin_menu()
        elif user_type == 'x':
            break
        else:
            print("Invalid option.")

if __name__ == '__main__':
    main()
