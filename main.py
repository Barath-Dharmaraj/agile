import random

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        self.transaction_history = []

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Deposited: ${amount}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew: ${amount}")
        else:
            self.transaction_history.append(f"Failed Withdrawal: ${amount}")

    def get_summary(self):
        return f"Account: {self.owner} | Balance: ${self.balance}"

def run_bank_simulation():
    # Pre-defined data instead of reading user input
    clients = ["Alice Smith", "Bob Johnson", "Charlie Brown"]
    accounts = []

    print("--- 2026 Automated Bank System ---")
    
    # 1. Initialize accounts
    for name in clients:
        initial_fund = random.randint(1000, 5000)
        acc = BankAccount(name, initial_fund)
        accounts.append(acc)
        print(f"System: Created account for {name} with ${initial_fund}")

    # 2. Automated Transactions (No IP needed)
    for acc in accounts:
        # Simulate a series of random banking actions
        acc.deposit(random.randint(100, 500))
        acc.withdraw(random.randint(50, 600))
        acc.deposit(200)
        
    # 3. Generate Final Report
    print("\n" + "="*30)
    print("FINAL BANKING REPORT")
    print("="*30)
    
    for acc in accounts:
        print(acc.get_summary())
        for txn in acc.transaction_history:
            print(f"  - {txn}")
        print("-" * 20)

if __name__ == "__main__":
    run_bank_simulation()
