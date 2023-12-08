class BalanceException(Exception):
    pass

class BankAccount:
    def __init__(self, AccountBalance, AccountName):
        self.balance = AccountBalance
        self.name = AccountName
        print(f"\nAccount '{self.name}' created\nBalance = ${self.balance:.2f}")

    def getBalance(self):
        print(f"\nAccount '{self.name}' balance = ${self.balance:.2f}")
    
    def deposite(self, amount):
        self.balance = self.balance + amount
        print("\nDeposited complete.")
        self.getBalance()

    def viableTransaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(
                f"\nSorry, account '{self.name}' only has a balance of ${self.balance:.2f}"
            )
        
    def withdraw(self, amount):
        try:
            self.viableTransaction(amount)
            self.balance=self.balance - amount
            print("\nWithdraw complete")
            self.getBalance()
        except BalanceException as error:
            print(f"\nWithdraw innterrupted: {error}")


    def transfer(self, amount, account):
        try:
            print("\n**********\n\nBeginning Transfer..")
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposite(amount)
            print("\nTransfer complete!\n\n**********")

        except BalanceException as error:
            print(f"\nTransfer interrupted. {error}")


class IntrestRewardsAccount(BankAccount):
    def deposite(self, amount):
        self.balance = self.balance + (amount * 1.05)
        print("\nDeposite complete.")
        self.getBalance()

class SavingsAcc(IntrestRewardsAccount):
    def __init__(self, AccountBalance, AccountName):
        super().__init__(AccountBalance, AccountName)
        self.fee = 5


    def withdraw(self, amount):
        try:
            self.viableTransaction(amount + self.fee)
            self.balance = self.balance - (amount + self.fee)
            print("\nWithdraw completed.")
            self.getBalance()
        except BalanceException as error:
            print(f"\nWithdraw interrupted: {error}")
