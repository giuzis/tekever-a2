from flask import current_app as app
from flask_restx import Api
from app.extensions import log

authorizations = {
    'Authorization': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization'
    }
}

api = Api(version='1.0', title='Tekever - Assignment 2',
          description="", authorizations=authorizations)

@api.errorhandler
def default_error_handler(error):
    """
    Default error handler method
    :param error: error message
    :return: Message Error response
    """
    message = 'An unhandled exception occurred.'
    log.exception(message)
    log.exception(error)
    if not app.confg["FLASK_DEBUG"]:
        return {'message': message}, 500
    return error