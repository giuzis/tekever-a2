from flask import request
from flask_restx import Resource, marshal, fields
from app.api.schemas.account import create_account_schema, account_schema
from app.api.services.account import AccountService
from app.api.services.customer import CustomerService
from app.api.restplus import api

ns = api.namespace(
    'accounts')

account_service = AccountService()
customer_service = CustomerService()

schema_response = api.model('Account Response', {
    'account_id': fields.String(),
    'transaction_id': fields.String(),
})

@ns.route('/')
class AccountCollection(Resource):

    @classmethod
    @ns.marshal_list_with(account_schema)
    def get(cls):
        accounts = account_service.get_all()

        response = []
        for account in accounts:
            response.append(marshal(account, account_schema))

        return response

    
    @classmethod
    @ns.response(201, "Account created.", schema_response)
    @ns.expect(create_account_schema, validate=True)
    def post(cls):
        data = request.json

        if customer_service.check_if_customer_exists_by_id(data['customer_id']): 
            response = account_service.create(data)
            return response
        else:
            return {"message": "Customer Id not found"}, 400
