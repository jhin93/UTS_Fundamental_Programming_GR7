import random
class User:
    """ A simple base class for all users."""
    def __init__(self, name: str, email: str, password: str):
        self.name = name
        self.email = email
        self.password = password
    
    def __studentID_generator(self):
        return self.email.split('@')[0] + str(random.randint(1000, 9999))
    
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
        
    
    