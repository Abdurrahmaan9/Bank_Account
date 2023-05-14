from practise import BankAccount
from datetime import datetime

#prompting user for input
customer_name = input("Enter Name :")
account_number = int(input("Enter acc no :"))
balance = 0
date_of_opening = datetime.now()

#create an object for the Bankacc class
account = BankAccount(account_number,balance,date_of_opening,customer_name)
account.customer_details()

# creating a loop
while True:
    print("""====Welcome to Frank's Family bank====
                 1.Deposit
                 2.Withdraw
                 3.Check Balance
                 4.Exit""")
    
    #creating a new variable action
    action = int(input("Enter choice :"))
    
    #create a statement
    if action == 1:
        amount = float(input("Enter Amount :"))
        account.deposit(amount,datetime)
    elif action == 2:
        amount = float(input("Enter Amount :"))
        account.withdraw(amount,datetime)
    elif action == 3:
        account.checkbalance(datetime)
    elif action == 4:
        exit()
    else:
        print("Invalid choice please try again")