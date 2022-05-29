from importlib.metadata import files
from flask_restx import fields
from app.api.restplus import api
from app.api.schemas.account import account_schema


customer_schema = api.model('Customer Schema', {
    'name': fields.String(required=True),
    'surname': fields.String(required=True),
})

customer_schema_dump = api.clone('Customer Schema Dump', customer_schema, {
    'id': fields.String(description="Customer id")
})

customer_schema_account = api.clone('Customer Schema Dump', customer_schema_dump, {
    'total_balance':fields.Float(),
    'accounts':fields.List(fields.Nested(account_schema))
})