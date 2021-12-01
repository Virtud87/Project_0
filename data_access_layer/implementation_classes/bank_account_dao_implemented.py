from typing import List

from data_access_layer.abstract_classes.bank_account_dao import BankAccountDAO
from entities.bank_accounts import BankAccount


class BankAccountDAOImplemented(BankAccountDAO):
    premade_bank_account = BankAccount(1, 1, 10.00)
    premade_bank_account_2 = BankAccount(2, 1, 10.00)
    premade_bank_account_3 = BankAccount(3, 2, 200.00)
    premade_bank_account_4 = BankAccount(4, 2, 250.00)
    # premade_bank_account, premade_bank_account_2, premade_bank_account_3, premade_bank_account_4
    bank_accounts_list = [premade_bank_account, premade_bank_account_2, premade_bank_account_3, premade_bank_account_4]
    bank_account_id_generator = 5

    def create_account(self, bank_account: BankAccount) -> BankAccount:
        bank_account.bank_account_id = BankAccountDAOImplemented.bank_account_id_generator
        BankAccountDAOImplemented.bank_account_id_generator += 1
        BankAccountDAOImplemented.bank_accounts_list.append(bank_account)
        return bank_account

    def deposit_into_account_by_id(self, bank_account_id: int, deposit_amount: float) -> BankAccount:
        for account in BankAccountDAOImplemented.bank_accounts_list:
            if account.bank_account_id == bank_account_id:
                account.balance += deposit_amount
                return account

    def withdraw_from_account_by_id(self, bank_account_id: int, withdraw_amount: float) -> BankAccount:
        for account in BankAccountDAOImplemented.bank_accounts_list:
            if account.bank_account_id == bank_account_id:
                account.balance -= withdraw_amount
                return account

    def transfer_money_between_accounts_by_id(self, transfer_amount: float, send_id: int,
                                              receive_id: int) -> List[BankAccount]:
        updated_accounts = []
        for account in BankAccountDAOImplemented.bank_accounts_list:
            if account.bank_account_id == send_id:
                account.balance -= transfer_amount
                updated_accounts.append(account)
            if account.bank_account_id == receive_id:
                account.balance += transfer_amount
                updated_accounts.append(account)
        return updated_accounts

    def get_account_by_id(self, bank_account_id: int) -> BankAccount:
        for account in BankAccountDAOImplemented.bank_accounts_list:
            if account.bank_account_id == bank_account_id:
                return account

    def get_all_bank_accounts(self) -> List[BankAccount]:
        return BankAccountDAOImplemented.bank_accounts_list

    def get_all_customer_bank_accounts_by_id(self, customer_id: int) -> List[BankAccount]:
        customer_bank_accounts_list = []
        for account in BankAccountDAOImplemented.bank_accounts_list:
            if account.customer_id == customer_id:
                customer_bank_accounts_list.append(account)
                return customer_bank_accounts_list
