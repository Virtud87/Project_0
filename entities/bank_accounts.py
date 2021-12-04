# import decimal


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

    def __str__(self):
        return f"bank account id: {self.bank_account_id}, customer id: {self.customer_id}, balance: {self.balance}"
