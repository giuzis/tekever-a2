
class CustomerModel(object):
    def __init__(self, id, data):
        self.id = id
        self.name = data['name']
        self.surname = data['surname']
        

class CustomerDB:
    def __init__(self):
        self.CustomerList = []


    def add(self, new_customer_obj):
        
        self.CustomerList.append(new_customer_obj) 
        
        return str(new_customer_obj.id)

    def get_new_id(self):
        new_id = 0
        for customer in self.CustomerList:
            new_id = max(customer.id,new_id)

        return new_id + 1

    def check_if_customer_exists_by_id(self, id):
        return any(customer.id == id for customer in self.CustomerList)

    def get_by_id(self, id):
        for customer in self.CustomerList:
            if customer.id == id:
                return customer
        return None

    def get_all(self):
        return self.CustomerList

