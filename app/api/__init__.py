from flask import Blueprint
from app.api.restplus import api
from app.api.resources import customers_namespace, accounts_namespace

blueprintAPI = Blueprint('api', __name__, url_prefix='/api')
api.init_app(blueprintAPI)
api.add_namespace(customers_namespace)
api.add_namespace(accounts_namespace)

__all__ = ["blueprintAPI"]