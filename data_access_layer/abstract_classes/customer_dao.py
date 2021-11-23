from abc import ABC, abstractmethod

from entities.customers import Customer


class CustomerDAO(ABC):
    @abstractmethod
    def create_new_customer(self, customer: Customer) -> Customer:
        pass

    @abstractmethod
    def return_customer_by_id(self, customer_id: int) -> Customer:
        pass

    @abstractmethod
    def return_all_customers(self):
        pass

    @abstractmethod
    def update_customer_by_id(self, customer: Customer) -> Customer:
        pass

    @abstractmethod
    def delete_customer_by_id(self, customer_id: int) -> bool:
        pass
