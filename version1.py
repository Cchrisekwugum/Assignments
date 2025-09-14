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
    return True
    
    
def is_email_unique(email):
    for user in users.values():
        if user["email"] ==email:
            return True
        return False
    
   
# Test validation functions
# password = "christoper123"
# email = "chris@gmail.com"
# print("Password validation:", validate_password(password))   
# print("Email validation:", validate_email(email))
# print("Email validation:", is_email_unique(email))  
                

# STEP 1 B
# Create a function to register a new user
# - check if email is valid
# - check if password is strong
# - check if there is no duplicate email
# - if email is valid, creates a new user with unique ID that is, check if it already exist

def register(email:str, name:str, password:str) ->dict:
    
    """
    Arguments:
        email: user’s email address
        name: user’s full name
        password: chosen password

    """
    global users, new_id
    
    if not validate_email(email):
        return {"status": "error", "Message": "Invalid email"}
    if not validate_password(password):
        return {"status": "error", "Message": "Password must be min of 8 chars and min of 1 digit"}
    if is_email_unique(email):
        return {"status": "error", "Message": "Email already taken"}
    
    user = {
        "id": new_id,
        "email": email,
        "name": name,
        "password": password,
        "is_admin": False
    }
    users[new_id] = user
    new_id = new_id + 1
    return {"Status": "success", "Message": "User registered successfully", "user_id": new_id}

# Test register function
email = "chris@gmail.com"
name = "christopher"
password = "christoper123"
print(register(email, name, password))


# STEP 2
# Create a function for user login
 # - check if user exists
 # - check if password matches

def login(email:str, password:str) -> dict:
    """
    Arguments:
        email: user’s email
        password: user’s password
    """
    for user_id, user_data in users.items():
        if user_data["email"] == email:
            if user_data["password"] == password:
                return {"Status": "success", "Message": "Login successful", "user_id": user_id}
            else:
                return {"Status": "error", "Message": "Invalid email or password"}
    return {"Status": "error", "Message": "Invalid email or password"}

# Test login function
email = "chris@gmail.com"
password = "christoper123"
print(login(email, password))