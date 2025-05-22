from cli.controllers.student_controller import StudentController
from cli.views.base import BaseView
class StudentView(BaseView):
    """Student View for managing student records. This class handles the registration and login of students,
    as well as their dashboard functionalities."""
    def __init__(self):
        self.controller = StudentController()

    def show_menu(self):
        """Display the main menu for students, allowing them to register or login."""
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
        """Handle the registration process for students. This includes input validation and retry options."""
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
        """Handle the login process for students. This includes input validation and retry options."""
        email = input("Email: ")
        password = input("Password: ")
        result = self.controller.login(email, password)
        print(result)
        if "Welcome" in result:
            self.dashboard()

    def dashboard(self):
        """Display the dashboard menu for logged-in students. This includes options to change password, enrol in subjects,
        remove subjects, view enrolment, and logout."""
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
