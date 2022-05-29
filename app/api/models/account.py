from datetime import datetime

class AccountModel(object):
    def __init__(self, id, data):
        self.id = id
        self.customer_id = data['customer_id']
        self.balance = data['balance']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

class AccountDB:
    def __init__(self):
        self.AccountList = []

    def add(self, new_account_obj):
        self.AccountList.append(new_account_obj) 
        return new_account_obj.id

    def get_new_id(self):
        new_id = 0
        for account in self.AccountList:
            new_id = max(account.id,new_id)
        return new_id + 1

    def get_by_id(self, id):
        for account in self.AccountList:
            if account.id == id:
                return account
        return None

    def get_by_customer_id(self, id):
        return [account for account in self.AccountList if account.customer_id == id]

    def check_if_exists_by_customer_id(self, customer_id):
        return any(account.customer_id == customer_id for account in self.AccountList)

    def get_all(self):
        return self.AccountList

    def update_balance(self, id, balance):
        account = self.get_by_id(id)
        account.balance = balance
        account.updated_at = datetime.now()
        return account.id

