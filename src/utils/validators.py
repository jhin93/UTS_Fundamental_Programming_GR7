import re

def validate_email(email):
    return email.endswith('@university.com')

def validate_password(password):
    pass_check = True
    # Rule 1: Starts with an uppercase letter
    if not re.match(r'^[A-Z]', password):
        print("Password must start with an uppercase letter.")
        pass_check = False

    # Rule 2: Contains at least 5 letters total (including first)
    letter_matches = re.findall(r'[a-zA-Z]', password)
    if len(letter_matches) < 5:
        print("Password must contain at least 5 letters.")
        pass_check = False

    # Rule 3: Ends with at least 3 digits
    digit_match = re.search(r'\d{3,}$', password)
    if not digit_match:
        print("Password must end with at least 3 digits.")
        pass_check = False
        
    return pass_check
    # return re.match(r'^[A-Z][a-zA-Z]{4,}\d{3,}$', password)

def validate_old_password(old_password, new_password):
    return old_password != new_password
