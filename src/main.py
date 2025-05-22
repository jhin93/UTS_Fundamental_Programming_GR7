from cli.views.student_view import StudentView
from cli.views.admin_view import AdminView

def main():
    student_view = StudentView()
    admin_view = AdminView()

    while True:
        print("\nUniversity Menu:\n(A) Admin\n(S) Student\n(X) Exit")
        choice = input("Select option: ").lower()

        if choice == 's':
            student_view.show_main_menu()
        elif choice == 'a':
            admin_view.show_admin_menu()
        elif choice == 'x':
            break
        else:
            print("Invalid option.")

if __name__ == '__main__':
    main()
