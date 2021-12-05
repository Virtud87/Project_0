from flask import Flask, request, jsonify, render_template

from custom_exceptions.account_does_not_exist import AccountDoesNotExist
from custom_exceptions.customer_already_exists import CustomerAlreadyExists
from custom_exceptions.customer_does_not_exist import CustomerDoesNotExist
from custom_exceptions.empty_database import EmptyDatabase
from custom_exceptions.negative_deposit_amount import NegativeDepositAmount
from custom_exceptions.transfer_more_than_available import TransferMoreThanAvailable
from custom_exceptions.withdraw_more_than_available import WithdrawMoreThanAvailable
from custom_exceptions.withdraw_negative_amount import WithdrawNegativeAmount
from data_access_layer.implementation_classes.bank_account_postgres_dao import BankAccountPostgresDAO
from data_access_layer.implementation_classes.customer_postgres_dao import CustomerPostgresDAO
from entities.bank_accounts import BankAccount
from entities.customers import Customer
from service_layer.implemententation_service.bank_account_postgres_service import BankAccountPostgresService
from service_layer.implemententation_service.customer_postgres_service import CustomerPostgresService
import logging

logging.basicConfig(filename="records.log", level=logging.DEBUG, format=f"%(asctime)s %(levelname)s %(message)s")

app: Flask = Flask(__name__, template_folder="templates")

customer_dao = CustomerPostgresDAO()
customer_service = CustomerPostgresService(customer_dao)

bank_account_dao = BankAccountPostgresDAO()
bank_account_service = BankAccountPostgresService(bank_account_dao)


# @app.route("/")
# def home():
#     return render_template("index.html")


# CUSTOMERS
@app.post("/customer")
def create_new_customer():
    try:
        # first step converts the json into a dictionary
        customer_data = request.get_json()
        # creates a new customer object to pass to service, validate, then pass it to the DAO
        new_customer = Customer(
            customer_data["customerId"],
            customer_data["firstName"],
            customer_data["lastName"],
            customer_data["email"])
        # passes new customer object to service layer
        customer_returned = customer_service.service_create_new_customer(new_customer)
        # converts new customer object into dictionary
        customer_as_dictionary = customer_returned.create_customer_dictionary()
        # converts the object into a json
        return jsonify(customer_as_dictionary)
    except CustomerAlreadyExists as e:
        exception_dictionary = {"message": str(e)}
        return jsonify(exception_dictionary)


@app.get("/customer/<customer_id>")
def return_customer_by_id(customer_id: str):
    try:
        customer_returned = customer_service.service_return_customer_by_id(int(customer_id))
        customer_as_dictionary = customer_returned.create_customer_dictionary()
        return jsonify(customer_as_dictionary)
    except CustomerDoesNotExist as e:
        exception_dictionary = {"message": str(e)}
        return jsonify(exception_dictionary)


@app.get("/customers")
def return_all_customers():
    try:
        customer_list_returned = customer_service.service_return_all_customers()
        customer_list = []
        for customer in customer_list_returned:
            customer_list.append(customer.create_customer_dictionary())
        return jsonify(customer_list)
    except EmptyDatabase as e:
        exception_dictionary = {"message": str(e)}
        return jsonify(exception_dictionary)


@app.patch("/customer/<customer_id>")
def update_customer_by_id(customer_id: str):
    try:
        customer_data = request.get_json()
        customer_to_be_updated = Customer(
            int(customer_id),
            customer_data["firstName"],
            customer_data["lastName"],
            customer_data["email"])
        customer_updated = customer_service.service_update_customer_by_id(customer_to_be_updated)
        return "Customer was updated successfully! " + str(customer_updated)
    except CustomerDoesNotExist as e:
        exception_dictionary = {"message": str(e)}
        return jsonify(exception_dictionary)


@app.delete("/customer/<customer_id>")
def delete_customer_by_id(customer_id: str):
    try:
        deleted = customer_service.service_delete_customer_by_id(int(customer_id))
        if deleted:
            return f"Customer of ID {customer_id} was deleted successfully!"
        return f"Something went wrong. Customer of Id {customer_id} was not deleted."
    except CustomerDoesNotExist as e:
        exception_dictionary = {"message": str(e)}
        return jsonify(exception_dictionary)


