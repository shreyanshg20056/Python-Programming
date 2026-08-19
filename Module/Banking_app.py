balance = 1000
amount = 0
def check_balance(balance):
    print(f"Your Bank Balance is: {balance}")

def deposit(balance,amount):
    amount = int(input("Enter Deposit Amount:"))
    balance += amount
    print(f"Your Amount {amount} has been deposited successfully!!")
    print(f"Your New Balance is:{balance}")

def withdraw(balance,amount):
    amount = int(input("Enter Withdrawing Amount:"))
    balance = balance - amount
    print(f"Your Amount {amount} has been withdrwan Sucessfully!!")
    print(f"Your New Balance is:{balance}")
bal = 1000
amt = 0

print("Welcome To Our Bank!!")

while True:
    print("1. Check Balance")
    print("2. Deposit Amount")
    print("3. Withdraw Amount")
    print("4. Quit")
    choice = int(input("Enter Your Choice (1-4): "))
    if choice == 1:
        check_balance(bal)
    elif choice == 2:
        deposit(bal,amt)
        print(f"Your New Balance is:{bal}")    
    elif choice == 3:
        withdraw(bal,amt)
        print(f"Your New Balance is:{bal}")
    elif choice == 4:
        break
    else:
        print("You Entered Invalid Choice!!Please Try Again.")

    
print("Thank You For Banking with us!!")