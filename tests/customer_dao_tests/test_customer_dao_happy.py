from data_access_layer.implementation_classes.customer_dao_implemented import CustomerDAOImplemented
from entities.customers import Customer

customer_dao_implementation = CustomerDAOImplemented()
customer = Customer(0, 1, "Jack", "Frost", "frost@gmail.com")
customer_to_update = Customer(3, 1, "Dan", "Bear", "goose@gmail.com")


def test_create_new_customer_success():
    new_customer: Customer = customer_dao_implementation.create_new_customer(customer)
    assert new_customer.customer_id != 0


def test_return_customer_by_id_success():
    returned_customer: Customer = customer_dao_implementation.return_customer_by_id(1)
    assert returned_customer.customer_id == 1


def test_return_all_customers_success():
    returned_customer_list = customer_dao_implementation.return_all_customers()
    assert len(returned_customer_list) >= 2


def test_update_customer_by_id_success():
    updated_customer: Customer = customer_dao_implementation.update_customer_by_id(1)
    assert updated_customer.customer_id == 1


def test_delete_customer_by_id_success():
    confirm_customer_deleted = customer_dao_implementation.delete_customer_by_id(3)
    assert confirm_customer_deleted
