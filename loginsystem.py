import hashlib
import uuid
import os
import pyodbc

def passwordvalidator(password): 
    isvalid= True
    if(len(password) < 8 ): 
         isvalid = False
    if isvalid: 
        return isvalid
def LoginAttempt():
   username= input(("Enter your username: "))
   password= input(("Enter your password: "))
   return username, password 
   
 
def main():
    users = {} # A simple demo storage
    count=0
    while count <3:
        # Add a user
        username = input(("Enter a username : ")) # The users username
        password = input(("Enter a password which is atleast 8 characters long: ")) # The users password 
    
        if(passwordvalidator(password)): 
            print("Password is valid ")
            count=4
        else: 
            print("Invalid password ")  
            count= count+1 
        
    users = {} # A simple demo storage
    salt = uuid.uuid4().hex
         
    hashedpassword= hashlib.sha1(salt.encode() +
     password.encode()).hexdigest() + ':' + salt
    print(hashedpassword)
    try: 
            conn= pyodbc.connect('Driver= {ODBC Driver 17 for SQL Server};' 'Server=(LocalDB)\MSSQLLocalDB;' 
                                'Database=python;'   'Trusted_Connection=yes;' )
            print("Connection Success")  
            cursor = conn.cursor()
            query="INSERT INTO Users (Username, Password) VALUES (?,? )" 
            parameters= username,hashedpassword,
            conn.execute(query,parameters)
            LoginAttempt()
            username,password = LoginAttempt()
            query1= """SELECT FROM Users WHERE Username=%s  AND Password=%s """
            parameters1 = username,password
            conn.execute(query1,parameters1)
            cursor.commit()                  
            
    except Exception as e:
            print(e)
            print("failed connection ")
     
    

if __name__ == '__main__':
    main()