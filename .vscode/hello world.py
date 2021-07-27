import os
import hashlib

print("Hello world")
print ("What is your name")
name = input()
print("Hi your name is: "+ name )
string_length= len(name)
print("The length of your name is:" + str(string_length))
age=int(input("Enter you age "))
if age> 21:
    print ("Your are old enough to buy a knife")
if age>= 18 & age<=21:
    print ("You can buy alcohol but not a knife  ")
else:
    print("You are too young to buy a knife or alchohol")

print("Enter a password ")
password=input()
salt = os.urandom(32)

key= hashlib.pbkdf2_hmac(
    'sha256', password.encode('utf-8'),
    salt, 100000,
    dklen=128
)

print(password)