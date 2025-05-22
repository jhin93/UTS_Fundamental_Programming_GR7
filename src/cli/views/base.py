from abc import abstractmethod

class BaseView:
    """Base class for all views in the CLI application."""
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
        response = input("Try again? (y/n): ").lower()
        if response == 'y':
            return True
        elif response == 'n':
            return False
        else:
            print("Invalid option. Please enter 'y' or 'n'.")
            BaseView.retry()