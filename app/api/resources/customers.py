from flask import request
from flask_restx import Resource, marshal, fields
from app.api.schemas.customer import customer_schema, customer_schema_dump, customer_schema_account
from app.api.services.customer import CustomerService
from app.api.services.account import AccountService
from app.api.restplus import api

ns = api.namespace(
    'customers')

customer_service = CustomerService()
account_service = AccountService()

schema_response = api.model('Customer Response', {
    'id': fields.String(),
})

@ns.route('/')
class CustomerCollection(Resource):

    @classmethod
    @ns.marshal_list_with(customer_schema_dump)
    def get(cls):
        customers = customer_service.get_all()

        response = []
        for customer in customers:
            response.append(marshal(customer, customer_schema_dump))

        return response

    
    @classmethod
    @ns.response(201, "Customer created.", schema_response)
    @ns.expect(customer_schema, validate=True)
    def post(cls):
        data = request.json
        return customer_service.create(data)

@ns.route('/<string:customer_id>')
@ns.response(404, 'Customer not found.')
class CustomerItem(Resource):

    @classmethod
    @ns.marshal_with(customer_schema_account)
    def get(cls, customer_id):
        customer = customer_service.get_by_id(customer_id)
        if customer == None:
            return 400, {'message': 'customer_id not found'}
        else:
            accounts = account_service.get_by_customer_id(customer_id)
        

        customer['total_balance'] = 0
        if len(accounts) > 0:
            customer['total_balance'] = sum([float(account['balance']) for account in accounts])
            
        customer['accounts'] = accounts

        return marshal(customer, customer_schema_account)