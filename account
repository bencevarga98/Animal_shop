class Account:
    def __init__(self, name, account_number):
        self.full_name = name
        self.acc_no = account_number
        self.balance = 0

    def get_data(self):
        print(self.full_name, self.acc_no, self.balance)

    def add(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Not enough funds")
        else:
            self.balance -= amount

    def inquire(self):
        return f'Your balance is {self.balance}'

    def __del__(self):
        print("Object deleted")