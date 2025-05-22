from cli.controllers.admin_controller import AdminController
from cli.views.base import BaseView

class AdminView(BaseView):
    def __init__(self):
        self.controller = AdminController()

    def show_menu(self):
        email = input("Email: ")
        password = input("Password: ")
        login_result = self.controller.login(email, password)
        print(login_result)
        if "Welcome" in login_result:
            self.dashboard()

    def dashboard(self):
        while self.controller.logged_in_admin:
            print("Admin Menu:\n(s) Show all students\n(g) Group by grade\n(p) Partition Pass/Fail\n(r) Remove student\n(c) Clear all students\n(x) Logout\n")
            choice = input("Choose: \n").lower()
            if choice == 's':
                print(self.controller.list_students())
            elif choice == 'g':
                print(self.controller.group_by_grade())
            elif choice == 'p':
                print(self.controller.partition_pass_fail())
            elif choice == 'r':
                sid = input("Enter student ID to remove: ")
                print(self.controller.remove_student(sid))
            elif choice == 'c':
                print(self.controller.clear_students())
            elif choice == 'x':
                self.controller.logout()
                print("Logged out.")
            else:
                print("Invalid option.")