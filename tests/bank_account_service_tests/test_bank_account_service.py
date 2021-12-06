from custom_exceptions.account_does_not_exist import AccountDoesNotExist
from custom_exceptions.negative_deposit_amount import NegativeDepositAmount
from custom_exceptions.transfer_more_than_available import TransferMoreThanAvailable
from custom_exceptions.withdraw_more_than_available import WithdrawMoreThanAvailable
from custom_exceptions.withdraw_negative_amount import WithdrawNegativeAmount
from data_access_layer.implementation_classes.bank_account_postgres_dao import BankAccountPostgresDAO
from entities.bank_accounts import BankAccount

from service_layer.implemententation_service.bank_account_postgres_service import BankAccountPostgresService

bank_account_dao = BankAccountPostgresDAO()
bank_account_service = BankAccountPostgresService(bank_account_dao)

# test transfer
sending = BankAccount(1, 3, 0.00)
receiving = BankAccount(3, 2, 0.00)


def test_validate_service_deposit_into_account_by_id():
    try:
        bank_account_service.service_deposit_into_account_by_id(1, -100.00)
        assert False
    except NegativeDepositAmount as e:
        assert str(e) == "Can not deposit a negative amount!"


# when running these tests, have to make amount negative to raise second exception
def test_validate_service_withdraw_from_account_by_id():
    try:
        bank_account_service.service_withdraw_from_account_by_id(1, 2.00)
        assert False
    except WithdrawMoreThanAvailable as e:
        assert str(e) == "Can not withdraw more than available balance!"
    except WithdrawNegativeAmount as e:
        assert str(e) == "Can not withdraw a negative amount!"


def test_validate_service_transfer_money_between_accounts_by_id():
    try:
        bank_account_service.service_transfer_money_between_accounts_by_id(sending, receiving, 2.00)
        assert False
    except TransferMoreThanAvailable as e:
        assert str(e) == "Can not transfer more money than available in balance!"


def test_validate_service_get_account_by_id():
    try:
        bank_account_service.service_get_account_by_id(5)
        assert False
    except AccountDoesNotExist as e:
        assert str(e) == "Bank account does not exist!"
