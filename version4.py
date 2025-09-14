# Lets build endpoints  for our users

#POST /register → create user

#POST /login → login user

#GET /users → list all users

#PUT /users/{user_id}/password → update password

#DELETE /users/{user_id} → remove user

###########################################

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from config import CONFIG
import uvicorn

# let create a FastAPI instance
# Import the correct version
VERSION = CONFIG["version"]
if VERSION == "v1":
    from version1 import *
elif VERSION == "v2":
    from version2 import *
elif VERSION == "v3":
    from version3 import *
else:
    raise ValueError(f"Unsupported version: {VERSION}")

app = FastAPI(title="Advantra Authentication API", version=VERSION)

# Setting up pydantic schema
class Register_user(BaseModel):
    name: str
    email: str
    password: str
    
class User_login(BaseModel):
    email: str
    password: str
    
class Update_user_password(BaseModel):
    user_id: int
    old_password: str
    new_password: str
    
# SETTING UP ENDPOINTS

# 1. Post endpoint for user registration

@app.post("/register")
def register_user_endpoint(user: Register_user):
    result = register(user.email, user.name, user.password)
    if result["Status"] == "error":
        raise HTTPException(status_code=400, detail=result["Message"])
    return result

# 2. Post endpoint for user login

@app.post("/login")
def login_user_endpoint(user: User_login):
    result = login(user.email, user.password)
    if result["Status"] == "error":
        raise HTTPException(status_code=400, detail=result["Message"])
    return result

# 3. Get endpoint for listing all users

@app.get("/users")
def list_users_users():
    result = list_users()
    if result["Status"] == "error":
        raise HTTPException(status_code=400, detail=result["message"])
    return result

# 4. Put endpoint for updating user password

@app.put("/users/{user_id}/password")
def update_password_endpoint(user_id: int, password: Update_user_password):
    result = update_password(user_id, password.old_password, password.new_password)
    if result["Status"] == "error":
        raise HTTPException(status_code=400, detail=result["message"])
    return result

# 5. Delete endpoint for removing user

@app.delete("/users/{user_id}")
def remove_user_user(user_id: int):
    result = remove_user(user_id)
    if result["Status"] == "error":
        raise HTTPException(status_code=400, detail=result["message"])
    return result


# Run the fastAPI app
if __name__ == "__main__":
    uvicorn.run(app)

# Run the fastAPI app
 # - http://127.0.0.1:8000/docs


