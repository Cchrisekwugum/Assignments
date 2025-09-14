#### CREATING AN AUTHENTICATION SYSTEM #######

# For Login: Checking if a user exists and verifying their password.
# To Register User: Adding a new user with validation checks (valid email, strong password, no duplicates).
# To Remove User: Deleting a user by ID.

# STEP 1 A
# Create a function to validate email and password
# - Email must contain "@"
# - Password must have min of 8 chars and min of 1 digit
# - Email must be unique

users = {}
new_id = 1

# Defining validation functions

def validate_password(password):     
    if len(password) < 8:
        print("Password must be at least 8 least 8 characters")
        return False
    
    if not any(char.isdigit() for char in password):
        print("Password must contain at least one digit")
        return False
    
    return True

def validate_email(email):
    if "@" not in email:
        print("Invalid email")
        return False
    else:   
        return True
    
    
def is_email_unique(email):
    for user in users.values():
        if user["email"] ==email:
            return True
        else:
            return False
    
   
# Test validation functions
password = "christoper123"
email = "chris@gmail.com"
print("Password validation:", validate_password(password))     
                
    