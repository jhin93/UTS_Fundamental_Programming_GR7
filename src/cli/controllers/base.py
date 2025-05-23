from models.database import Database
from abc import abstractmethod
class BaseController:
    """Base class for all controllers in the CLI application. In case in the future, 
    we would need to build more controllers, we can inherit from this class."""
    def __init__(self):
        self.db = Database()
        self.students = self.db.students

    def refresh_db(self):
        """Refresh the database to ensure we have the latest data."""
        self.db.load()
        self.students = self.db.students

    @abstractmethod
    def login(self, email, password):
        pass
    
    @abstractmethod
    def logout(self):
        pass
    