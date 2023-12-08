from bank_acc import *

kingsley = BankAccount(1000, "Kingsley")
obi = BankAccount(1200, "obi")

kingsley.getBalance()
kingsley.deposite(100)

kingsley.withdraw(20)
kingsley.transfer(67, obi)

obi.getBalance()

victor = IntrestRewardsAccount(100, "Victor")

victor.getBalance
victor.deposite(100)

victor.transfer(100, kingsley)

ada = SavingsAcc(1100, "Ada")

ada.getBalance()
ada.deposite(1000)
ada.transfer(100, kingsley)
