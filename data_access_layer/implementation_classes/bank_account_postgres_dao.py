from typing import List

from data_access_layer.abstract_classes.bank_account_dao import BankAccountDAO
from entities.bank_accounts import BankAccount
from util.database_connection import connection


class BankAccountPostgresDAO(BankAccountDAO):
    def create_account(self, bank_account: BankAccount) -> BankAccount:
        sql = "insert into bank_accounts values(default, %s, %s) returning bank_account_id"
        cursor = connection.cursor()
        cursor.execute(sql, (bank_account.customer_id, bank_account.balance))
        connection.commit()
        generated_id = cursor.fetchone()[0]
        bank_account.bank_account_id = generated_id
        return bank_account

    def deposit_into_account_by_id(self, bank_account_id: int, deposit_amount: float):
        sql = "update bank_accounts set balance = balance + %s where bank_account_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql,
                       (deposit_amount, bank_account_id))
        connection.commit()
        return bank_account_id

    def withdraw_from_account_by_id(self, bank_account_id: int, withdraw_amount: float):
        sql = "update bank_accounts set balance = balance - %s where bank_account_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql,
                       (withdraw_amount, bank_account_id))
        connection.commit()
        return bank_account_id

    def transfer_money_between_accounts_by_id(self, sending: BankAccount, receiving: BankAccount,
                                              amount: float):
        sql = "update bank_accounts set balance = balance - %s where bank_account_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, (amount, sending.bank_account_id))
        connection.commit()
        sql = "update bank_accounts set balance = balance + %s where bank_account_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, (amount, receiving.bank_account_id))
        connection.commit()
        return amount

    def get_account_by_id(self, bank_account_id: int) -> BankAccount:
        sql = "select * from bank_accounts where bank_account_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [bank_account_id])
        account_returned = cursor.fetchone()
        bank_account = BankAccount(*account_returned)
        return bank_account

    def get_all_bank_accounts(self) -> List[BankAccount]:
        sql = "select * from bank_accounts"
        cursor = connection.cursor()
        cursor.execute(sql)
        all_accounts = cursor.fetchall()
        accounts = []
        for account in all_accounts:
            accounts.append(BankAccount(*account))
        return accounts

    def get_all_customer_bank_accounts_by_id(self, customer_id: int) -> List[BankAccount]:
        sql = "select * from bank_accounts where customer_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [customer_id])
        customers_accounts = cursor.fetchall()
        accounts = []
        for account in customers_accounts:
            accounts.append(BankAccount(*account))
        return accounts

    def delete_account_by_id(self, bank_account_id) -> bool:
        sql = "delete from bank_accounts where bank_account_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [bank_account_id])
        connection.commit()
        return True
