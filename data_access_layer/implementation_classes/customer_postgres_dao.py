from data_access_layer.abstract_classes.customer_dao import CustomerDAO
from util.database_connection import connection
from entities.customers import Customer


class CustomerPostgresDAO(CustomerDAO):
    def create_new_customer(self, customer: Customer) -> Customer:
        sql = "insert into customers values(default, %s, %s, %s) returning customer_id"
        cursor = connection.cursor()
        # pass in our sql to cursor's execute method, inside a tuple, we then pass in the values for insert command
        cursor.execute(sql, (customer.first_name, customer.last_name, customer.email))
        connection.commit()
        customer_id = cursor.fetchone()[0]
        customer.customer_id = customer_id
        return customer

    def return_customer_by_id(self, customer_id: int) -> Customer:
        sql = "select * from customers where customer_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [customer_id])
        customer_record = cursor.fetchone()
        customer = Customer(*customer_record)
        return customer

    def return_all_customers(self):
        sql = "select * from customers"
        cursor = connection.cursor()
        cursor.execute(sql)
        customer_records = cursor.fetchall()
        customer_list = []
        for customer in customer_records:
            customer_list.append(Customer(*customer))
        return customer_list

    def update_customer_by_id(self, customer: Customer) -> Customer:
        sql = "update customers set first_name = %s, last_name = %s, email = %s where customer_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, (customer.first_name, customer.last_name, customer.email, customer.customer_id))
        connection.commit()
        return customer

    def delete_customer_by_id(self, customer_id: int) -> bool:
        sql = "delete from customers where customer_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [customer_id])
        connection.commit()
        return True
