from cmath import acos
from datetime import datetime
from app.api.models import accountDB, transactionDB 
from app.api.models.account import AccountModel
from app.api.models.transaction import TransactionModel

class AccountService():
    def __init__(self):
        pass

    def create(self, new_account):
        if new_account['initialCredit'] < 0:
            return {'message':'initialCredit can not be negative'}, 400
        else:
            new_account_obj = self.create_account_model(new_account)
            account_id = accountDB.add(new_account_obj)
            if new_account['initialCredit'] > 0:
                transaction_id = self.create_initial_transaction(account_id, new_account)
                self.update_account(account_id, new_account['initialCredit'])
                return {'account_id': str(account_id), 'transaction_id': str(transaction_id)}
            else:
                return {'account_id': str(account_id), 'transaction_id': None}

    def update_account(self, id, data):
        return accountDB.update_balance(id, data)

    def create_account_model (self, data):
        return AccountModel(accountDB.get_new_id(), {
            'created_at' : datetime.now(),
            'updated_at' : datetime.now(),
            'customer_id' : int(data['customer_id']),
            'balance' : 0
        })

    def create_initial_transaction(self, account_id, data):
        transaction_obj = TransactionModel(transactionDB.get_new_id(), {
            'type': 'initial_transaction',
            'account_id': account_id,
            'amount': data['initialCredit'],
            'created_at' : datetime.now(),
        })
        return transactionDB.add(transaction_obj)

    def check_if_account_exists_by_customer_id(self, customer_id):
        return accountDB.check_if_exists_by_customer_id(int(customer_id))

    def get_by_customer_id(self, customer_id):
        accounts = accountDB.get_by_customer_id(int(customer_id))
        if len(accounts) is 0:
            return []
        else:
            response = []
            for account in accounts:
                transactions = self.get_transaction_by_account_id(account.id)
                response.append({
                    'id' : account.id,
                    'customer_id' : str(account.customer_id),
                    'balance' : account.balance,
                    'created_at' : account.created_at,
                    'updated_at' : account.updated_at,
                    'transactions' : transactions
                })
        return response

    def get_transaction_by_account_id(self, id):
        transactions = transactionDB.get_by_account_id(int(id))
        if len(transactions) is 0:
            return []
        
        return [{
            'id' : str(transaction.id),
            'type' : transaction.type,
            'amount' : transaction.amount,
            'created_at' : transaction.created_at
        } for transaction in transactions
        ]

    def get_all(self):
        all_accounts_obj = accountDB.get_all()
        accounts = []
        for account_obj in all_accounts_obj:
            account = {
                'id' : account_obj.id,
                'customer_id' : str(account_obj.customer_id),
                'balance' : account_obj.balance,
                'created_at' : account_obj.created_at,
                'updated_at' : account_obj.updated_at,
                'transactions' : self.get_transaction_by_account_id(account_obj.id)
            }
            accounts.append(account)
            
        return accounts

    