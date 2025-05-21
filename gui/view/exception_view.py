import re

def validate_email(email):
    return email.endswith('@university.com')

def validate_password(password):
    return re.match(r'^[A-Z][a-zA-Z]{4,}\d{3,}$', password) 