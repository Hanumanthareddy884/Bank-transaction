from bank_account import *

Reddy = BankAccount(1000, "Hanumanthareddy H")
Mane = BankAccount(2000, "Sundri")

Reddy.getBalance()
Mane.getBalance()

Reddy.deposit(500)

Reddy.withdraw(811)

Reddy.transfer(200,Mane)