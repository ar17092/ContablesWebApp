from .default import *

SECRET_KEY = '9ls_u0qO8TcrGhr68FP3h-3YkcV54l89_mL6A2brXcfXqfpJMDBgwfNOWydQKXjJZTg'

APP_ENV = APP_ENV_PRODUCTION

SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://{username}:{passW}@db4free.net:3306/{dbN}'.format(username='ar17092',passW='ajar24332',dbN='contablesdb')
