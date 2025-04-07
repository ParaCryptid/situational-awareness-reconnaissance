
import json
import getpass
import os

ROLES_FILE = "/opt/training-system/config/roles.json"

def load_roles():
    if not os.path.exists(ROLES_FILE):
        return {}
    with open(ROLES_FILE, "r") as f:
        return json.load(f)

def authenticate_user():
    username = input("Username: ")
    password = getpass.getpass("Password: ")
    roles = load_roles()
    if username in roles and roles[username]["password"] == password:
        print(f"[AUTH] Login successful - Role: {roles[username]['role']}")
        return roles[username]["role"]
    else:
        print("[AUTH] Access denied.")
        return None
