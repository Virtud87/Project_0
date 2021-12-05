from typing import List

from custom_exceptions.account_does_not_exist import AccountDoesNotExist
from custom_exceptions.customer_does_not_exist import CustomerDoesNotExist
from custom_exceptions.empty_database import EmptyDatabase
from custom_exceptions.negative_deposit_amount import NegativeDepositAmount
from custom_exceptions.transfer_more_than_available import TransferMoreThanAvailable
from custom_exceptions.withdraw_more_than_available import WithdrawMoreThanAvailable
from custom_exceptions.withdraw_negative_amount import WithdrawNegativeAmount
from data_access_layer.implementation_classes.bank_account_postgres_dao import BankAccountPostgresDAO
from entities.bank_accounts import BankAccount
from service_layer.abstract_service.bank_account_service import BankAccountService


class BankAccountPostgresService(BankAccountService):
    def __init__(self, bank_account_dao: BankAccountPostgresDAO):
        self.bank_account_dao = bank_account_dao

    def service_create_account(self, bank_account: BankAccount) -> BankAccount:
        return self.bank_account_dao.create_account(bank_account)

    def service_deposit_into_account_by_id(self, bank_account_id: int, deposit_amount: float):
        if deposit_amount < 0:
            raise NegativeDepositAmount("Can not deposit a negative amount!")
        return self.bank_account_dao.deposit_into_account_by_id(bank_account_id, deposit_amount)

    def service_withdraw_from_account_by_id(self, bank_account_id: int, withdraw_amount: float):
        account = self.bank_account_dao.get_account_by_id(bank_account_id)
        if account.balance < withdraw_amount:
            raise WithdrawMoreThanAvailable("Can not withdraw more than available balance!")
        if withdraw_amount < 0:
            raise WithdrawNegativeAmount("Can not withdraw a negative amount!")
        return self.bank_account_dao.withdraw_from_account_by_id(bank_account_id, withdraw_amount)

    def service_transfer_money_between_accounts_by_id(self, sending: BankAccount, receiving: BankAccount,
                                                      amount: float) -> bool:
        sending_account = self.bank_account_dao.get_account_by_id(sending.bank_account_id)
        receiving_account = self.bank_account_dao.get_account_by_id(receiving.bank_account_id)
        if sending_account.balance < amount:
            raise TransferMoreThanAvailable("Can not transfer more money than available in balance!")
        return self.bank_account_dao.transfer_money_between_accounts_by_id(sending_account, receiving_account, amount)

    def service_get_account_by_id(self, bank_account_id: int) -> BankAccount:
        accounts = self.bank_account_dao.get_all_bank_accounts()
        for account in accounts:
            if account.bank_account_id == bank_account_id:
                return self.bank_account_dao.get_account_by_id(bank_account_id)
        raise AccountDoesNotExist("Bank account does not exist!")

    def service_get_all_bank_accounts(self) -> List[BankAccount]:
        accounts = self.bank_account_dao.get_all_bank_accounts()
        if len(accounts) == 0:
            raise EmptyDatabase("There are no bank accounts in database!")
        return self.bank_account_dao.get_all_bank_accounts()

    def service_get_all_customer_bank_accounts_by_id(self, customer_id: int) -> List[BankAccount]:
        return self.bank_account_dao.get_all_customer_bank_accounts_by_id(customer_id)

    def service_delete_account_by_id(self, bank_account_id) -> bool:
        return self.bank_account_dao.delete_account_by_id(bank_account_id)
