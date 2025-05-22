from cli.controllers.admin_controller import AdminController

class AdminView:
    def __init__(self):
        self.controller = AdminController()

    def show_admin_menu(self):
        email = input("Email: ")
        password = input("Password: ")
        login_result = self.controller.login(email, password)
        print(login_result)

        if "Welcome" not in login_result:
            return

        while self.controller.logged_in_admin:
            print("\nAdmin Menu:")
            print("(s) Show all students")
            print("(g) Group by grade")
            print("(p) Partition Pass/Fail")
            print("(r) Remove student")
            print("(c) Clear all students")
            print("(x) Logout")

            choice = input("Choose: ").lower()

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
