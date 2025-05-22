from models.database import Database
from abc import abstractmethod
class BaseController:
    def __init__(self):
        self.db = Database()
        self.students = self.db.students

    def refresh_db(self):
        self.database.load()
        self.students = self.database.students

    @abstractmethod
    def login(self, email, password):
        pass
    
    @abstractmethod
    def logout(self):
        pass
    