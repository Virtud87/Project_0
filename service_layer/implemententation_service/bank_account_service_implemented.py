from typing import List

from custom_exceptions.account_does_not_exist import AccountDoesNotExist
from custom_exceptions.customer_does_not_exist import CustomerDoesNotExist
from custom_exceptions.empty_database import EmptyDatabase
from custom_exceptions.mulitple_customers_per_account import MultipleCustomersPerAccount
from custom_exceptions.negative_deposit_amount import NegativeDepositAmount
from custom_exceptions.transfer_more_than_available import TransferMoreThanAvailable
from custom_exceptions.withdraw_more_than_available import WithdrawMoreThanAvailable
from data_access_layer.implementation_classes.bank_account_dao_implemented import BankAccountDAOImplemented
from entities.bank_accounts import BankAccount
from service_layer.abstract_service.bank_account_service import BankAccountService


class BankAccountServiceImplemented(BankAccountService):
    def __init__(self, bank_account_dao):
        self.bank_account_dao: BankAccountDAOImplemented = bank_account_dao

    def service_create_account(self, bank_account: BankAccount) -> BankAccount:
        for account in self.bank_account_dao.bank_accounts_list:
            if account.bank_account_id == bank_account.bank_account_id and account.customer_id != bank_account.customer_id:
                raise MultipleCustomersPerAccount("Can not have multiple customers on same bank account!")
            return self.bank_account_dao.create_account(bank_account)

    def service_deposit_into_account_by_id(self, bank_account_id: int, deposit_amount: float) -> BankAccount:
        for account in self.bank_account_dao.bank_accounts_list:
            if account.bank_account_id == bank_account_id:
                if deposit_amount < 0:
                    raise NegativeDepositAmount("Can not deposit a negative amount!")
                account.balance += deposit_amount
                return self.bank_account_dao.deposit_into_account_by_id(bank_account_id, deposit_amount)

    def service_withdraw_from_account_by_id(self, bank_account_id: int, withdraw_amount: float) -> BankAccount:
        for account in self.bank_account_dao.bank_accounts_list:
            if account.bank_account_id == bank_account_id:
                if withdraw_amount > account.balance:
                    raise WithdrawMoreThanAvailable("Can not withdraw more than available balance!")
                account.balance -= withdraw_amount
                return self.bank_account_dao.withdraw_from_account_by_id(bank_account_id, withdraw_amount)

    def service_transfer_money_between_accounts_by_id(self, transfer_amount: float, send_id: int, receive_id: int) -> \
            List[BankAccount]:
        for account in self.bank_account_dao.bank_accounts_list:
            if account.bank_account_id == send_id:
                if account.balance < transfer_amount:
                    raise TransferMoreThanAvailable("Can not transfer more money than available in balance!")
                return self.bank_account_dao.transfer_money_between_accounts_by_id(transfer_amount, send_id, receive_id)

    def service_get_account_by_id(self, bank_account_id: int) -> BankAccount:
        for account in self.bank_account_dao.bank_accounts_list:
            if account.bank_account_id != bank_account_id:
                raise AccountDoesNotExist("Bank account does not exist!")
            return self.bank_account_dao.get_account_by_id(bank_account_id)

    def service_get_all_bank_accounts(self) -> List[BankAccount]:
        if not self.bank_account_dao.bank_accounts_list:
            raise EmptyDatabase("There are no bank accounts in database!")
        return self.bank_account_dao.bank_accounts_list

    def service_get_all_customer_bank_accounts_by_id(self, customer_id: int) -> List[BankAccount]:
        customer_bank_accounts = []
        for account in self.bank_account_dao.bank_accounts_list:
            if account.customer_id == customer_id:
                customer_bank_accounts.append(account)
                return customer_bank_accounts
            return self.bank_account_dao.get_all_customer_bank_accounts_by_id(customer_id)
        raise CustomerDoesNotExist("Customer does not exist!")


