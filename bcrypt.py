 import bcrypt

password= b"SecretPassword55"
salt = bcrypt.gensalt()
hashed = bcrypt.hashpw(password,salt)
print(hashed)
b''