# BANK ACCOUNTS
@app.post("/account")
def create_account():
    account_data = request.get_json()
    new_account = BankAccount(
        account_data["bankAccountId"],
        account_data["customerId"],
        account_data["balance"])
    bank_account_returned = bank_account_service.service_create_account(new_account)
    bank_account_as_dictionary = bank_account_returned.create_bank_account_dictionary()
    return jsonify(bank_account_as_dictionary)


@app.post("/deposit/<bank_account_id>")
def deposit_into_account_by_id(bank_account_id: str):
    try:
        deposit_dict = request.get_json()
        deposit_amount = deposit_dict["depositAmount"]
        deposited = bank_account_service.service_deposit_into_account_by_id(int(bank_account_id), float(deposit_amount))
        return f"Deposit into account of ID {deposited} successful!"
    except NegativeDepositAmount as e:
        exception_dictionary = {"message": str(e)}
        return jsonify(exception_dictionary)


@app.post("/withdraw/<bank_account_id>")
def withdraw_from_account_by_id(bank_account_id: str):
    try:
        withdraw_dict = request.get_json()
        withdraw_amount = withdraw_dict["withdrawAmount"]
        withdrawn = bank_account_service.service_withdraw_from_account_by_id(int(bank_account_id), float(withdraw_amount))
        return f"Withdrawal from account of ID {withdrawn} successful!"
    except WithdrawMoreThanAvailable as e:
        exception_dictionary = {"message": str(e)}
        return jsonify(exception_dictionary)
    except WithdrawNegativeAmount as e:
        exception_dictionary = {"message": str(e)}
        return jsonify(exception_dictionary)


@app.post("/transfer/<bank_account_id>/<bank_account_id_2>")
def transfer_money_between_accounts_by_id(bank_account_id: str, bank_account_id_2: str):
    try:
        transfer_dict = request.get_json()
        transfer_amount = transfer_dict["transferAmount"]
        sending = bank_account_service.service_get_account_by_id(int(bank_account_id))
        receiving = bank_account_service.service_get_account_by_id(int(bank_account_id_2))
        transferred = bank_account_service.service_transfer_money_between_accounts_by_id(sending, receiving,
                                                                                         transfer_amount)
        return "Transfer successful! Transfer amount = $" + str(transferred)
    except TransferMoreThanAvailable as e:
        exception_dictionary = {"message": str(e)}
        return jsonify(exception_dictionary)


@app.get("/account/<bank_account_id>")
def get_account_by_id(bank_account_id: str):
    try:
        account = bank_account_service.service_get_account_by_id(int(bank_account_id))
        account_as_dict = account.create_bank_account_dictionary()
        return jsonify(account_as_dict)
    except AccountDoesNotExist as e:
        exception_dictionary = {"message": str(e)}
        return jsonify(exception_dictionary)


@app.get("/accounts")
def get_all_bank_accounts():
    try:
        accounts = bank_account_service.service_get_all_bank_accounts()
        list_of_account_dict = []
        for account in accounts:
            account_as_dict = account.create_bank_account_dictionary()
            list_of_account_dict.append(account_as_dict)
        return jsonify(list_of_account_dict)
    except EmptyDatabase as e:
        exception_dictionary = {"message": str(e)}
        return jsonify(exception_dictionary)


@app.get("/accounts/<customer_id>")
def get_all_customer_bank_accounts_by_id(customer_id: str):
    try:
        accounts = bank_account_service.service_get_all_customer_bank_accounts_by_id(int(customer_id))
        list_of_account_dict = []
        for account in accounts:
            account_as_dict = account.create_bank_account_dictionary()
            list_of_account_dict.append(account_as_dict)
        return jsonify(list_of_account_dict)
    except CustomerDoesNotExist as e:
        exception_dictionary = {"message": str(e)}
        return jsonify(exception_dictionary)


@app.delete("/account/<bank_account_id>")
def service_delete_account_by_id(bank_account_id: str):
    deleted = bank_account_service.service_delete_account_by_id(int(bank_account_id))
    if deleted:
        return f"Bank account of ID {bank_account_id} successfully deleted."
    return f"Error: bank account of ID {bank_account_id} not deleted."


app.run()
