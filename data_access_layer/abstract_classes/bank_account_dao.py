from abc import ABC, abstractmethod
from typing import List

from entities.bank_accounts import BankAccount


class BankAccountDAO(ABC):
    @abstractmethod
    def create_account(self, bank_account: BankAccount) -> BankAccount:
        pass

    @abstractmethod
    def deposit_into_account_by_id(self, bank_account: BankAccount, deposit_amount: float) -> BankAccount:
        pass

    @abstractmethod
    def withdraw_from_account_by_id(self, bank_account: BankAccount, withdraw_amount: float) -> BankAccount:
        pass

    @abstractmethod
    def transfer_money_between_accounts_by_id(self, sending: BankAccount, receiving: BankAccount, amount: float) -> bool:
        pass

    @abstractmethod
    def get_account_by_id(self, bank_account_id: int) -> BankAccount:
        pass

    @abstractmethod
    def get_all_bank_accounts(self) -> List[BankAccount]:
        pass

    @abstractmethod
    def get_all_customer_bank_accounts_by_id(self, customer_id: int) -> List[BankAccount]:
        pass

    @abstractmethod
    def delete_account_by_id(self, bank_account: BankAccount) -> bool:
        pass
