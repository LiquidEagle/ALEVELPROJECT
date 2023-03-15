# All Database stuff goes in here!!
import sqlite3
import hashlib

# test_input = input("What is the password: ")
# test_hashed = hashlib.sha256(test_input.encode('utf-8')).hexdigest()
# test_string = 'hello'
# hashed = hashlib.sha256(test_string.encode('utf-8')).hexdigest()
# if test_hashed == hashed:
#   print("Correct!!!!!!!")
# else:
#     print("nah")
#from cryptography.fernet import Fernet

# key = Fernet.generate_key()
# cipher = Fernet(key)

# def encrypt(message: bytes, key: bytes):
#     return Fernet(key).encrypt(message)
# def decrypt(token: bytes, key: bytes):
#     return Fernet(key).decrypt(token)

# print(ciphered_text)


con = sqlite3.connect('alldata.db')
cursor = con.cursor()
access = True

def createDBandTable():
    sql = """
CREATE TABLE Logins(id INTEGER,
username TEXT,
password TEXT,
PRIMARY KEY(id AUTOINCREMENT))
"""

    cursor.execute(sql)
    con.commit()
    return "database and table created"


def register():
    username = input("Create Username: ")
    password = input("Create Password: ")
    hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
    sql = 'INSERT INTO Logins (username,password) VALUES ("' + username + '","' + hashed_password + '");'
    print(sql)
    cursor.execute(sql)
    con.commit()


def login():
    username_login = input("Username: ")
    password_login = input("Password: ")
    password_hashed = hashlib.sha256(password_login.encode('utf-8')).hexdigest()
    statement = "SELECT * FROM Logins WHERE username = '" + username_login + "' AND password = '" + password_hashed + "'"
    cursor.execute(statement)
    if not cursor.fetchone():
        print("Login failed")
        access = False
    else:
        print("Welcome")
        access = True
    return access
