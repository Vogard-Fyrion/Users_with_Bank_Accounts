
class BankAccount:
    def __init__(self, interest_rate, balance):
        self.interest_rate = interest_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance - amount < 0:
            print("Insufficient funds: Chargina $5 fee")
            self.balance -= 5
        else:
            self.balance -= amount
        return self

    def display_account_info(self):
        print(f"Balance: ${self.balance}, Interest rate {self.interest_rate}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.interest_rate
        return self

class User:
    bank_name = "First National Dojo"
    def __init__(self , name, email_address):
        self.name = name
        self.email = email_address
        self.account = BankAccount()

    def make_deposit(self, amount):
        self.account.balance += amount
    
    def make_withdrawal(self, amount):
        self.account.balance -= amount

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.account.balance}")

    def transfer_money(self, amount, reciever):
        self.account.balance -= amount
        reciever.account.balance += amount
