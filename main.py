from flask import Flask, request, jsonify

from custom_exceptions.customer_already_exists import CustomerAlreadyExists
from custom_exceptions.customer_does_not_exist import CustomerDoesNotExist
from custom_exceptions.empty_database import EmptyDatabase
from data_access_layer.implementation_classes.customer_postgres_dao import CustomerPostgresDAO
from entities.customers import Customer
from service_layer.implemententation_service.customer_postgres_service import CustomerPostgresService

app: Flask = Flask(__name__)

customer_dao = CustomerPostgresDAO()

customer_service = CustomerPostgresService(customer_dao)


@app.post("/new_customer")
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


@app.get("/get_customer/<customer_id>")
def return_customer_by_id(customer_id: str):
    try:
        customer_returned = customer_service.service_return_customer_by_id(int(customer_id))
        customer_as_dictionary = customer_returned.create_customer_dictionary()
        return jsonify(customer_as_dictionary)
    except CustomerDoesNotExist as e:
        exception_dictionary = {"message": str(e)}
        return jsonify(exception_dictionary)


@app.get("/get_all_customers")
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


@app.patch("/update_customer/<customer_id>")
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


@app.delete("/delete_customer/<customer_id>")
def delete_customer_by_id(customer_id: str):
    try:
        deleted = customer_service.service_delete_customer_by_id(int(customer_id))
        if deleted:
            return f"Customer of ID {customer_id} was deleted successfully!"
        return f"Something went wrong. Customer of Id {customer_id} was not deleted."
    except CustomerDoesNotExist as e:
        exception_dictionary = {"message": str(e)}
        return jsonify(exception_dictionary)


app.run()
