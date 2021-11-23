from abc import ABC, abstractmethod

from entities.customers import Customer


class CustomerService(ABC):
    @abstractmethod
    def service_create_new_customer(self, customer: Customer) -> Customer:
        pass

    @abstractmethod
    def service_return_customer_by_id(self, customer_id: int) -> Customer:
        pass

    @abstractmethod
    def service_return_all_customers(self):
        pass

    @abstractmethod
    def service_update_customer_by_id(self, customer: Customer) -> Customer:
        pass

    @abstractmethod
    def service_delete_customer_by_id(self, customer_id: int) -> bool:
        pass
