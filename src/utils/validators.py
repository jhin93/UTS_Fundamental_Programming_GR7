import re

def validate_login(email, password):
    if not email.strip() or not password.strip():
        return False

    if not email.endswith("@university.com"):
        return False
    
    pattern = r'[A-Z][a-zA-Z]{4,}[0-9]{3,}'
    if not re.fullmatch(pattern, password):
        return False

    return True
    
    