import pytest

from data_access_layer.implementation_classes.bank_account_dao_implemented import BankAccountDAOImplemented
from entities.bank_accounts import BankAccount

customer_dao_implementation = BankAccountDAOImplemented()

# line below is for testing create account
bank_account = BankAccount(4, 1, 0.00)

transfer_1 = BankAccount(1, 1, 10.00)
transfer_2 = BankAccount(2, 1, 10.00)


def test_create_account():
    new_bank_account: BankAccount = customer_dao_implementation.create_account(bank_account)
    assert new_bank_account.bank_account_id != 0


def test_deposit_into_account_by_id():
    bank_account_deposited: BankAccount = customer_dao_implementation.deposit_into_account_by_id(1, 5.00)
    assert bank_account_deposited.balance > 10.00


def test_withdraw_from_account_by_id():
    bank_account_withdrawn: BankAccount = customer_dao_implementation.withdraw_from_account_by_id(2, 5.00)
    assert bank_account_withdrawn.balance < 10.00


def test_transfer_money_between_accounts_by_id():
    transferred = customer_dao_implementation.transfer_money_between_accounts_by_id(50.00, 3, 4)
    assert bool(transferred)


def test_get_account_by_id():
    bank_account_returned = customer_dao_implementation.get_account_by_id(1)
    assert bank_account_returned.bank_account_id == 1


def test_get_all_accounts():
    returned_list = customer_dao_implementation.get_all_bank_accounts()
    assert len(returned_list) >= 2


def test_get_all_customer_accounts_by_id():
    returned_list = customer_dao_implementation.get_all_customer_bank_accounts_by_id(2)
    assert len(returned_list) > 0
