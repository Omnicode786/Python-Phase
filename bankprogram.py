def withdraw (balance, amount):
    balance -= amount
    print(f"you withdrawed {amount} from you account your new balance is: {balance}")
    return balance
def deposit (balance, amount):
    balance += amount
    print(f"you deposited {amount} into your account your new balance is: {balance}")
    return balance
def viewbalance(balance):
    print(f"Your current balance is: {balance}")
def main():
    print("Welcome to The Bank")
    active = False
    loop = True
    balance = float(input("Enter your balance: "))
    if balance >= 0:
        active = True
    if active:
        while loop and active:
            print("1: Show my Balance\n 2: Withdraw amount\n3: Deposit amount\n 4: Active/Unactive your account\n 5: Exit")
            choice = int(input("What would you like to do enter any number to perform the action: "))
            if choice == 1:
                viewbalance(balance)
            elif choice == 2:
                amount = float(input("Enter the amount you want to withdraw: "))
                balance = withdraw(balance, amount)
            elif choice == 3:
                amount = float(input("Enter the amount you want to deposit: "))
                balance = deposit(balance, amount)
            elif choice == 4:
                check = int(input("Enter 1 for active and 0 for locking it: "))
                if check == 1:
                    active = True
                    print("Tour account is already active keep using us")
                else:
                    print("Your account has been locked, Thanks for using our program bye!")
                    active = False
            else:
                print("Thanks for using our program bye!")
                loop = False
    print("Your account is locked!!")
main()