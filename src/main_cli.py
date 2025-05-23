from cli.views.student_view import StudentView
from cli.views.admin_view import AdminView

def main():
    """Main function to run the CLI application."""
    
    

    while True:
        print("\nUniversity Menu:\n(A) Admin\n(S) Student\n(X) Exit")
        choice = input("Select option: ").lower()

        if choice == 's':
            student_view = StudentView()
            student_view.show_menu()
        elif choice == 'a':
            admin_view = AdminView()
            admin_view.show_menu()
        elif choice == 'x':
            break
        else:
            print("Invalid option.")

if __name__ == '__main__':
    main()
