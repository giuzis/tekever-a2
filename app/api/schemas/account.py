from ast import List
from datetime import datetime
from xmlrpc.client import DateTime
from flask_restx import fields
from app.api.restplus import api
from app.api.schemas.transactions import transaction_schema

create_account_schema = api.model('Create Account Schema', {
    'customer_id': fields.String(required=True),
    'initialCredit': fields.Float(),
})

account_schema = api.model('Account Schema', {
    'id': fields.String(required=True),
    'customer_id': fields.String(required=True),
    'balance': fields.Float(), 
    'created_at': fields.DateTime(),
    'updated_at': fields.DateTime(),
    'transactions':fields.List(fields.Nested(transaction_schema))
})
