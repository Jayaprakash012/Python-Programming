class BankAccount:
    
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.__balance = balance  

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"₹{amount} deposited successfully.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient balance.")
        elif amount <= 0:
            print("Invalid withdrawal amount.")
        else:
            self.__balance -= amount
            print(f"₹{amount} withdrawn successfully.")

    def get_balance(self):
        return self.__balance

account = BankAccount("Jaya Prakash", 5000)

account.deposit(2000)
account.withdraw(1500)
print("Current Balance:", account.get_balance())
