import pandas as pd
import json
import os
import bcrypt 

USER_data = "users.json"

# Load existing users
if os.path.exists(USER_data):
    with open(USER_data, "r") as f:
        users = json.load(f)
else:
    users = {}

# Convert keys to int for internal use
users = {int(k): v for k, v in users.items()}
next_id = max(users.keys(), default=0) + 1


def save_users(users):
  
    with open(USER_data, "w") as f:
        json.dump(users, f, indent=4)


# STEP 1: Register
def register(email: str, name: str, password: str) -> dict:
    global next_id

    if "@" not in email:
        return {"Status": "error", "Message": "Invalid email"}
    if len(password) < 8 or not any(char.isdigit() for char in password):
        return {"Status": "error", "Message": "Password must be at least 8 characters and contain a digit"}
    if any(user["email"] == email for user in users.values()):
        return {"Status": "error", "Message": "User email already taken"}

    # lets hash the password
    hashed_pw = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

    user_id = next_id
    users[user_id] = {
        "id": user_id,
        "name": name,
        "email": email,
        "password": hashed_pw,  
        "is_admin": False
    }
    next_id += 1
    save_users(users)
    return {"Status": "success", "Message": "User registered successfully", "User_id": user_id}

# testing register
#acount1
email = "chris@gmail.com"
name = "chris"
password = "chris123"
print("Register result:", register(email, name, password))

#acount2
email = "onyekachi@gmail.com"
name = "onyekachi"
password = "onyekachi123"
print("Register result:", register(email, name, password))

#acount3
email = "ekwugum@gmail.com"
name = "ekwugum"
password = "ekwugum123"
print("Register result:", register(email, name, password))

# STEP 2: Login
def login(email: str, password: str) -> dict:
    try:
        with open(USER_data, "r") as f:
            users = json.load(f)
    except FileNotFoundError:
        return {"Status": "error", "Message": "No users found"}

    for user in users.values():
        if user["email"] == email:
            if bcrypt.checkpw(password.encode("utf-8"), user["password"].encode("utf-8")):
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


# STEP 3: List all users
def list_users() -> dict:
    try:
        with open(USER_data, "r") as f:
            users = json.load(f)
            df = pd.DataFrame.from_dict(
                users, orient="index",
                columns=["id", "name", "email", "password", "is_admin"]
            )
            print(f"\nYou have a total number of {len(df)} users\n")
            print(df.head())  
    except FileNotFoundError:
        return {"Status": "error", "Message": "Users file not found"}

    if len(users) == 0:
        return {"Status": "error", "Message": "No users found"}

    return {"Status": "success", "Message": "This is a view of all users"}


# STEP 4: Update password
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

    # Verify old password
    if not bcrypt.checkpw(old_password.encode("utf-8"), user["password"].encode("utf-8")):
        return {"Status": "error", "Message": "Invalid old password"}

    # Validate new password
    if len(new_password) < 8 or not any(char.isdigit() for char in new_password):
        return {"Status": "error", "Message": "New password must be at least 8 characters and contain a digit"}

    # Hash new password
    hashed_pw = bcrypt.hashpw(new_password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")
    user["password"] = hashed_pw
    users[user_id_str] = user
    save_users(users)

    return {"Status": "success", "Message": "Password updated successfully"}

# testing update password
user_id = 1
old_password = "chris123"
new_password = "chris321"
print("Update password result:", update_password(user_id, old_password, new_password))

# STEP 5: Remove user
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