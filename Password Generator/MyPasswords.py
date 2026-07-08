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

        def passwordmaker(self):
            while True:
                if self.stop=='S':
                    break
                else:
                    patten = string.ascii_letters + string.digits + '@#$%&'
                    self.password = "".join(r.choice(patten)
                    for i in range(self.length))
                    self.password_check()

        def password_check(self):
            ptn = 0
            while True:
                DIGITS = "0123456789"
                SYMBOL = "@#$%&"
                STRING = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                for digit in DIGITS:
                    if digit in self.password:
                        ptn += 1
                        break
                for symbol in SYMBOL:
                    if symbol in self.password:
                        ptn += 1
                        break
                for string in STRING.lower():
                    if string in self.password:
                        ptn += 1
                        break
                for string in STRING:
                    if string in self.password:
                        ptn += 1
                        break
                break
            if ptn == 4:
                print("-" * 70)
                print(" Do Not Share " * 5)
                print("-" * 70)
                print(f"{self.index:^3}. {self.password:^60}")
                print("-"*70)
                print(" Do Not Share " * 5)
                print("-" * 70 + "\n")
                stop = str(input("Enter 'S' for stop else Press 'Enter' For New Password:")).capitalize()
                if stop == 'S':
                    self.stop = 'S'
                    time.sleep(10)

                    print("~"*70)
                    print("Prince Kyada - 'Your Security is Our Responsibility!!'")
                    print("Thanks for using Password Generator!!!")
                    print("~"*70)
                else:
                    print("New Password Arrive after 15 Seconds.. \n")
                    self.index += 1
                    time.sleep(10)
                    self.passwordmaker()
    except  Exception as e:
        print(f"Password Generator Error!!- {str(e)}")
password = PasswordGenerator()
