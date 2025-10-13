class BankAccount:
    def __init__(self,balance):
        self.__balance=balance
    def deposit(self,amount):
        self.__balance+=amount
        print("Amount deposited:",amount)
    
    def withdraw(self,amount):
        if amount<=self.__balance:
            self.__balance-=amount
            print("Amount withdrawm:",amount)
        else:
            print("Insufficient balance")
    def get_balance(self):
        return self.__balance

acc=BankAccount(1000)
acc.deposit(500)
acc.withdraw(200)
print("Current balance:",acc.get_balance())