from models.database import Database

class BaseController:
    def __init__(self):
        self.database = Database("data.json")

    def read_data(self):
        pass