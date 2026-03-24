class BankAccount :
    def __init__(self , account_number , balance ) :
        self.account_number = account_number
        self.balance = balance

# Method to deposite money
    def deposite(self , amount) :
        if amount > 0 :
            self.balance += amount
            print(f"Deposited amount {amount} successfully .")
        else :
            print("Invalid deposite amount .")

# method to withdraw money
    def withdraw(self , amount) :
        if amount > 0 :
            if amount <= self.balance :
                self.balance -= amount
                print(f"Withdrawn amount {amount} successfully .")
            else:
                print("Insufficient balance .")
        else :
            print("Invalid withdrawl amount.") 

#Method to enter your account details
print("Enter your account number:")
account_number = input()
print("Enter your initial balance:")
initial_balance = float(input())

# Create a BankAccount object
account = BankAccount(account_number, initial_balance)
print("\nChoose your option:")
while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        amount = float(input("Enter amount to deposit: ")) 
        account.deposite(amount)
        print("Remaining balance:", account.balance)

    elif choice == "2":
        amount = float(input("Enter amount to withdraw: "))
        account.withdraw(amount)
        print("Remaining balance:", account.balance)

    elif choice == "3":
        account.check_balance()
   
    elif choice == "4":
        print("Thank you for using the bank account system.")
        break
    else:
        print("Invalid choice. Please try again.")
