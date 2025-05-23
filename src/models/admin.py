import random

class Admin:
    """Admin class representing an administrator in the system. This model class is used to manage the 
    administrator's information such as name, email, and password. It also provides methods to convert the
    admin object to and from a dictionary format for easy serialization and deserialization."""
    def __init__(self, name, email, password, admin_id=None):
        self.admin_id = admin_id or f"{random.randint(1, 99999):05}"
        self.name = name
        self.email = email
        self.password = password

    def to_dict(self):
        return {
            "admin_id": self.admin_id,
            "name": self.name,
            "email": self.email,
            "password": self.password
        }

    @staticmethod
    def from_dict(data):
        return Admin(
            name=data["name"],
            email=data["email"],
            password=data["password"],
            admin_id=data.get("admin_id")
        )