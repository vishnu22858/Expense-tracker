from stores import UserStore
from getpass import getpass
import hashlib
import random
from datetime import datetime
import os

_ITERATIONS = 120_000

"""
    1. take username
    2. Ensure the username is not taken
    3. Ask for a password
    4. Confirm password again
    5. SECURELY store the password
    6. Save the user in the users list in users.json
"""

def _hash_pass(password, salt):
    dk = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, _ITERATIONS)
    return dk.hex()

def signup(users):
   
    print("\nSignup new user")

    username = input("Enter a username: ")

    if not username:
        print("Username cannot be empty")
        return

    if users.find_user_by_username(username):
        print("Username already taken. please choose a diffetrent username")
        return 

    password = getpass()
    confirm_pass = getpass("Confirm password:")

    if not password == confirm_pass:
        print("Passwords do not match. Please try again")
        return

    if len(password) < 6:
        print("Minimum 6 chars required")
        return
    salt = os.urandom(16)
    hash_password = _hash_pass(password, salt)

    user = {
        "user_id": str(random.random()),
        "username": username,
        "password_hash": hash_password,
        "salt": salt.hex(),
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    
    users.add_user(user)
    print("Signup successful. You can now login")
    

def login(users):
    print("\nLogin existing user")

    username = input("Enter your username:")
    
    user = users.find_user_by_username(username)
    if not user:
        print("User not found. please signup first")
        return 
    
    password = getpass("Enter your password: ")

    salt = bytes.fromhex(user["salt"])
    entered_hashed_password = _hash_pass(password, salt)

    if entered_hashed_password != user["password_hash"]:
        print("Password does not match, Please try again")
        return None

    print("Login Successful!")
    return user
