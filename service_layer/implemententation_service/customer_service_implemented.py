from custom_exceptions.customer_already_exists import CustomerAlreadyExists
from custom_exceptions.customer_does_not_exist import CustomerDoesNotExist
from custom_exceptions.empty_database import EmptyDatabase
from data_access_layer.implementation_classes.customer_dao_implemented import CustomerDAOImplemented
from entities.customers import Customer
from service_layer.abstract_service.customer_service import CustomerService

"""
To switch from a local "database" to a cloud-based database, simply pass in a cloud-based implementation object into
the service layer instead of the local implementation object
"""


# BUSINESS LOGIC: validation of requests passing from the API layer to the DAO layer

class CustomerServiceImplemented(CustomerService):
    # Dependency injection
    # with the __init__ function below, all the info in customer_dao will be passed into the service class
    # and this service class will be able to call the appropriate method in the DAO layer
    def __init__(self, customer_dao):
        self.customer_dao: CustomerDAOImplemented = customer_dao

    def service_create_new_customer(self, customer: Customer) -> Customer:
        for customer_in_list in self.customer_dao.customer_list:
            if customer_in_list.email == customer.email:
                raise CustomerAlreadyExists("This customer already exists!")
        return self.customer_dao.create_new_customer(customer)

    def service_return_customer_by_id(self, customer_id) -> Customer:
        for customer_in_list in self.customer_dao.customer_list:
            if customer_in_list.customer_id == customer_id:
                return self.customer_dao.return_customer_by_id(customer_id)
        raise CustomerDoesNotExist("This customer does not exist. Try again.")

    def service_return_all_customers(self):
        if len(self.customer_dao.customer_list) > 0:
            return self.customer_dao.return_all_customers()
        raise EmptyDatabase("There are no customers available.")

    def service_update_customer_by_id(self, customer: Customer) -> Customer:
        for customer_in_list in self.customer_dao.customer_list:
            if customer_in_list.customer_id == customer.customer_id:
                return self.customer_dao.update_customer_by_id(customer)
        raise CustomerDoesNotExist("This customer does not exist. Try again.")

    def service_delete_customer_by_id(self, customer_id):
        for customer_in_list in self.customer_dao.customer_list:
            if customer_in_list.customer_id == customer_id:
                return self.customer_dao.delete_customer_by_id(customer_id)
        raise CustomerDoesNotExist("This customer does not exist. Try again.")
