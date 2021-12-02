from data_access_layer.implementation_classes.customer_postgres_dao import CustomerPostgresDAO
from entities.customers import Customer

customer_dao_postgres = CustomerPostgresDAO()
new_customer_postgres: Customer = Customer(1, "Daniel", "Landeros", "this4mail31@gmail.com")

random_names = {"Bob"}
random_names.add("Sally")
random_names.add("Bill")
random_names.add("Susie")

random_name = random_names.pop()

update_customer = Customer(4, "Updated", "Landeros", "updated@gmail.com")


def test_create_new_customer_success():
    new_customer: Customer = customer_dao_postgres.create_new_customer(new_customer_postgres)
    assert new_customer.customer_id != 0


def test_return_customer_by_id_success():
    returned_customer: Customer = customer_dao_postgres.return_customer_by_id(1)
    assert returned_customer.customer_id == 1


def test_return_all_customers_success():
    returned_customer_list = customer_dao_postgres.return_all_customers()
    assert len(returned_customer_list) >= 2


def test_update_customer_by_id_success():
    # changed parameter to customer from int 1
    updated_customer: Customer = customer_dao_postgres.update_customer_by_id(update_customer)
    assert updated_customer.customer_id == 4


def test_delete_customer_by_id_success():
    confirm_customer_deleted = customer_dao_postgres.delete_customer_by_id(3)
    assert confirm_customer_deleted
