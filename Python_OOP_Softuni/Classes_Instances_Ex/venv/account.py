class Account:

    def __init__(self, id, name, *args):
        self.name = name
        self.id = id
        if args:
            self.balance = args[0]
        else:
            self.balance = 0

    def credit(self, amount):
        self.balance += amount
        return self.balance

    def debit(self, amount):
        if self.balance > amount:
            self.balance -= amount
            return self.balance
        return "Amount exceeded the balance"

    def info(self):
        return f"User {self.name} with account {self.id} has {self.balance} balance"


account = Account(5411256, "Peter")
print(account.debit(500))
print(account.credit(1000))
print(account.debit(500))
print(account.info())
print("#" * 50)
account = Account(1234, "George", 1000)
print(account.credit(500))
print(account.debit(1500))
print(account.info())

