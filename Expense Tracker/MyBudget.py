import time as t
import csv as c

class budget:
    Name = ''
    MyBudget = 0
    Budget_copy = 0
    my_record = {
    }

    def __init__(self):
        self.Name = str(input("Please Enter Your Good Name: "))
        while True:
            print("----- Expense Tracker -----")
            print("1. Set Budget")
            print("2. Add Expence")
            print("3. Analyze Budget")
            print("0. Exit \n")
            Choice = int(input("Enter Your Choice: "))
            if Choice == 0:
                break
            if Choice == 1:
                self.setBudget()
            elif Choice == 2:
                self.addExpense()
            elif Choice == 3:
                self.analyse()
            else:
                print(f"{self.Name}, Please Enter Valid Choice.")

    def setBudget(self):
        self.MyBudget = int(input(f"{self.Name}, Enter Your Budget:"))
        print(f"{self.MyBudget} Is Set For You!")
        self.Budget_copy = self.MyBudget

    def addExpense(self):
        ask = ''
        while True:
            if self.MyBudget == 0:
                print(f"{self.Name}, Please Set Your Budget First!")
                self.setBudget()
            if ask == 's' or ask == 'S':
                break
            elif ask == '':
                exp_type = input("Enter Your Expense Title: ")
                exp_amount = int(input("Enter Your Expense: "))
                self.my_record[exp_type]=exp_amount
                self.MyBudget -= exp_amount
                low = int(self.Budget_copy*5/100)
                print(self.MyBudget)
                print(low)
                print(f"{self.Name}, Your {self.MyBudget} Available Out of {self.Budget_copy}")
                if self.MyBudget == 0:
                    print("Your Budget Limit Execute!")
                elif self.MyBudget <= low:
                    print("Your Budget is Low!")
                    ask = str(input("Press Enter For 'Continue' Or S for 'Stop'"))
                else:
                    ask = str(input("Press Enter For 'Continue' Or S for 'Stop'"))

    def analyse(self):
        print(f"{self.Name}, Your Set Budget Is ${self.Budget_copy}.")
        calculation = self.Budget_copy
        for key,value in self.my_record.items():
            calculation += value
            print(f"{key}:{value}")
        print(f"Your Total Spend: {calculation}")
        print(f"Available Budget: {self.MyBudget}")
            
Budget = budget()
