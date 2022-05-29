from flask_restx import fields
from app.api.restplus import api

transaction_schema = api.model('Transaction Schema', {
    'id': fields.String(required=True),
    'type': fields.String(required=True),
    'amount': fields.Float(),
    'created_at': fields.DateTime()
})