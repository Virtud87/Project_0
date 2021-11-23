from typing import List, Type

from data_access_layer.abstract_classes.customer_dao import CustomerDAO
from entities.customers import Customer


class CustomerDAOImplemented(CustomerDAO):
    # a "premade" customer is used strictly for testing purposes
    premade_customer = Customer(1, 1, "Daniel", "Landeros", "d31@gmail.com")
    premade_customer_2 = Customer(2, 2, "Jieun", "Gu", "gu@gmail.com")
    premade_customer_3 = Customer(3, 3, "Goosey", "Bear", "goose@gmail.com")

    # the list below serves as our "database"
    # customer list must contain at least one premade customer in order to run return_customer_by_id
    customer_list = [premade_customer, premade_customer_2, premade_customer_3]
    # we use this generator to assign unique customer ids
    customer_id_generator = 1

    def create_new_customer(self, customer: Customer) -> Customer:
        customer.customer_id = CustomerDAOImplemented.customer_id_generator
        CustomerDAOImplemented.customer_id_generator += 1
        # line below must be commented out when running service test for returning all customers
        CustomerDAOImplemented.customer_list.append(customer)
        return customer

    def return_customer_by_id(self, customer_id: int) -> Customer:
        for customer in CustomerDAOImplemented.customer_list:
            if customer.customer_id == customer_id:
                return customer

    def return_all_customers(self) -> List[Customer]:
        return CustomerDAOImplemented.customer_list

    def update_customer_by_id(self, customer_id) -> Customer:
        for customer_in_list in CustomerDAOImplemented.customer_list:
            if customer_in_list.customer_id == customer_id:
                return customer_in_list

    def delete_customer_by_id(self, customer_id: int) -> Type[bool]:
        for customer_in_list in CustomerDAOImplemented.customer_list:
            if customer_in_list.customer_id == customer_id:
                index = CustomerDAOImplemented.customer_list.index(customer_in_list)
                del CustomerDAOImplemented.customer_list[index]
                return bool
