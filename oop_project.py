from bank_account import *

Reddy = BankAccount(1000, "Hanumanthareddy H")
Mane = BankAccount(2000, "Sundri")

Reddy.getBalance()
Mane.getBalance()

Reddy.deposit(500)

Reddy.withdraw(811)

Reddy.transfer(200,Mane)

raghu = InterestRewardsAcct(1000,"raghu")
raghu.getBalance()
raghu.deposit(100)
raghu.transfer(100,Reddy)

Smith = SavingAcct(1000,"Smith")
Smith.getBalance()
Smith.deposit(20)
Smith.transfer(100,Reddy)