from data_access_layer.implementation_classes.bank_account_postgres_dao import BankAccountPostgresDAO
from entities.bank_accounts import BankAccount

customer_dao_implementation = BankAccountPostgresDAO()

# testing create account
bank_account = BankAccount(0, 1, 0.00)

# testing transfer
sending = BankAccount(3, 1, 0.00)
receiving = BankAccount(1, 1, 0.00)


def test_create_account():
    new_bank_account: BankAccount = customer_dao_implementation.create_account(bank_account)
    assert new_bank_account.bank_account_id != 0


def test_deposit_into_account_by_id():
    deposited = customer_dao_implementation.deposit_into_account_by_id(1, 5.00)
    assert bool(deposited)


def test_withdraw_from_account_by_id():
    withdrawn = customer_dao_implementation.withdraw_from_account_by_id(1, 1.00)
    assert bool(withdrawn)


def test_transfer_money_between_accounts_by_id():
    transferred = customer_dao_implementation.transfer_money_between_accounts_by_id(sending, receiving, 1.00)
    assert bool(transferred)


def test_get_account_by_id():
    bank_account_returned = customer_dao_implementation.get_account_by_id(1)
    assert bank_account_returned.bank_account_id == 1


def test_get_all_accounts():
    returned_list = customer_dao_implementation.get_all_bank_accounts()
    assert len(returned_list) >= 2


def test_get_all_customer_accounts_by_id():
    returned_list = customer_dao_implementation.get_all_customer_bank_accounts_by_id(1)
    assert len(returned_list) > 1


def test_delete_account_by_id():
    account_deleted = customer_dao_implementation.delete_account_by_id(1)
    assert account_deleted
