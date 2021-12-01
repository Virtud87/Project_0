from abc import ABC, abstractmethod
from typing import List

from entities.bank_accounts import BankAccount


class BankAccountService(ABC):
    @abstractmethod
    def service_create_account(self, bank_account: BankAccount) -> BankAccount:
        pass

    @abstractmethod
    def service_deposit_into_account_by_id(self, bank_account_id: int, deposit_amount: float) -> BankAccount:
        pass

    @abstractmethod
    def service_withdraw_from_account_by_id(self, bank_account_id: int, withdraw_amount: float) -> BankAccount:
        pass

    @abstractmethod
    def service_transfer_money_between_accounts_by_id(self, transfer_amount: float, send_id: int,
                                                      receive_id: int) -> List[BankAccount]:
        pass

    @abstractmethod
    def service_get_account_by_id(self, bank_account_id: int) -> BankAccount:
        pass

    @abstractmethod
    def service_get_all_bank_accounts(self) -> List[BankAccount]:
        pass

    @abstractmethod
    def service_get_all_customer_bank_accounts_by_id(self, customer_id: int) -> List[BankAccount]:
        pass
