import hashlib
import os
import re

users = {} # A simple demo storage

# Add a user
username = input(print("Enter a username")) # The users username
password = input(print("Enter a password which is atleast 8 characters long ")) # The users password
if(re.fullmatch(r'[A-Za-z0-9#$%^&+={8,}]',password )):

    salt = os.urandom(32) # A new salt for this user
    key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    users[username] = { # Store the salt and key
        'salt': salt,
        'key': key
}

else:print("Enter a password which is atleast 8 characters long ")

# Verification attempt 1 
salt = os.urandom(32) 
username =  input(print("Enter your username again"))
password = input(print("Enter your password again"))

salt = users[username]['salt'] # Get the salt
key = users[username]['key'] # Get the correct key
new_key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)

if  key != new_key:
    print(" invalid login username or password dosen't match")

else:    

    print("succesfull login")
    h = hashlib.blake2b.hexdigest
    print(h)


