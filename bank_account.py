""""
Task: To implement bank account
Bank account funtionalities: deposit, withdrawl, and balance information
"""

# comment

class BankAccount:
    def __init__(self):
        self._balance = 0.0

    
    def deposit(self, amount):
        self._balance += amount

    def withdrawal(self, amount):
        if amount > self._balance:
            print(f"Insufficient funds")
            return
        self._balance -= amount

    def show_balance(self):
        print(f"Your balance is: {self._balance:,.2f}$")


acc1 = BankAccount()
acc1.deposit(100)
acc1.withdrawal(1000)
acc1.show_balance() 