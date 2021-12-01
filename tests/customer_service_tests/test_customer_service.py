from custom_exceptions.customer_already_exists import CustomerAlreadyExists
from custom_exceptions.customer_does_not_exist import CustomerDoesNotExist
from custom_exceptions.empty_database import EmptyDatabase
from data_access_layer.implementation_classes.customer_dao_implemented import CustomerDAOImplemented
from entities.customers import Customer

from service_layer.implemententation_service.customer_service_implemented import CustomerServiceImplemented

# create the DAO
customer_dao = CustomerDAOImplemented()

# create customer service implemented object and inject customer_dao into service implemented object
customer_service = CustomerServiceImplemented(customer_dao)

new_customer = Customer(1, 1, "Jieun", "Gu", "jieun@gmail.com")

update_customer = Customer(1, 5, "a", "b", "a@me.com")


def test_validate_service_create_new_customer():
    try:
        customer_service.service_create_new_customer(new_customer)
        assert False
    except CustomerAlreadyExists as e:
        assert str(e) == "This customer already exists!"


def test_validate_service_return_customer_by_id():
    try:
        customer_service.service_return_customer_by_id(1)
        assert False
    except CustomerDoesNotExist as e:
        assert str(e) == "This customer does not exist. Try again."


def test_validate_service_return_all_customers():
    try:
        customer_service.service_return_all_customers()
        assert False
    except EmptyDatabase as e:
        assert str(e) == "There are no customers available."


def test_validate_service_update_customer_by_id():
    try:
        customer_service.service_update_customer_by_id(update_customer)
        assert False
    except CustomerDoesNotExist as e:
        assert str(e) == "This customer does not exist. Try again."


def test_validate_service_delete_customer_by_id():
    try:
        customer_service.service_delete_customer_by_id(13)
        assert False
    except CustomerDoesNotExist as e:
        assert str(e) == "This customer does not exist. Try again."
