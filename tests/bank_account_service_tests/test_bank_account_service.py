from custom_exceptions.account_does_not_exist import AccountDoesNotExist
from custom_exceptions.customer_does_not_exist import CustomerDoesNotExist
from custom_exceptions.empty_database import EmptyDatabase
from custom_exceptions.mulitple_customers_per_account import MultipleCustomersPerAccount
from custom_exceptions.negative_deposit_amount import NegativeDepositAmount
from custom_exceptions.transfer_more_than_available import TransferMoreThanAvailable
from custom_exceptions.withdraw_more_than_available import WithdrawMoreThanAvailable
from data_access_layer.implementation_classes.bank_account_dao_implemented import BankAccountDAOImplemented
from entities.bank_accounts import BankAccount
from service_layer.implemententation_service.bank_account_service_implemented import BankAccountServiceImplemented

bank_account_dao = BankAccountDAOImplemented

bank_account_service = BankAccountServiceImplemented(bank_account_dao)

new_bank_account = BankAccount(1, 2, 0.00)


# def test_validate_service_create_account():
#     try:
#         bank_account_service.service_create_account(new_bank_account)
#         assert False
#     except MultipleCustomersPerAccount as e:
#         assert str(e) == "Can not have multiple customers on same bank account!"


def test_validate_service_deposit_into_account_by_id():
    try:
        bank_account_service.service_deposit_into_account_by_id(1, -100.00)
        assert False
    except NegativeDepositAmount as e:
        assert str(e) == "Can not deposit a negative amount!"


def test_validate_service_withdraw_from_account_by_id():
    try:
        bank_account_service.service_withdraw_from_account_by_id(2, 20.00)
        assert False
    except WithdrawMoreThanAvailable as e:
        assert str(e) == "Can not withdraw more than available balance!"


def test_validate_service_transfer_money_between_accounts_by_id():
    try:
        bank_account_service.service_transfer_money_between_accounts_by_id(300.00, 3, 4)
        assert False
    except TransferMoreThanAvailable as e:
        assert str(e) == "Can not transfer more money than available in balance!"


def test_validate_service_get_account_by_id():
    try:
        bank_account_service.service_get_account_by_id(10)
        assert False
    except AccountDoesNotExist as e:
        assert str(e) == "Bank account does not exist!"


def test_validate_service_get_all_bank_accounts():
    try:
        bank_account_service.service_get_all_bank_accounts()
        assert False
    except EmptyDatabase as e:
        assert str(e) == "There are no bank accounts in database!"


# TODO: figure out WTF is wrong with this test!
def test_validate_service_get_all_customer_bank_accounts_by_id():
    try:
        bank_account_service.service_get_all_customer_bank_accounts_by_id(2)
        assert False
    except CustomerDoesNotExist as e:
        assert str(e) == "Customer does not exist!"
