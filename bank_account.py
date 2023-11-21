class BalanceException(Exception):
    pass


class BankAccount:

    def __init__(self, initialAmount, accountName):
        self.balance = initialAmount
        self.name = accountName

        # print(f"Account '{self.name}', created. \nBalance = ${self.balance:.2f} \n")

    def getBalance(self):
        print(f"Account '{self.name}' balance = ${self.balance:.2f}")

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("\nDeposite is completed.")
        self.getBalance()

    def viableTransaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(f' Insuffiecent balace ')

    def withdraw(self, amount):
        try:
            self.viableTransaction(amount)
            self.balance = self.balance - amount
            print("\nWithdraw Complete.")
            self.getBalance()
        except BalanceException as error:
            print(f"Withdraw interrupted: {error}")

    def transfer(self,amount,account):
        try:
            print('\n**********\n \nBegining Transfer...🌈')
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print('\n Transfer complete...✅')
        except BalanceException as error:
            print(f'\n Transfer Intrrupted.❌❌ {error}')