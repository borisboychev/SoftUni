class Account:

    def __init__(self, owner, amount = 0):
        self.owner = owner
        self.amount = amount
        self._transaction = []

    def add_transaction(self, amount):
        if isinstance(amount, int):
            self._transaction.append(amount)
        else:
            raise ValueError("please use int for amount")

    def balance(self):
        return self.amount + sum(self._transaction)

    def validate_transaction(self, account: Account, amount_to_add):
        if account.amount >= amount_to_add:
            account._transaction.append(amount_to_add)
            return f'New balance: {account.balance()}'

    def __str__(self):
        return f'Account of {self.owner} with starting amount {self.amount}'