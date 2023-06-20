class BankAccount:
    def __init__(self,account_number,balance):
        self._account_number = account_number
        self.__balance = balance

    def deposit(self,amount):
        self.__balance += amount

    def withdraw(self,amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance.")

    def get_account_number(self):
        return self._account_number

    def get_balance(self):
        return self.__balance

if __name__ == '__main__':
    account = BankAccount("12345",1000)
    #access protected attribute directly
    print(account._account_number)

    #access private attributes using mangled name
    print(account._BankAccount__balance)

    #access attribute using getter method
    print(account.get_account_number())
    print(account.get_balance())

    account.deposit(500)
    print("After deposit of 500: ",account.get_balance())

    account.withdraw(200)
    print("After withdraw of 200: ",account.get_balance())

    if account.get_balance() == 1300:
        print("Win!!")
