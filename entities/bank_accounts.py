class BankAccount:
    def __init__(self, bank_account_id: int, customer_id: int, balance: float):
        self.bank_account_id = bank_account_id
        self.customer_id = customer_id
        self.balance = balance

    def create_bank_account_dictionary(self):
        return {
            "bankAccountId": self.bank_account_id,
            "customerId": self.customer_id,
            "balance": self.balance
        }
