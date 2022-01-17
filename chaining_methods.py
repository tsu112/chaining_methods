class User:
    def __init__(self, name):
        self.name = name
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_witdrawal(self, amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.account_balance}")
        return self

    def make_transfer(self, amount, user):
        self.account_balance -= amount
        user.account_balance += amount
        self.display_user_balance()
        user.display_user_balance()


guido = User("Guido")
monty = User("Monty")
sue = User("Sue")

guido.make_deposit(100).display_user_balance().make_deposit(
    200).make_witdrawal(50).display_user_balance()
# guido.make_deposit(100)
# guido.make_deposit(200)
# guido.make_witdrawal(50)
# guido.display_user_balance()

monty.make_deposit(100).make_deposit(100).make_witdrawal(
    50).make_witdrawal(50).display_user_balance()
# monty.make_deposit(100)
# monty.make_witdrawal(50)
# monty.make_witdrawal(50)
# monty.display_user_balance()

sue.make_deposit(100).make_witdrawal(100).make_witdrawal(
    50).make_witdrawal(50).display_user_balance()
# sue.make_witdrawal(100)
# sue.make_witdrawal(50)
# sue.make_witdrawal(50)
# sue.display_user_balance()

monty.make_transfer(100, sue)
