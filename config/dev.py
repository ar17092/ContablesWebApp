from .default import *

APP_ENV = APP_ENV_DEVELOPMENT

SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://{username}:{passW}@localhost:3306/{dbN}'.format(username='root',passW='',dbN='contablesdb')