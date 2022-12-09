class Account():
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        print(f"Account owner: \t\t{self.owner}\nAccount balance: \t${self.balance}")

    def deposit(self, amount=0):
        self.balance = self.balance + amount
        return f"Deposit Accepted, Current Balance: ${self.balance}"

    def withdraw(self, amount=0):
        if self.balance>amount:
            self.balance = self.balance - amount
            return f"Withdrawal Accepted, Current Balance: ${self.balance}"
        else:
            return f"Funds Unavailable, Current Balance: ${self.balance}"

acct1 = Account('Jose', 100)
print(acct1.deposit(50))
print(acct1.withdraw(75))
print(acct1.withdraw(500))