import random as r
import string
import time

class PasswordGenerator:
    try:
        length = 0
        stop = ''
        index = 1
        def __init__(self):
            print("*"*70)
            print(f"{'Welcome To Password Maker':^70}")
            print("*"*70)
            print("Initializing Password Generator ...")
            time.sleep(5)
            print("Setup is completed.")
            while True:
                try:
                    print("*" * 70)
                    self.length = int(input("Enter the length of the password you would like to generate: "))
                    print("*" * 70)
                    if self.length < 4:
                        print("Password Length must be greater than 4")
                    else:
                        break
                except ValueError:
                    print("Please enter a valid Digit length.")
            print("Generating password ...")
            time.sleep(5)
            self.passwordmaker()
password = PasswordGenerator()
