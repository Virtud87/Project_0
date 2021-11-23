import pytest

from data_access_layer.implementation_classes.bank_account_dao_implemented import BankAccountDAOImplemented
from entities.bank_accounts import BankAccount

customer_dao_implementation = BankAccountDAOImplemented()
bank_account = BankAccount(4, 1, 0.00)


def test_create_account():
    new_bank_account: BankAccount = customer_dao_implementation.create_account(bank_account)
    assert new_bank_account.bank_account_id != 0


def test_deposit_into_account_by_id():
    bank_account_id = customer_dao_implementation.deposit_into_account_by_id(1)

def test_withdraw_from_account_by_id():
    pass


def test_transfer_money_between_accounts_by_id():
    pass


def test_get_account_by_id():
    pass


def test_get_all_accounts():
    pass


# def test_get_all_customer_accounts_by_id():
#     pass
