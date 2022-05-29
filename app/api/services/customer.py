from app.api.models import customerDB
from app.api.models.customer import CustomerModel

class CustomerService():
    def __init__(self):
        pass
    def create(self, new_customer_data):
        new_customer_obj = CustomerModel(customerDB.get_new_id(), new_customer_data)
        customer_id = customerDB.add(new_customer_obj)
        return {'id': customer_id}

    def get_all(self):
        all_customers = customerDB.get_all()
        return [
            {
                'id': customer.id, 
                'name': customer.name, 
                'surname': customer.surname
            }
            for customer in all_customers
        ]

    def check_if_customer_exists_by_id(self, id):
        return customerDB.check_if_customer_exists_by_id(int(id))

    def get_by_id(self, customer_id):
        customer = customerDB.get_by_id(int(customer_id))
        return {
            'id': customer.id, 
            'name': customer.name, 
            'surname': customer.surname
        } if customer is not None else None

    