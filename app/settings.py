from decouple import config

ENV = config("ENV")
DEBUG = ENV == "development"
SECRET_KEY = config("SECRET_KEY")
PORT = config("PORT")

# Flask settings
FLASK_DEBUG = DEBUG  # Do not use debug mode in production