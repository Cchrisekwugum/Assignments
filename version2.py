import pandas as pd
import json
import os

print(os.getcwd())
#USER_data = "users.json"
USER_data = r"../users.json"

if os.path.exists(USER_data):
    with open(USER_data, "r") as f:
        users = json.load(f)
else:
    users = {}


users = {int(k): v for k, v in users.items()}


next_id = max(users.keys(), default=0) + 1

def save_users(users):
    """Save users dictionary to file."""
    with open(USER_data, "w") as f:
        json.dump(users, f, indent=4)

# STEP 1 A: Register a new user
def register(email: str, name: str, password: str) -> dict:
    
    global next_id
    
    if "@" not in email:
        return {"Status": "error", "Message": "Invalid email"}
    if len(password) < 8 or not any(char.isdigit() for char in password):
        return {"Status": "error", "Message": "Password must be at least 8 characters and contain a digit"}
    if any(user["email"] == email for user in users.values()):
        return {"Status": "error", "Message": "User email already taken"}
    

    user_id = next_id
    users[user_id] = {
        "id": user_id,
        "name": name,
        "email": email,
        "password": password,
        "is_admin": False
    }
    next_id += 1
    save_users(users)
    return {"Status": "success", "Message": "User registered successfully", "User_id": user_id}

#testing register
email = "chris@gmail.com"
name = "chris"
password = "chris123"
print("Register result:", register(email, name, password))

# STEP2: Login a user

def login(email: str, password: str) -> dict:
 
  
    try:
        with open(USER_data, "r") as f:
            users = json.load(f)
    except FileNotFoundError:
        return {"Status": "error", "Message": "No users found"}
    
    for user in users.values():
        if user["email"] == email:
            if user["password"] == password:
                return {
                    "Status": "success",
                    "Message": "Login successful",
                    "User_id": user["id"],
                    "Name": user["name"]
                }
            else:
                return {"Status": "error", "Message": "Invalid password"}
    
    return {"Status": "error", "Message": "Email not found"}

# testing login
email = "chris@gmail.com"
password = "chris123"
print("Login result:", login(email, password))

#STEP3: List all users
def list_users() -> dict:
    try:
       with open("users.json", "r") as f:
            users = json.load(f)
            df = pd.DataFrame.from_dict(users, orient="index", columns=["id", "name", "email", "password", "is_admin"])
            df = df.drop(columns=["password"])
            print(f"\nYou hava a total number of {len(df.loc[:, 'id'])} users\n")
            print(df)

            
    except FileNotFoundError:
         return {"Status": "error", "Message": "Users file not found"}
 
    
    if len(df) == 0:
        return {"Status": "error", "Message": "No users found"}
    
    return {"Status": "success", "Message": "This is a view of all users"}


# testing list users
print("List of users:", list_users())


# STEP 5: Update user password

def update_password(user_id: int, old_password: str, new_password: str) -> dict:
    
    try:
        with open(USER_data, "r") as f:
            users = json.load(f)
    except FileNotFoundError:
        return {"Status": "error", "Message": "Users file not found"}

    user_id_str = str(user_id)

    if user_id_str not in users:
        return {"Status": "error", "Message": "User not found"}

    user = users[user_id_str]

    
    if user["password"] != old_password:
        return {"Status": "error", "Message": "Invalid old password"}

 
    if len(new_password) < 8 or not any(char.isdigit() for char in new_password):
        return {"Status": "error", "Message": "New password must be at least 8 characters long and contain a digit"}

   
    user["password"] = new_password
    users[user_id_str] = user

  
    save_users(users)

    return {"Status": "success", "Message": "Password updated successfully"}

# testing update password
user_id = 1
old_password = "chris123"
new_password = "chris1234"
print("Update password result:", update_password(user_id, old_password, new_password))


# STEP4: Remove a user from file by ID

def remove_user(user_id: int) -> dict:
    try:
        with open(USER_data, "r") as f:
            users = json.load(f)
    except FileNotFoundError:
        return {"Status": "error", "Message": "Users file not found"}
    
    user_id = str(user_id)
    if user_id not in users:
        return {"Status": "error", "Message": "User not found"}
    del users[user_id]
    save_users(users)
    return {"Status": "success", "Message": "User removed successfully"}

# testing remove user
user_id = 1
print("Remove user result:", remove_user(user_id))


