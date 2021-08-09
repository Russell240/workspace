import hashlib
import os
import pyodbc


users = {} # A simple demo storage

# Add a user
username = input(("Enter a username : ")) # The users username
if(username==""):
        print("Don't leave username blank")
        username = input(("Enter a username : ")) 


password = input(("Enter a password which is atleast 8 characters long: ")) # The users password 
if len(password) <= 8:
    print("Enter a longer password")
    password = input(("Enter a password which is atleast 8 characters long: "))
       

salt = os.urandom(32) 
key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
users[username] = { # Store the salt and key
    'salt': salt, 
    'key': key
}   


        # Verification attempt 1 
username = input("Enter your username again: ")
password = input("Enter your password again: ")
if len(password) <= 8:
    print("Enter a longer password")
    password = input(("Enter a password which is atleast 8 characters long: "))


salt = users[username]['salt'] # Get the salt
key = users[username]['key'] # Get the correct key
new_key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)

if  key != new_key:
    print(" invalid login username or password dosen't match")

else:    

    print("succesfull login")
    print(salt); 

try: 
        conn= pyodbc.connect('Driver= {ODBC Driver 17 for SQL Server};' 'Server=(LocalDB)\MSSQLLocalDB;' 
                            'Database=python;'   'Trusted_Connection=yes;' )
        print("Connection Success")                    
               
except Exception as e:
        print(e)
        print("failed connection ")
else: 
    cursor = conn.cursor()
    cursor.execute(" INSERT INTO User (Username, Password, ID)  Values( username,password, 1 " )
    conn.commit()
