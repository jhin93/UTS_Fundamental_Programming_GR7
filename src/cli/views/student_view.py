from cli.controllers.student_controller import StudentController
from cli.views.base import BaseView
class StudentView(BaseView):
    def __init__(self):
        self.controller = StudentController()

    def show_menu(self):
        while True:
            print("\nStudent Menu:\n(r) Register\n(l) Login\n(x) Exit")
            choice = input("Choose: ").lower()
            if choice == 'r':
                self.handle_register()
            elif choice == 'l':
                self.handle_login()
            elif choice == 'x':
                break
            else:
                print("Invalid option.")

    def handle_register(self):
        print("(i) Password starts with an upper-case character\n (ii) Password contains at least five (5) letters\n (iii) Password ends with three (3) or more digits")
        while True:
            name = input("Enter name: ")
            email = input("Enter email: ")
            password = input("Enter password: ")
            result = self.controller.register(name, email, password)
            print(result)
            if result == "Registration successful.":
                break
            else:
                try_again = self.retry()
                if not try_again:
                    break
                
    def handle_login(self):
        email = input("Email: ")
        password = input("Password: ")
        result = self.controller.login(email, password)
        print(result)
        if "Welcome" in result:
            self.dashboard()

    def dashboard(self):
        while self.controller.logged_in_student:
            print("\n(c) Change password\n(e) Enrol\n(r) Remove subject\n(s) Show subjects\n(x) Logout")
            choice = input("Choose: ").lower()

            if choice == 'c':
                new_password = input("New password: ")
                confirm_password = input("Confirm new password: ")
                if new_password != confirm_password:
                    print("Passwords do not match. Try again.")
                    continue
                print(self.controller.change_password(new_password))
            elif choice == 'e':
                print(self.controller.enrol_subject())
            elif choice == 'r':
                sid = input("Enter subject ID to remove: ")
                print(self.controller.remove_subject(sid))
            elif choice == 's':
                print(self.controller.view_enrolment())
            elif choice == 'x':
                self.controller.logout()
                print("Logged out.")
            else:
                print("Invalid option.")
