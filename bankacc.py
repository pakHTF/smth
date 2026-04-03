class BankAccount:
    def __init__(self, initial_balance):
        self.balance = int(initial_balance)

    def deposit(self, amount):
        self.balance+=amount
        if self.balance<=0:
            print('negative balance.')
    def withdraw(self, amount):
        if self.balance>=amount:
            self.balance-=amount
        else:
            print('error')
    def show_balance(self):
        print(self.balance)
