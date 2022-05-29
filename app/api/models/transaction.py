from datetime import datetime

class TransactionModel():
    def __init__(self, id, data):
        self.id = id
        self.type = data['type']
        self.account_id = data['account_id']
        self.amount = data['amount']
        self.created_at = data['created_at']

class TransactionDB:
    def __init__(self):
        self.TransactionList = []

    def add(self, new_transaction_obj):
        self.TransactionList.append(new_transaction_obj) 
        return str(new_transaction_obj.id)

    def get_new_id(self):
        new_id = 0
        for transaction in self.TransactionList:
            new_id = max(transaction.id,new_id)
        return new_id + 1

    def get_by_id(self, id):
        for transaction in self.TransactionList:
            if transaction.id == id:
                return transaction
        return None

    def get_by_account_id(self, id):
        return [transaction for transaction in self.TransactionList if transaction.account_id == id]

    def get_all(self):
        return self.TransactionList

