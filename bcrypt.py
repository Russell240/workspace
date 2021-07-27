import bcrypt

password= b"SecretPassword55"
hashed = bcrypt.hashpw(password, bcrypt.gensalt())
print(hashed)
b''