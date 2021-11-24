class Customer:
    def __init__(self, customer_id: int, bank_account_id: int, first_name: str, last_name: str, email: str):
        self.customer_id = customer_id
        self.bank_account_id = bank_account_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def create_customer_dictionary(self):
        return {
            "customerId": self.customer_id,
            "bankAccountId": self.bank_account_id,
            "firstName": self.first_name,
            "lastName": self.last_name,
            "email": self.email
        }

    def __str__(self):
        return "customer ID: {}, bank account ID: {}, first name: {}, last name: {}, email: {}".format(
            self.customer_id,
            self.bank_account_id,
            self.first_name,
            self.last_name,
            self.email
        )
