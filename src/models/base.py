from abc import ABC, abstractmethod
import random
class User:
    """ A simple base class for all users."""
    def __init__(self, name: str, email: str, password: str):
        self.name = name
        self.email = email
        self.password = password
    
    def __studentID_generator(self):
        return self.email.split('@')[0] + str(random.randint(1000, 9999))
    
class Student(User):
    """ A student class that inherits from the User class"""
    def __init__(self, name, email, password):
        super().__init__(name, email, password)
        self.student_id = 
        
    def __str__(self):
        return f"Student ID: {self.student_id},\n Name: {self.name},\n Email: {self.email}"