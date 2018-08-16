"""Aidan"""

MIN_LENGTH = 6
password = input("Password: ")

while len(password) < MIN_LENGTH:
    print("Error! Password too short!")
    password = input("Password: ")

print("*" * len(password))