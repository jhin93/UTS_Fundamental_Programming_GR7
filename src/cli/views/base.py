from abc import abstractmethod

class BaseView:
    """Base class for all views in the CLI application. This class serves as a template for
    specific views like StudentView and AdminView. It defines the basic structure and methods"""
    def __init__(self):
        pass
    
    @abstractmethod
    def show_menu(self):
        """Display the menu to the user."""
        pass
    
    @abstractmethod
    def dashboard(self):
        """Display the dashboard functionalities to the user."""
        pass
    
    @staticmethod
    def retry():
        """
        Prompt the user to retry an action. This method is only used in the 
        StudentView class till now.
        
        """
        try:
            response = input("Try again? (y/n): ").lower()
            if response == 'y':
                return True
            elif response == 'n':
                return False
            else:
                print("Invalid option. Please enter 'y' or 'n'.")
                BaseView.retry()
        except (EOFError, KeyboardInterrupt):
            print("\nError in getting input response. Exiting.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return False