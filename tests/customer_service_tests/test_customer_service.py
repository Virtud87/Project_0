from custom_exceptions.customer_already_exists import CustomerAlreadyExists
from custom_exceptions.customer_does_not_exist import CustomerDoesNotExist
from data_access_layer.implementation_classes.customer_postgres_dao import CustomerPostgresDAO
from entities.customers import Customer
from service_layer.implemententation_service.customer_postgres_service import CustomerPostgresService

# create the DAO
customer_dao = CustomerPostgresDAO()

# create customer service implemented object and inject customer_dao into service implemented object
customer_service = CustomerPostgresService(customer_dao)

new_customer = Customer(0, "Veronica", "Gomez", "updated@gmail.com")

update_customer = Customer(13, "a", "b", "a@me.com")


def test_validate_service_create_new_customer():
    try:
        customer_service.service_create_new_customer(new_customer)
        assert False
    except CustomerAlreadyExists as e:
        assert str(e) == "This customer already exists!"


def test_validate_service_return_customer_by_id():
    try:
        customer_service.service_return_customer_by_id(13)
        assert False
    except CustomerDoesNotExist as e:
        assert str(e) == "This customer does not exist. Try again."


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
