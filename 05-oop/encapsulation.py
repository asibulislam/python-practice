#Secure Bank Account
class BankAccount:
    def __init__(self, account_holder, account_number, balance):
        self.__account_holder = account_holder
        self.__account_number = account_number
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance: {self.__balance}")
        else:
            print("Insufficient balance.")
    def set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount
            print(f"Balance set to {self.__balance}")
        else:
            print("Balance cannot be negative.")

    def get_balance(self):
        return self.__balance

    def display_account_info(self):
        print(f"Account Holder: {self.__account_holder}")
        print(f"Account Number: {self.__account_number}")
        print(f"Balance: {self.__balance}")

s1 = BankAccount("Alice Smith", "A123456", 1000)
s1.display_account_info()
s1.deposit(500)
s1.withdraw(200)
s1.display_account_info()

print("\n")
s1.set_balance(2000)
print(f"Updated Balance: {s1.get_balance()}")

s1.display_account_info()
