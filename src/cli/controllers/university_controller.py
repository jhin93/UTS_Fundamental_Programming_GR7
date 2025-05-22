# def load_students():
#     if not os.path.exists(DATA_FILE):
#         return []
#     with open(DATA_FILE, 'rb') as f:
#         return pickle.load(f)
    
# def register():
#     name = input("Enter name: ")
#     email = input("Enter email: ")
#     password = input("Enter password: ")

#     if not validate_email(email):
#         print("Invalid email format.")
#         return
#     if not validate_password(password):
#         print("Invalid password format.")
#         return

#     students = load_students()
#     if any(s.email == email for s in students):
#         print("Student already registered.")
#         return

#     new_student = Student(name, email, password)
#     students.append(new_student)
#     save_students(students)
#     print(f"Registered with ID: {new_student.student_id}")