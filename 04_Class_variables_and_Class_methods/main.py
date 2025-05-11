class Bank:
    # Class variable shared by all instances
    bank_name = "Default Bank"

    def __init__(self, account_holder):
        self.account_holder = account_holder

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

    def display(self):
        print(f"Account Holder: {self.account_holder}, Bank Name: {Bank.bank_name}")

# Creating instances
user1 = Bank("Alice")
user2 = Bank("Bob")

# Display initial bank names
user1.display()
user2.display()

# Change bank name using class method
Bank.change_bank_name("Global Trust Bank")

# Display after change
print("\nAfter changing the bank name:")
user1.display()
user2.display()
