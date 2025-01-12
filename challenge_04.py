#Password Strength Checker
#Write a function that checks the strength of a given password. The function should:
#Check if the password has at least one uppercase letter, one lowercase letter, one number, and one special character.

import re

password = (input("Enter a password including numbers, uppercase letters and special character: "))

def password_check(password):
    if (any(char.isdigit() for char in password) and
        any(char.isupper() for char in password) and
        any(char in "!@#$%^&*()_+" for char in password)):
        print("Good password!")
    else:
        print("Bad password! Make sure it has a number, an uppercase letter, and a special character.")

password_check(password)