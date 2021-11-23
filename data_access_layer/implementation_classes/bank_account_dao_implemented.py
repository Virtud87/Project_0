from typing import List

from data_access_layer.abstract_classes.bank_account_dao import BankAccountDAO
from entities.bank_accounts import BankAccount


class BankAccountDAOImplemented(BankAccountDAO):
    premade_bank_account = BankAccount(1, 1, 0.00)
    bank_accounts = []
    bank_account_id_generator = 1

    def create_account(self, bank_account: BankAccount) -> BankAccount:
        bank_account.bank_account_id = BankAccountDAOImplemented.bank_account_id_generator
        BankAccountDAOImplemented.bank_account_id_generator += 1
        BankAccountDAOImplemented.bank_accounts.append(bank_account)
        return bank_account

    def deposit_into_account_by_id(self, bank_account_id: int) -> bool:
        pass

    def withdraw_from_account_by_id(self, bank_account_id: int) -> bool:
        pass

    def transfer_money_between_accounts_by_id(self, *bank_account_id: int) -> bool:
        pass

    def get_account_by_id(self, bank_account_id: int) -> BankAccount:
        pass

    def get_all_bank_accounts(self) -> List[BankAccount]:
        pass

    def get_all_customer_bank_accounts_by_id(self, customer_id: int) -> List[BankAccount]:
        pass
