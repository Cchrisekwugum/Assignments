import pandas as pd
import json
import os


USER_data = "users.json"

if os.path.exists(USER_data):
    with open(USER_data, "r") as f:
        users = json.load(f)
else:
    users = {}


users = {int(k): v for k, v in users.items()}


next_id = max(users.keys(), default=0) + 1
