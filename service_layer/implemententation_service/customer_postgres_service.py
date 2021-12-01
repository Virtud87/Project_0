from custom_exceptions.customer_already_exists import CustomerAlreadyExists
from custom_exceptions.customer_does_not_exist import CustomerDoesNotExist
from custom_exceptions.empty_database import EmptyDatabase
from data_access_layer.implementation_classes.customer_postgres_dao import CustomerPostgresDAO
from entities.customers import Customer
from service_layer.abstract_service.customer_service import CustomerService


class CustomerPostgresService(CustomerService):
    def __init__(self, customer_dao: CustomerPostgresDAO):
        self.customer_dao = customer_dao

    def service_create_new_customer(self, customer: Customer) -> Customer:
        customers = self.customer_dao.return_all_customers()
        for customer_in_list in customers:
            if customer_in_list.email == customer.email:
                raise CustomerAlreadyExists("This customer already exists!")
        return self.customer_dao.create_new_customer(customer)

    def service_return_customer_by_id(self, customer_id: int) -> Customer:
        customers = self.customer_dao.return_all_customers()
        for customer_in_list in customers:
            if customer_in_list.customer_id == customer_id:
                return self.customer_dao.return_customer_by_id(customer_id)
        raise CustomerDoesNotExist("This customer does not exist. Try again.")

    def service_return_all_customers(self):
        customers = self.customer_dao.return_all_customers()
        if len(customers) > 0:
            return self.customer_dao.return_all_customers()
        raise EmptyDatabase("There are no customers available.")

    def service_update_customer_by_id(self, customer: Customer) -> Customer:
        customers = self.customer_dao.return_all_customers()
        for customer_in_list in customers:
            if customer_in_list.customer_id == customer.customer_id:
                return self.customer_dao.update_customer_by_id(customer)
        raise CustomerDoesNotExist("This customer does not exist. Try again.")

    def service_delete_customer_by_id(self, customer_id: int) -> bool:
        customers = self.customer_dao.return_all_customers()
        for customer_in_list in customers:
            if customer_in_list.customer_id == customer_id:
                return self.customer_dao.delete_customer_by_id(customer_id)
        raise CustomerDoesNotExist("This customer does not exist. Try again.")
