from custom_exceptions.account_does_not_exist import AccountDoesNotExist
from custom_exceptions.customer_does_not_exist import CustomerDoesNotExist
from custom_exceptions.empty_database import EmptyDatabase
from custom_exceptions.negative_deposit_amount import NegativeDepositAmount
from custom_exceptions.transfer_more_than_available import TransferMoreThanAvailable
from custom_exceptions.withdraw_more_than_available import WithdrawMoreThanAvailable
from custom_exceptions.withdraw_negative_amount import WithdrawNegativeAmount
from data_access_layer.implementation_classes.bank_account_postgres_dao import BankAccountPostgresDAO
from data_access_layer.implementation_classes.customer_postgres_dao import CustomerPostgresDAO
from entities.bank_accounts import BankAccount

from service_layer.implemententation_service.bank_account_postgres_service import BankAccountPostgresService

bank_account_dao = BankAccountPostgresDAO()
bank_account_service = BankAccountPostgresService(bank_account_dao)

# test transfer
sending = BankAccount(3, 1, 0.00)
receiving = BankAccount(1, 1, 0.00)


def test_validate_service_deposit_into_account_by_id():
    try:
        bank_account_service.service_deposit_into_account_by_id(1, 100.00)
        assert False
    except NegativeDepositAmount as e:
        assert str(e) == "Can not deposit a negative amount!"


def test_validate_service_withdraw_from_account_by_id():
    try:
        bank_account_service.service_withdraw_from_account_by_id(1, 1000.00)
        assert False
    except WithdrawMoreThanAvailable as e:
        assert str(e) == "Can not withdraw more than available balance!"
    except WithdrawNegativeAmount as e:
        assert str(e) == "Can not withdraw a negative amount!"


def test_validate_service_transfer_money_between_accounts_by_id():
    try:
        bank_account_service.service_transfer_money_between_accounts_by_id(sending, receiving, 1.00)
        assert False
    except TransferMoreThanAvailable as e:
        assert str(e) == "Can not transfer more money than available in balance!"


def test_validate_service_get_account_by_id():
    try:
        bank_account_service.service_get_account_by_id(1)
        assert False
    except AccountDoesNotExist as e:
        assert str(e) == "Bank account does not exist!"


def test_validate_service_get_all_bank_accounts():
    try:
        bank_account_service.service_get_all_bank_accounts()
        assert False
    except EmptyDatabase as e:
        assert str(e) == "There are no bank accounts in database!"


def test_validate_service_delete_account_by_id():
    try:
        bank_account_service.service_delete_account_by_id(7)
        assert False
    except AccountDoesNotExist as e:
        assert str(e) == "Bank account does not exist!"
