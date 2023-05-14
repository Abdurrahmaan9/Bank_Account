from datetime import datetime
class BankAccount:
    #initializing a constructor with attributes
    def __init__(self,account_number,balance,date_of_opening,customer_name):
        self.account_number = account_number
        self.balance = balance
        self.date_of_opening = date_of_opening
        self.customer_name = customer_name
    #create method deposit
    def deposit(self,amount,datetime):
        datetime = datetime.now()
        # self.balance = self.balance + amount
        self.balance += amount
        print(f"{amount} has been deposited on your account at {datetime}")
    #method withdraw
    def withdraw(self,amount,datetime):
        datetime = datetime.now()
        if amount > self.balance:
            print(f"Insufficient funds your current balance is{self.balance}")
        else:
            # self.balance = self.balance - amount
            self.balance -= amount
            print(f"withdrawal succeful you have withdrawn {amount} you current balance is {self.balance} at {datetime}")
    #method checkbalance
    def checkbalance(self,datetime):
        datetime = datetime.now()
        print(f"current balance is {self.balance} {datetime}")
    #method customer details
    def customer_details(self):
        print(f"Name:{self.customer_name}")
        print(f"Accountnumber:{self.account_number}")
        print(f"Date of Opening:{self.date_of_opening}")
        print(f"Balance:{self.balance}")

